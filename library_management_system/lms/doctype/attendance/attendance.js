frappe.ui.form.on('Attendance', {
    refresh: function(frm) {
        // Add a button to trigger the barcode scanner for check-in
        frm.add_custom_button(__('Scan Check-In'), function() {
            scanBarcode(frm, 'checkin_time', 'roll_no');
        });

        // Add a button to trigger the barcode scanner for check-out
        frm.add_custom_button(__('Scan Check-Out'), function() {
            scanBarcode(frm, 'checkout_time', 'roll_no');
        });
    }
});

// Function to handle barcode scanning
function scanBarcode(frm, timeField, idField) {
    // Open a modal to display the input field for barcode
    frappe.prompt({
        label: __('Scan ID Card'),
        fieldname: idField,
        fieldtype: 'Link',
        options: 'Members',
    }, function(values) {
        // After the barcode is scanned, set the user_id (roll_no) and update the time field
        frm.set_value(idField, values[idField]);
        frm.set_value(timeField, frappe.datetime.now_datetime());
    }, __('ID Card Scanner'));
}
