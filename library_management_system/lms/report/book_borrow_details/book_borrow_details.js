// Copyright (c) 2024, Jyothish and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Book Borrow Details"] = {
    filters: [
        {
            fieldname: 'book_serial',
            label: __('Book ID'),
            fieldtype: 'Data',
            
            reqd: 0
        },
        {
            fieldname: 'book_name',
            label: __('Book Name'),
            fieldtype: 'Data',
          
            reqd: 0
        },
        {
            fieldname: 'issued_date',
            label: __('Issue Date'),
            fieldtype: 'Date',
            default: frappe.datetime.nowdate(),
            reqd: 0
        },
        {
            fieldname: 'borrower_name',
            label: __('Borrower Name'),
            fieldtype: 'Data',
            reqd: 0
        },
        {
            fieldname: 'borrower',
            label: __('Borrower Id'),
            fieldtype: 'Data',
            reqd: 0
        }
    ],
    onload: function(report) {
        // Add clear filter button
        report.page.add_inner_button(__('Clear Filters'), function() {
            // Clear all filters
            report.clear_filters();
        });
    }
};
