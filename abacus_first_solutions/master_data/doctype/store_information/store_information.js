// Copyright (c) 2019, AFS and contributors
// For license information, please see license.txt

frappe.ui.form.on("Store Information", "usa_state", function(frm) {
    frm.set_value('state', frm.doc.usa_state)
});

// frappe.ui.form.on("Store Information", "partner_id", function(frm) {
//     frm.set_value('full_name', frm.doc.first_name +" "+ frm.doc.last_name)
// });
