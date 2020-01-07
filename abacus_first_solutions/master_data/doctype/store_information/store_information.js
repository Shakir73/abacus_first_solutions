


// frappe.ui.form.on('Share', {
//     share_:function(frm, cdt, cdn){
//     var d = locals[cdt][cdn];
//     var total = 0;
//     frm.doc.partner.forEach(function(d) { total += d.share_; });
//     frm.set_value('total_per', total);
//     refresh_field('total_per');
//     },
//     partner_remove:function(frm, cdt, cdn){
//     var d = locals[cdt][cdn];
//     var total = 0;
//     frm.doc.partner.forEach(function(d) { total += d.share_; });
//     frm.set_value('total_per', total);
//     refresh_field('total_per');
//     }
//     });


frappe.ui.form.on("Share", {
    share_: function(frm) {
    var grand_total = 0;
    for(var i=0;i<frm.doc.partner.length;i++) {
        grand_total += frm.doc.partner[i].share_;
    }
    frm.set_value("total_per", grand_total);
    refresh_field('total_per');
}
});
