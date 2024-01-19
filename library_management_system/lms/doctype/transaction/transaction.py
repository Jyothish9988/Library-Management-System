# Copyright (c) 2024, Jyothish and contributors
# For license information, please see license.txt
import datetime
import frappe
from frappe.website.website_generator import WebsiteGenerator

class Transaction(WebsiteGenerator):
    # time
    def validate(self):
        if not self.date_time:
            self.date_time = frappe.utils.now()

    def on_submit(self):
        # When a Borrower record is submitted, update the related Book status to 'Available'
        if self.book_serial:
            book = frappe.get_doc("Book", self.book_serial)
            if book:
                book.status = "Available"
                book.save()

                # Update the b_status in the related Borrower record
                borrower = frappe.get_value("Borrower", {"book_serial": self.book_serial}, "name")
                if borrower:
                    frappe.set_value("Borrower", borrower, "b_status", "Returned")
        
        if self.name1:
            details_doc = frappe.get_doc("Details", self.name1)
            if details_doc:
                details_doc.due_date = self.due_date
                details_doc.fine_amount = self.fine_amount
                details_doc.status = "No Pending Book Returns"
                # details_doc.date_time = self.date_time(details have no fields set)
                details_doc.save()
