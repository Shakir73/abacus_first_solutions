# -*- coding: utf-8 -*-
# Copyright (c) 2020, AFS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class ManagingPartner(Document):
	def validate(self):
		# if not self.full_name:
		self.full_name = f"{self.first_name} {self.last_name}"
