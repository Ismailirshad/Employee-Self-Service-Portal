import frappe

@frappe.whitelist()
def get_location(lattitude, longitude):
    frappe.msgprint(f"Received location: Latitude={lattitude}, Longitude={longitude}")
    
    user = frappe.session.user

    employee = frappe.get_value(
        "Employee",
        {"user_id": user},
        ["name", "custom_site_lattitude", "custom_site_longitude"],
        as_dict=True
    )

    if not employee:
        return f"No Employee linked to {user}"
    
# to understand the degree of latitude and longitude in meters
#     0.01 degree ≈ 1.11 km
#     0.001 degree ≈ 111 meters
#     0.0001 degree ≈ 11 meters

    if abs(float(employee.custom_site_lattitude) - float(lattitude)) <= 0.001 and abs(float(employee.custom_site_longitude) - float(longitude)) <= 0.01:
       
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
    
    return frappe.msgprint("You are not within the 100 mtrs of work location")
        
@frappe.whitelist()
def handle_checkout():
    user = frappe.session.user

    employee = frappe.get_value(
        "Employee",
        {"user_id": user},
        ["name"],
        as_dict=True
    )

    if not employee:
        return f"No Employee linked to {user}"
    
    last_checkout = frappe.get_all(
           "Employee Checkin",
           filters = {"employee": employee.name},
           fields = ["log_type"],
           order_by = "time desc",
           limit =1
       )

    if last_checkout and last_checkout[0].log_type == "OUT":
           return "You have already checked out"
       

    frappe.get_doc({
           "doctype": "Employee Checkin",
           "employee": employee.name,
           "log_type": "OUT" 
        }).insert()

    return "Check_out Successfull"

