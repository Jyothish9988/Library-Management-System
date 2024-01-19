
frappe.ui.form.on('Transaction', {
    refresh: function(frm) {
        frm.add_custom_button(__('Scan Book Serial'), function() {
            scanBarcode(frm, 'book_serial', 'book_serial');
        });

        frm.add_custom_button(__('Calculate Fine'), function() {
            calculateFine(frm);
        });
    },
    page_refresh: function(frm) {
        calculateFine(frm);
    }
});

// Function for handling barcode
function scanBarcode(frm, fieldToUpdate, idField) {
    frappe.prompt({
        label: __('Scan book serial'),
        fieldname: idField,
        fieldtype: 'Link',
        options: 'Borrower',
    }, function(values) {
        frm.set_value(fieldToUpdate, values[idField]);
        calculateFine(frm);  // Recalculate fine after setting the book serial
    }, __('Book Serial Scanner'));
}

function calculateFine(frm) {
    var dueDate = frm.doc.due_date;
    var currentDate = frappe.datetime.now_datetime();

    if (dueDate && currentDate) {
        var overdueDays = frappe.datetime.get_diff(currentDate, dueDate);
        var fineRatePerDay = 5;  // Adjust this based on your requirements
        var fineAmount = Math.max(overdueDays, 0) * fineRatePerDay;

        frm.set_value('fine_amount', fineAmount);
        frm.refresh_field('fine_amount');
    }
}
