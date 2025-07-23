from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    data = []
    error = None

    try:
        if source == 'sql':
            conn = sqlite3.connect('products.db')
            c = conn.cursor()
            
            if id:
                c.execute('SELECT * FROM Products WHERE id = ?', (id,))
                row = c.fetchone()
                if row:
                    data = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}]
                else:
                    error = 'Product not found'
            else:
                c.execute('SELECT * FROM Products')
                rows = c.fetchall()
                data = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
            
            conn.close()
        else:
            error = 'Wrong source'
    except Exception as e:
        error = str(e)

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)