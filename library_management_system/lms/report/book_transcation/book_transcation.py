# Copyright (c) 2024, Jyothish and contributors
# For license information, please see license.txt
import frappe
from frappe import _

def execute(filters=None):
    

def get_data(filters):
    # Example query to fetch data from your table
    query = """
        SELECT
            book_serial,
            book_name,
            borrower,
            borrower_name,
            b_status,
            issued_date,
            return_date
        FROM
            Borrower
        WHERE
            issued_date BETWEEN %s AND %s
    """

    # Execute the query with the provided date range
    data = frappe.db.sql(query, (filters.get("from_date"), filters.get("to_date")), as_dict=True)

    return data
