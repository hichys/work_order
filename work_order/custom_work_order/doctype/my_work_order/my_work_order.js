frappe.ui.form.on('my work order', {
    onload:function(frm) {
        
        //frappe.msgprint("on load")
        fetchSalesInvoiceItems(frm);
        updateItemsTable(frm)
    },
    before_save: function(frm) {
         //frappe.msgprint("before save")
        // Fetch items before saving the form
        fetchSalesInvoiceItems(frm);
    },
    refresh: function(frm) {
        
        //frappe.msgprint("refersh")
        // Add a trigger for the 'sales_invoice' field change
        frm.fields_dict['sales_invoice_number'].$input.on('change', function() {
            // Fetch items based on the selected Sales Invoice
            
            fetchSalesInvoiceItems(frm);
            updateItemsTable(frm)
        });
        
        
    }
});

function fetchSalesInvoiceItems(frm) {
    var sales_invoice_name = frm.doc.sales_invoice_number;
   
    if (sales_invoice_name) {
        frappe.run_serially([
            function() {
                return frappe.call({
                    method: 'work_order.custom_work_order.doctype.my_work_order.my_work_order.get_sales_invoice_items',
                    args: {
                        sales_invoice_name: sales_invoice_name
                    },
                    callback: function(response) {
                        if (response.message) {
                            var items = response.message;

                            // Set the fetched items as options in the 'items' select field
                            frm.set_df_property('items', 'options', items);
                            frm.clear_table('items_table');
                            // Set the default value to the first item
                            frm.set_value('items', items[0].value );
                            // Refresh the 'items' select field
                            frm.refresh_field('items');
                        }
                    }
                });
            }
        ]);
    }
}
function updateItemsTable(frm) {
    var total_qty=0;
    // Clear existing items in the table
    frm.clear_table('items_table');

    // Fetch items from the selected Sales Invoice
    if (frm.doc.sales_invoice_number) {
        frappe.call({
            method: 'work_order.custom_work_order.doctype.my_work_order.my_work_order.get_sales_invoice_items',
            args: {
                sales_invoice_name: frm.doc.sales_invoice_number
            },
            callback: function(response) {
                if (response.message) {
                    // Iterate through the fetched items and add them to the table
                    response.message.forEach(function(item) {
                        frm.add_child('items_table', {
                            item_code: item.value,
                            item_name: item.label.split(' - ')[0],
                            qty: parseFloat(item.label.split(' - Qty: ')[1]) || 1,
                            // Add other fields as needed
                        });
                    });

                    // Refresh the table to display the changes
                    frm.refresh_field('items_table');
                }
            }
        });
    }
}

