# -*- coding: utf-8 -*-
# Copyright (c) 2020, AFS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class DistrictManager(Document):
	def validate(self):
		self.full_name = ' '.join(filter(lambda x: x, [self.first_name, self.last_name]))
