# Copyright (c) 2024, Jyothish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Attendance(Document):
    def on_submit(self):
        if self.roll_no:
            details_doc = frappe.get_doc("Details", self.roll_no)
            if details_doc:
                details_doc.check_in = self.checkin_time
                details_doc.check_out = self.checkout_time
                details_doc.save()

