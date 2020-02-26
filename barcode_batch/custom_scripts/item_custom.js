frappe.ui.form.on("Item", {
	validate: function(frm) {
		if(frm.doc.has_batch_no && frm.doc.create_new_batch && frm.doc.item_code && !frm.doc.batch_number_series){
			frm.set_value("batch_number_series", frm.doc.item_code + " .YY.MM.##");
		}
	}
});