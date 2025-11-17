#!/usr/bin/python3
"""Flask app to display products from JSON, CSV, or SQLite."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

# Create Flask application instance
app = Flask(__name__)


def read_products_from_json():
    """
    Read products from products.json and return a list of dicts.
    
    Returns:
        list: List of product dictionaries
    """
    try:
        with open('products.json', 'r') as f:
            # json.load() parses JSON file into Python list
            data = json.load(f)
        return data  # Expecting a list directly
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def read_products_from_csv():
    """
    Read products from products.csv and return a list of dicts.
    
    Returns:
        list: List of product dictionaries with proper types
    """
    products = []
    try:
        with open('products.csv', 'r', newline='') as f:
            # csv.DictReader reads each row as a dictionary
            # First row (headers) becomes the keys
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to proper types
                # CSV reads everything as strings by default
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except FileNotFoundError:
        return []
    except (ValueError, KeyError):
        return []
    
    return products


def read_products_from_sql(product_id=None):
    """
    Read products from the SQLite database (products.db).
    
    Args:
        product_id (int, optional): If provided, filter by this ID
    
    Returns:
        list: List of product dictionaries
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    try:
        if product_id is None:
            # No filter - get all products
            cursor.execute(
                "SELECT id, name, category, price FROM Products"
            )
        else:
            # Filter by specific ID using parameterized query
            # The ? placeholder prevents SQL injection
            # (product_id,) is a tuple - required for parameter substitution
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,)
            )
        
        # Fetch all matching rows
        rows = cursor.fetchall()
        
        # Convert rows to list of dictionaries to match JSON/CSV format
        products = []
        for row in rows:
            products.append({
                "id": row[0],       # First column: id
                "name": row[1],     # Second column: name
                "category": row[2], # Third column: category
                "price": row[3]     # Fourth column: price
            })
        
        return products
    
    finally:
        # Always close the connection, even if errors occur
        conn.close()


@app.route('/products')
def products():
    """
    Display products from JSON, CSV, or SQLite based on ?source= parameter.
    
    Query Parameters:
        source (str): Data source - 'json', 'csv', or 'sql'
        id (int, optional): Product ID to filter by
    
    Returns:
        Rendered product_display.html template with products or error message
    """
    # Get query parameters from URL
    # Example: /products?source=json&id=1
    source = request.args.get('source', default='', type=str).lower()
    product_id = request.args.get('id', type=int)
    
    # Initialize variables for template
    error = None
    products_list = []
    
    # Branch 1: JSON source
    if source == 'json':
        # Load all products from JSON file
        products_list = read_products_from_json()
        
        # Filter by ID if provided
        if product_id is not None:
            # List comprehension: keep only products matching the ID
            products_list = [p for p in products_list if p.get('id') == product_id]
            
            # If no products match, set error message
            if not products_list:
                error = "Product not found"
    
    # Branch 2: CSV source
    elif source == 'csv':
        # Load all products from CSV file
        products_list = read_products_from_csv()
        
        # Filter by ID if provided
        if product_id is not None:
            products_list = [p for p in products_list if p.get('id') == product_id]
            
            if not products_list:
                error = "Product not found"
    
    # Branch 3: SQL source (NEW in Task 4)
    elif source == 'sql':
        try:
            # read_products_from_sql handles filtering internally
            # If product_id is None, it returns all products
            # If product_id is provided, it returns only matching products
            products_list = read_products_from_sql(product_id)
            
            # Check if we asked for specific ID but got nothing
            if product_id is not None and not products_list:
                error = "Product not found"
        
        except sqlite3.Error:
            # Catch any SQLite-related errors (missing file, table, etc.)
            error = "Database error"
    
    # Branch 4: Invalid source
    else:
        # Source is not 'json', 'csv', or 'sql'
        error = "Wrong source"
    
    # Render the template with products and/or error message
    # Template decides what to display based on these values
    return render_template(
        'product_display.html',
        products=products_list,
        error=error
    )


if __name__ == '__main__':
    # Run the Flask application
    # debug=True: Shows detailed errors and auto-reloads on code changes
    # port=5000: Application runs on http://localhost:5000
    app.run(debug=True, port=5000)
