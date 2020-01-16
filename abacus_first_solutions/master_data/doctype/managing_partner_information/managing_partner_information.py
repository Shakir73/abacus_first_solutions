# -*- coding: utf-8 -*-
# Copyright (c) 2020, AFS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ManagingPartnerInformation(Document):
	def __setup__(self):
    		self.onload()

	def onload(self):
		self.load_stores()

	def load_stores(self):
		self.managing_partner = []
		store = frappe.get_all("Managing Partner Child", filters={"managing_partner": self.name}, fields = ["parent"])
		for st in store:
			self.append("managing_partner", {
				"legal_name": st.parent,
				"store_no": frappe.db.get_value("Store Information", st.parent, "store_no"),
				# "share": frappe.db.get_value("Share", st.parent, "share_")
				# "share": st.share_
			})
		self.total_stores = len(self.managing_partner)
	def validate(self):
		self.full_name = ' '.join(filter(lambda x: x, [self.first_name, self.last_name]))
		self.managing_partner = []
