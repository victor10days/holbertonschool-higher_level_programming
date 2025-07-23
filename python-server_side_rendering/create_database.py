import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL)''')
    c.execute('DELETE FROM Products')
    c.executemany('INSERT INTO Products VALUES (?, ?, ?, ?)', [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ])
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()