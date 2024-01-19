# Copyright (c) 2024, Jyothish and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "book_serial", "label": ("Book ID"), "fieldtype": "Link", "options": "Book", "width": 100},
        {"fieldname": "book_name", "label": ("Book Name"), "fieldtype": "Link", "options": "Book", "width": 150},
        {"fieldname": "borrower_name", "label": ("Borrower Name"), "fieldtype": "Data", "width": 150},
        {"fieldname": "borrower", "label": ("Borrower Id"), "fieldtype": "Data", "width": 150},
        {"fieldname": "issued_date", "label": ("Issued Date"), "fieldtype": "Date", "width": 100},
        {"fieldname": "return_date", "label": ("Return Date"), "fieldtype": "Date", "width": 100},
    ]

    # Fetch data from the database based on filters
    data = get_data(filters)

    return columns, data

def get_data(filters):
    # Build the query based on the provided filters
    query = """
        SELECT
            book_serial,
            book_name,
            borrower_name,
            borrower,
            issued_date,
            return_date
        FROM
            tabBorrower
    """

    conditions = []

    # Add conditions based on filters
    if filters.get('book_serial'):
        conditions.append(f"book_serial = '{filters['book_serial']}'")

    if filters.get('book_name'):
        conditions.append(f"book_name = '{filters['book_name']}'")

    if filters.get('issued_date'):
        conditions.append(f"issued_date = '{filters['issued_date']}'")

    if filters.get('borrower'):
        conditions.append(f"borrower = '{filters['borrower']}'")

    if filters.get('borrower_name'):
        conditions.append(f"borrower_name = '{filters['borrower_name']}'")

    # Combine conditions with 'AND'
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Execute the query and fetch data as a list of dictionaries
    data = frappe.db.sql(query, as_dict=True)

    return data
