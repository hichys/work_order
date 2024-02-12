app_name = "work_order"
app_title = "Work Order"
app_publisher = "awad"
app_description = "sales work order"
app_email = "awad4430@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/work_order/css/work_order.css"
# app_include_js = "/assets/work_order/js/work_order.js"

 
# include js, css files in header of web template
# web_include_css = "/assets/work_order/css/work_order.css"
# web_include_js = "/assets/work_order/js/work_order.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "work_order/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Sales Invoice" : "public/js/si_workOrderButtom.js"}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "work_order/public/icons.svg"

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
# 	"methods": "work_order.utils.jinja_methods",
# 	"filters": "work_order.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "work_order.install.before_install"
# after_install = "work_order.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "work_order.uninstall.before_uninstall"
# after_uninstall = "work_order.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "work_order.utils.before_app_install"
# after_app_install = "work_order.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "work_order.utils.before_app_uninstall"
# after_app_uninstall = "work_order.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "work_order.notifications.get_notification_config"

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
doc_events = {
    "my work order": {
        "on_amend":"work_order.custom_work_order.doctype.my_work_order.on_amend",
    },
}
fixtures = ["Print Format"]
fixtures = [{
	"doctype": "DocType",
            "filters": { "custom" : ["=", "1"] }
           }, 
    	"Custom Field",
    	"Custom Script",
    	"Property Setter",
            "Print Format"
       ]
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"work_order.tasks.all"
# 	],
# 	"daily": [
# 		"work_order.tasks.daily"
# 	],
# 	"hourly": [
# 		"work_order.tasks.hourly"
# 	],
# 	"weekly": [
# 		"work_order.tasks.weekly"
# 	],
# 	"monthly": [
# 		"work_order.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "work_order.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "work_order.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "work_order.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["work_order.utils.before_request"]
# after_request = ["work_order.utils.after_request"]

# Job Events
# ----------
# before_job = ["work_order.utils.before_job"]
# after_job = ["work_order.utils.after_job"]

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
# 	"work_order.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

