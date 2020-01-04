// Copyright (c) 2019, AFS and contributors
// For license information, please see license.txt

frappe.ui.form.on("Partner Information", "last_name", function(frm) {
    frm.set_value('full_name', frm.doc.first_name +" "+ frm.doc.last_name)
});

// frappe.ui.form.on('Partner Information', {
// 	refresh: function(frm) {
// 		frm.add_fetch('state', 'id', 'state');
// 		// add_fetch(link_fieldname, source_fieldname, target_fieldname)
// 	}
// });
