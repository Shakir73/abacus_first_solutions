// Copyright (c) 2019, AFS and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Store Information", "usa_state", function(frm) {
//     frm.set_value('state', frm.doc.usa_state)
// });

// frappe.ui.form.on("Store Information", "partner_id", function(frm) {
//     frm.set_value('full_name', frm.doc.first_name +" "+ frm.doc.last_name)
// });

// frappe.ui.form.on('Store Information', {
// 	refresh: function(frm) {
// 		frm.add_fetch('usa_state', 'state', 'usa_state');
// 		// add_fetch(link_fieldname, source_fieldname, target_fieldname)
// 	}
// });

frappe.ui.form.on('Store Information', {
	refresh: function(frm) {
		frm.add_fetch('usa_state', 'id', 'state');
		// add_fetch(link_fieldname, source_fieldname, target_fieldname)
	}
});

frappe.ui.form.on("Store Information", {
	"partner_share": function(frm) {
        frm.add_fetch("partner_share", "store_no", "store_id");
        // add_fetch(link_fieldname, source_fieldname, target_fieldname)
	}
});

