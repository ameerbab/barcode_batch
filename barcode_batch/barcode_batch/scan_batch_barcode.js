frappe.provide("barcode_batch");

barcode_batch.Controller = frappe.ui.form.Controller.extend({
	scan_batch_barcode: function() {
		let scan_batch_barcode_field = this.frm.fields_dict["scan_batch_barcode"];

		let show_description = function(idx, exist = null) {
			if (exist) {
				scan_batch_barcode_field.set_new_description(__('Row #{0}: Qty increased by 1', [idx]));
			} else {
				scan_batch_barcode_field.set_new_description(__('Row #{0}: Item added', [idx]));
			}
		}

		if(this.frm.doc.scan_batch_barcode) {
			frappe.call({
				method: "erpnext.selling.page.point_of_sale.point_of_sale.search_serial_or_batch_or_barcode_number",
				args: { search_value: this.frm.doc.scan_batch_barcode }
			}).then(r => {
				const data = r && r.message;
				if (!data || Object.keys(data).length === 0) {
					scan_batch_barcode_field.set_new_description(__('Cannot find Item with this barcode'));
					return;
				}

				let cur_grid = this.frm.fields_dict.items.grid;

				let row_to_modify = null;
				const existing_item_row = this.frm.doc.items.find(d => d.item_code === data.item_code && d.batch_no === data.batch_no);
				const blank_item_row = this.frm.doc.items.find(d => !d.item_code);

				if (existing_item_row) {
					row_to_modify = existing_item_row;
				} else if (blank_item_row) {
					row_to_modify = blank_item_row;
                }

				if (!row_to_modify) {
					// add new row
					row_to_modify = frappe.model.add_child(this.frm.doc, cur_grid.doctype, 'items');
				}

				show_description(row_to_modify.idx, row_to_modify.item_code);

				this.frm.from_barcode = true;
				frappe.model.set_value(row_to_modify.doctype, row_to_modify.name, {
                    batch_no: data.batch_no,
					item_code: data.item_code,
					qty: (row_to_modify.qty || 0) + 1
                });


				['serial_no', 'batch_no', 'barcode'].forEach(field => {
					if (data[field] && frappe.meta.has_field(row_to_modify.doctype, field)) {
						frappe.model.set_value(row_to_modify.doctype,
							row_to_modify.name, field, data[field]);
					}
				});

				scan_batch_barcode_field.set_value('');
			});
		}
		return false;
	},
});

erpnext.stock.select_batch_and_serial_no = (frm, item) => {
	let get_warehouse_type_and_name = (item) => {
		let value = '';
		if(frm.fields_dict.from_warehouse.disp_status === "Write") {
			value = cstr(item.s_warehouse) || '';
			return {
				type: 'Source Warehouse',
				name: value
			};
		} else {
			value = cstr(item.t_warehouse) || '';
			return {
				type: 'Target Warehouse',
				name: value
			};
		}
	}

	if(item && item.has_serial_no
		&& frm.doc.purpose === 'Material Receipt') {
		return;
	}

	frappe.require("assets/erpnext/js/utils/serial_no_batch_selector.js", function() {
		new erpnext.SerialNoBatchSelector({
			frm: frm,
			item: item,
			warehouse_details: get_warehouse_type_and_name(item),
		});
	});

}

$.extend(cur_frm.cscript, new barcode_batch.Controller({frm: cur_frm}));
