# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "barcode_batch"
app_title = "Barcode Batch"
app_publisher = "vinhnguyen.t090@gmail.com"
app_description = "Barcode Batch"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vinhnguyen.t090@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/barcode_batch/css/barcode_batch.css"
# app_include_js = "/assets/barcode_batch/js/barcode_batch.js"

# include js, css files in header of web template
# web_include_css = "/assets/barcode_batch/css/barcode_batch.css"
# web_include_js = "/assets/barcode_batch/js/barcode_batch.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Item" : "custom_scripts/item_custom.js",
	"Stock Entry" : "custom_scripts/stock_entry_custom.js",
	"Delivery Note" : "custom_scripts/delivery_note_custom.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "barcode_batch.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "barcode_batch.install.before_install"
# after_install = "barcode_batch.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "barcode_batch.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"barcode_batch.tasks.all"
# 	],
# 	"daily": [
# 		"barcode_batch.tasks.daily"
# 	],
# 	"hourly": [
# 		"barcode_batch.tasks.hourly"
# 	],
# 	"weekly": [
# 		"barcode_batch.tasks.weekly"
# 	]
# 	"monthly": [
# 		"barcode_batch.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "barcode_batch.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "barcode_batch.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "barcode_batch.task.get_dashboard_data"
# }

