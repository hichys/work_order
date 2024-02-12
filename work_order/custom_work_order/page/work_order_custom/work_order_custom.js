frappe.pages['work-order-custom'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'امر العمل',
		single_column: true
	});
}