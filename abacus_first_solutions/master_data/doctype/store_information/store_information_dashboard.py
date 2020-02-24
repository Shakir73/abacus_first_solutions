from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on the activities of this Store'),
		'fieldname': 'store_name',
		'transactions': [
			{
				'label': _('Actvities'),
				'items': ['Store Payrolls',]
			},
			# {
			# 	'label': _('Partners'),
			# 	'items': ['Partner Information',]
			# },
			# {
			# 	'label': _('Assessment'),
			# 	'items': ['Assessment Result']
			# },
			# {
			# 	'label': _('Student LMS Activity'),
			# 	'items': ['Course Activity', 'Quiz Activity' ]
			# },
			# {
			# 	'label': _('Attendance'),
			# 	'items': ['Student Attendance', 'Student Leave Application']
			# },
			# {
			# 	'label': _('Fee'),
			# 	'items': ['Fees']
			# }
		]
	}