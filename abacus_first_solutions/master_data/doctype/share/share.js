// Copyright (c) 2019, AFS and contributors
// For license information, please see license.txt

frappe.ui.form.on("Share", {
  share_:function(frm, cdt, cdn){
  var d = locals[cdt][cdn];
  var total = 0;
  frm.doc.partner.forEach(function(d) { total += d.share_; });
  frm.set_value("total_per", total);
  refresh_field("total_per");
},
  partner_remove:function(frm, cdt, cdn){
  var d = locals[cdt][cdn];
  var total = 0;
  frm.doc.partner.forEach(function(d) { total += d.share_; });
  frm.set_value("total_per", total);
  refresh_field("total_per");
    }
  });
