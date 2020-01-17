from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Setup"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Store Information",
              "onboard": 1,
              "label": _("Store Information"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Partner Information",
              "onboard": 1,
              "label": _("Partner Information"),
              "description": _("Articles which members issue and return."),
            },
            
            {
              "type": "doctype",
              "name": "Managing Partner Information",
              "label": _("Managing Partner Information"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "District Manager",
              "label": _("District Manager"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Shift Manager",
              "label": _("Shift Manager"),
              "description": _("Articles which members issue and return."),
            },

          ]
      }
  ]