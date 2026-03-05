import frappe
import json

@frappe.whitelist()
def get_location(latitude, longitude):
    # frappe.msgprint(f"Received location: Latitude={latitude}, Longitude={longitude}")
    
    user = frappe.session.user

    employee = frappe.get_value(
        "Employee",
        {"user_id": user},
        ["name", "custom_site_location", "custom_allowed_radius"],
        as_dict=True
    )
    
    if not employee:
        return f"No Employee linked to {user}"
    
    if not employee.custom_site_location:
        return "Site location not defined for employee"

    print("location data:", employee.custom_site_location)
# location data:
# {
#   "type": "FeatureCollection",
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Point",
#         "coordinates": [77.622292, 12.953445]
#       }
#     }
#   ]
# }
    location_data = json.loads(employee.custom_site_location)
    
    if not location_data.get("features"):
        return "Site location not defined for employee"
    
    site_longitude = location_data["features"][0]["geometry"]["coordinates"][0]
    site_latitude = location_data["features"][0]["geometry"]["coordinates"][1]
    
# to understand the degree of latitude and longitude in meters
# 1 degree ≈ 111 km
# 0.001 degree ≈ 111 meters
# 0.0045 degree ≈ 50 meters
    allowed_radius = employee.custom_allowed_radius or 50
    radius_in_degree = allowed_radius / 111000

    if abs(float(site_latitude) - float(latitude)) <= radius_in_degree and abs(float(site_longitude) - float(longitude)) <= radius_in_degree:
      
       last_checkin = frappe.get_all(
           "Employee Checkin",
           filters = {"employee": employee.name},
           fields = ["log_type"],
           order_by = "time desc",
           limit =1
       )

       if last_checkin and last_checkin[0].log_type == "IN":
           return "You have already checked in"
       
       frappe.get_doc({
           "doctype": "Employee Checkin",
           "employee": employee.name,
           "log_type": "IN" 
       }).insert()

       return "Check_in Successfull"
    
    return frappe.msgprint("You are not within the " + str(allowed_radius) + " mtrs of work location")

@frappe.whitelist()
def handle_checkout(latitude, longitude):
    user = frappe.session.user

    employee = frappe.get_value(
        "Employee",
        {"user_id": user},
        ["name", "custom_site_location", "custom_allowed_radius"],
        as_dict=True
    )

    if not employee:
        return f"No Employee linked to {user}"
    
    if not employee.custom_site_location:
        return "Site location not defined for employee"

    
    location_data = json.loads(employee.custom_site_location)
    
    site_longitude = location_data["features"][0]["geometry"]["coordinates"][0]
    site_latitude = location_data["features"][0]["geometry"]["coordinates"][1]
    

    allowed_radius = employee.custom_allowed_radius or 50
    radius_in_degree = allowed_radius / 111000

    if abs(float(site_latitude) - float(latitude)) <= radius_in_degree and abs(float(site_longitude) - float(longitude)) <= radius_in_degree:
        
        last_checkout = frappe.get_all(
           "Employee Checkin",
           filters = {"employee": employee.name},
           fields = ["log_type"],
           order_by = "time desc",
           limit =1
       )
        if not last_checkout:
           return "Please Check In First"

        if last_checkout and last_checkout[0].log_type == "OUT":
           return "You have already checked out"
       

        frappe.get_doc({
           "doctype": "Employee Checkin",
           "employee": employee.name,
           "log_type": "OUT" 
        }).insert()

        return "Check_out Successfull"
    return frappe.msgprint("You are not within the " + str(allowed_radius) + " mtrs of work location")

