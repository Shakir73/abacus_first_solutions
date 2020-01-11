# -*- coding: utf-8 -*-
# Copyright (c) 2019, AFS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PartnerInformation(Document):
	def __setup__(self):
		self.onload()

	def onload(self):
		self.load_stores()

	def load_stores(self):
		self.store = []
		store = frappe.get_all("Share", filters={"partner_id": self.name}, fields = ["parent", "share_"])
		for st in store:
			self.append("store", {
				"legal_name": st.parent,
				"store_no": frappe.db.get_value("Store Information", st.parent, "store_no"),
				# "share": frappe.db.get_value("Share", st.parent, "share_")
				"share": st.share_
			})

		self.total_stores = len(self.store)




	def validate(self):
		# if self.total_stores == 0:
		# 	self.enabled = 0
		self.store = []
		self.full_name = f"{self.first_name} {self.last_name}"
