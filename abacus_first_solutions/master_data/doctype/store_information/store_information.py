# -*- coding: utf-8 -*-
# Copyright (c) 2019, AFS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class StoreInformation(Document):
    
	"""Calculate total percentage and warn duplicate."""
	def validate(self):
		
		found = []
		self.total_per = 0
		for d in self.partner:
			self.total_per +=d.share_
			if d.partner_id in found:
				# frappe.throw(_("partner {0} entered twice").format(d.full_name))
				frappe.throw(_(f"partner '{d.full_name}' entered twice"))
			found.append(d.partner_id)
			if self.total_per > 100:
				frappe.throw(_(f"Total Share is '{self.total_per}', not equal to 100"))
			

