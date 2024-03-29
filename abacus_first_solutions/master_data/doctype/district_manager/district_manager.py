# -*- coding: utf-8 -*-
# Copyright (c) 2020, AFS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DistrictManager(Document):
	def __setup__(self):
    		self.onload()

	def onload(self):
		self.load_stores()

	def load_stores(self):
		self.district_manager = []
		store = frappe.get_all("District Manager Details", filters={"district_manager": self.name}, fields = ["parent"])
		for st in store:
			self.append("district_manager", {
				"legal_name": st.parent,
				"store_no": frappe.db.get_value("Store Information", st.parent, "store_no"),
				# "share": frappe.db.get_value("Share", st.parent, "share_")
				# "share": st.share_
			})
		self.total_stores = len(self.district_manager)
	def validate(self):
		self.full_name = ' '.join(filter(lambda x: x, [self.first_name, self.last_name]))
		self.managing_partner = []
