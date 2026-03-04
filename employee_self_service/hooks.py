app_name = "employee_self_service"
app_title = "Employee Self Service"
app_publisher = "Ismail Irshad"
app_description = "Employee Self Service"
app_email = "irshadsha164@gmail.com"
app_license = "mit"


fixtures = [
    {
        "dt": "Workspace",
        "filters": [
            ["module", "=", "Employee Self Service"]
        ]
    },
     {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Employee"]
        ]
    },
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "employee_self_service",
# 		"logo": "/assets/employee_self_service/logo.png",
# 		"title": "Employee Self Service",
# 		"route": "/employee_self_service",
# 		"has_permission": "employee_self_service.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/employee_self_service/css/employee_self_service.css"
# app_include_js = "/assets/employee_self_service/js/employee_self_service.js"

# include js, css files in header of web template
# web_include_css = "/assets/employee_self_service/css/employee_self_service.css"
# web_include_js = "/assets/employee_self_service/js/employee_self_service.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "employee_self_service/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "employee_self_service/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "employee_self_service.utils.jinja_methods",
# 	"filters": "employee_self_service.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "employee_self_service.install.before_install"
# after_install = "employee_self_service.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "employee_self_service.uninstall.before_uninstall"
# after_uninstall = "employee_self_service.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "employee_self_service.utils.before_app_install"
# after_app_install = "employee_self_service.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "employee_self_service.utils.before_app_uninstall"
# after_app_uninstall = "employee_self_service.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "employee_self_service.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"employee_self_service.tasks.all"
# 	],
# 	"daily": [
# 		"employee_self_service.tasks.daily"
# 	],
# 	"hourly": [
# 		"employee_self_service.tasks.hourly"
# 	],
# 	"weekly": [
# 		"employee_self_service.tasks.weekly"
# 	],
# 	"monthly": [
# 		"employee_self_service.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "employee_self_service.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "employee_self_service.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "employee_self_service.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["employee_self_service.utils.before_request"]
# after_request = ["employee_self_service.utils.after_request"]

# Job Events
# ----------
# before_job = ["employee_self_service.utils.before_job"]
# after_job = ["employee_self_service.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"employee_self_service.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

