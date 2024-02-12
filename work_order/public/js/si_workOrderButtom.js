
frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        // Add a custom button after submission
        if (frm.doc.docstatus == 1) {  // Check if the document is submitted
            frm.add_custom_button(__('امر عمل'), function() {
                // Fetch items list from Sales Invoice
                const items_list = frm.doc.items.map(item => {
                    return {
                        'item_code': item.item_code,
                        'item_name': item.item_name,
                        'qty': item.qty,
                        'rate': item.rate,
                        // Add other fields as needed
                    };
                });

                // Create a new My Work Order document
                frappe.model.with_doctype('my work order', function() {
                    const wo = frappe.model.get_new_doc('my work order');

                    // Set the items list to the Table field in My Work Order
                    
                    // Set other fields as needed
                    wo.sales_invoice_number = frm.doc.name;
                    
                    // Set the name before saving
                    
                    frm.refresh_field('wo.items');  
                   
                    frm.set_value('items',items_list[0]);
                    
                    // Save the My Work Order document
                     
                        // Navigate to the newly created My Work Order document
                        frappe.set_route('Form', wo.doctype, wo.name);
                    
                        
                 
                        console.log(items_list[0]);
                     
                });
            }, __('Create'));
        }
    }
});
