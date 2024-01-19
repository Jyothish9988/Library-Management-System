import frappe

def execute(filters=None):
    # Define columns for the report
    columns = [
        {"fieldname": "book_serial", "label": ("Book ID"), "fieldtype": "Link", "options": "Book", "width": 100},
        {"fieldname": "book_name", "label": ("Book Name"), "fieldtype": "Link", "options": "Book", "width": 150},
        {"fieldname": "issued_date", "label": ("Issued Date"), "fieldtype": "Date", "width": 100},
        # Add more columns as needed
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
            book_serial,
            issued_date
        FROM
            tabTransaction
    """

    conditions = []

    # Add conditions based on filters
    if filters.get('book_serial'):
        conditions.append(f"book_serial = '{filters['book_serial']}'")

    if filters.get('book_name'):
        conditions.append(f"book_name = '{filters['book_name']}'")

    if filters.get('issued_date'):
        conditions.append(f"issued_date = '{filters['issued_date']}'")

    # Combine conditions with 'AND'
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Execute the query and fetch data as a list of dictionaries
    data = frappe.db.sql(query, as_dict=True)

    return data