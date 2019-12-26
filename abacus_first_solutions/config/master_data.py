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
              "name": "Share",
              "onboard": 1,
              "label": _("Share"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Share Holder Information",
              "onboard": 1,
              "label": _("Share Holder Information"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Store Information",
              "onboard": 1,
              "label": _("Store Information"),
              "description": _("Articles which members issue and return."),
            },
            # {
            #   "type": "doctype",
            #   "name": "District",
            #   "label": _("District"),
            #   "description": _("Articles which members issue and return."),
            # },

          ]
      }
  ]