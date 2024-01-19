# Copyright (c) 2024, Jyothish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Members(Document):
    # Script to automatically create Details record when a new Member is added

    def after_insert(self):
        # Create a new Details record
        details = frappe.new_doc("Details")
        details.roll_no = self.roll_no
        details.name1 = self.name1
        details.department = self.department
        details.image = self.image
        details.year = self.year
        details.phone = self.phone
        details.address = self.address
        
        # Add more fields as needed
        details.insert(ignore_permissions=True)
 