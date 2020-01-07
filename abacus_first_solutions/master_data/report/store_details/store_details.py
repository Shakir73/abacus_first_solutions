# Copyright (c) 2013, AFS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_report_columns()
    data = get_report_data(filters)
    # columns, data = [], []
    return columns, data

def get_report_columns():
    columns = [{
		"fieldname": "legal_name",
		"label": _("Business Name"),
		"fieldtype": "Data",
		"width": 200
	},
    {
		"fieldname": "store_no",
		"label": _("Store No"),
		"fieldtype": "Data",
		"width": 100
	},
    {
		"fieldname": "legal_mailing_address",
		"label": _("Legal Address"),
		"fieldtype": "Data",
		"width": 200
	},]
    
    return columns

def get_report_data(filters=None):
    data = get_orders(filters)
    return data

def get_orders(filters):
    test_q = """select legal_name, store_no, legal_mailing_address from `tabStore Information`"""
    return frappe.db.sql(test_q, as_dict=True)