// Copyright (c) 2019, AFS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Share', {
	refresh: function(frm) {
	    frm.add_fetch('partner_id', 'first_name', 'first_name');
	    frm.add_fetch('partner_id', 'last_name', 'last_name');
	}
});

frappe.ui.form.on('Share', {
	refresh: function(frm) {
		frm.add_fetch('store_no', 'legal_name', 'legal_name');
		// add_fetch(link_fieldname, source_fieldname, target_fieldname)
	}
});

frappe.ui.form.on("Share", {
    "partner_id" : function(frm) {
        frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Partner Information",
                name: frm.doc.partner_id
            },
            callback: function (data) {
                frappe.model.set_value(frm.doctype,
                    frm.docname, "full_name",
                    data.message.first_name
                    + (data.message.last_name ?
                        (" " + data.message.last_name) : ""))
            }
        })
    }
});
