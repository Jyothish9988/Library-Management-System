# borrower.py
# Copyright (c) 2024, Jyothish and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Borrower(WebsiteGenerator):
    def validate(self):
        # Set the current date in the 'issued_date' field when saving a new Borrower record
        if not self.issued_date:
            self.issued_date = frappe.utils.nowdate()

    def on_submit(self):
        # When a Borrower record is submitted, update the related Book status to 'Not Available'
        if self.book_serial:
            book = frappe.get_doc("Book", self.book_serial)
            
            if book:
                book.status = "Not Available"
                book.save()

        # Update the 'book_name' field in the related "Details" document
        if self.borrower:
            details_doc = frappe.get_doc("Details", self.borrower)
            if details_doc:
                # Replace with the correct fields from Borrower
                details_doc.issued_date = self.issued_date
                details_doc.return_date = self.return_date
                details_doc.book_serial = self.book_serial
                details_doc.status = "Book Borrowed"
                details_doc.book_name = self.book_name
                details_doc.save()
