#!/usr/bin/python3
"""Script to create and populate the SQLite database for Task 4."""
import sqlite3

def create_database():
    """
    Creates products.db with a Products table and sample data.
    Run this script once before running task_04_db.py.
    """
    # Connect to database file (creates it if doesn't exist)
    conn = sqlite3.connect('products.db')
    
    # Create cursor object to execute SQL commands
    cursor = conn.cursor()
    
    # Create Products table if it doesn't already exist
    # Structure:
    #   - id: INTEGER PRIMARY KEY (unique identifier)
    #   - name: TEXT NOT NULL (product name, required)
    #   - category: TEXT NOT NULL (product category, required)
    #   - price: REAL NOT NULL (product price as decimal, required)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Clear existing data to avoid duplicates when re-running this script
    cursor.execute('DELETE FROM Products')
    
    # Insert sample product data
    # These match the data in products.json and products.csv
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    # Commit changes to save them to the database file
    conn.commit()
    
    # Close the database connection
    conn.close()
    
    print("✓ Database created successfully!")
    print("✓ File: products.db")
    print("✓ Table: Products")
    print("✓ Rows inserted: 2")

if __name__ == '__main__':
    create_database()
