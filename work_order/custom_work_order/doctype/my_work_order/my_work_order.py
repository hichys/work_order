# Copyright (c) 2024, awad and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from frappe import _, ValidationError
from frappe.model.document import Document


class myworkorder(Document):
# In your my_work_order.py file

    def on_amend(doc, method=None):
        frappe.msgprint("on_update triggered!")
    # Rest of the function
# Import frappe module
        
# Validate method for my work order
    def validate(doc, method=None):
        # Check if the document is new and the sales_invoice_number field is not empty
        if doc.is_new() and doc.sales_invoice_number:
            # Check if another document with the same sales_invoice_number exists
            existing_doc = frappe.get_all(
                'my work order',
                filters={
                    'sales_invoice_number': doc.sales_invoice_number,
                    'name': ('!=', doc.name) if doc.name else None  # Exclude the current document from the check if it's being updated
                },
                fields=['name'],
                limit=1
            )

            if existing_doc:
                frappe.throw(_("امر العمل موجود"))


    # def validate(doc, method=None):
    #     #frappe.msgprint("validate triggered!")
	# #only validate on new doctype
    #     if doc.is_new() :
	# 	    # Check if a document with the same values for sales_invoice_number and items already exists
    #         existing_doc = frappe.get_all(
	# 		'my work order',
	# 		filters={'sales_invoice_number': doc.sales_invoice_number, 'items': doc.items, 'name': ('!=', doc.name)},
	# 		fields=['name'],
	# 		limit=1
	# 	    )

    #         if existing_doc:
    #             frappe.msgprint("امر العمل موجود")
    #             raise ValidationError(_("A document with the same values for Sales Invoice Number and Items already exists."))

		    # Continue with other validation logic or save the document
		    # ...
#    def on_change(doc,method=None):
#        sales_invoice_number_on_update(doc,method)



# In your 'My Work Order' DocType Python script (my_work_order.py)

@frappe.whitelist()
def get_sales_invoice_items(sales_invoice_name):
    # Fetch Sales Invoice items based on the provided Sales Invoice name
    sales_invoice_items = frappe.db.sql("""
        SELECT item_code, qty
        FROM `tabSales Invoice Item`
        WHERE parent = %s
    """, (sales_invoice_name,), as_dict=True)

    # Format items and quantities as options
    options = [{'value': item.item_code, 'label': f"Item Code: {item.item_code} - Qty: {item.qty}"} for item in sales_invoice_items]

    # Log the fetched items to the console
    frappe.logger().info("Fetched items from Sales Invoice: {0}".format(options))

    return options