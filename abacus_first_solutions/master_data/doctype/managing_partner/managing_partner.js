// Copyright (c) 2020, AFS and contributors
// For license information, please see license.txt


frappe.ui.form.on("Managing Partner", "last_name", function(frm) {
    frm.set_value('full_name', frm.doc.first_name +" "+ frm.doc.last_name)
});
