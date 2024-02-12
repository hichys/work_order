# your_app/your_module/your_script.py

import frappe

@frappe.whitelist()
def transition_to_next_workflow_state(docname, workflow_state_field):
    doc = frappe.get_doc('my work order', docname)
    current_state = doc.get(workflow_state_field)

    # Get the next state in the workflow
    next_state = frappe.get_all('Workflow Document State', filters={'parent': doc.workflow_id, 'state': current_state}, fields=['next_state'])

    if next_state:
        next_state = next_state[0].next_state

        # Update the workflow state field
        doc.set(workflow_state_field, next_state)
        doc.save()

        return next_state

    return None
