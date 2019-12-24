# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "abacus_first_solutions"
app_title = "Master Data"
app_publisher = "AFS"
app_description = "Abacus First Solutions"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "afs@afs.com"
app_license = "AFS"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/abacus_first_solutions/css/abacus_first_solutions.css"
# app_include_js = "/assets/abacus_first_solutions/js/abacus_first_solutions.js"

# include js, css files in header of web template
# web_include_css = "/assets/abacus_first_solutions/css/abacus_first_solutions.css"
# web_include_js = "/assets/abacus_first_solutions/js/abacus_first_solutions.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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
# get_website_user_home_page = "abacus_first_solutions.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "abacus_first_solutions.install.before_install"
# after_install = "abacus_first_solutions.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "abacus_first_solutions.notifications.get_notification_config"

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
# 		"abacus_first_solutions.tasks.all"
# 	],
# 	"daily": [
# 		"abacus_first_solutions.tasks.daily"
# 	],
# 	"hourly": [
# 		"abacus_first_solutions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"abacus_first_solutions.tasks.weekly"
# 	]
# 	"monthly": [
# 		"abacus_first_solutions.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "abacus_first_solutions.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "abacus_first_solutions.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "abacus_first_solutions.task.get_dashboard_data"
# }

