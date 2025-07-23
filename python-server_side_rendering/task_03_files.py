from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    data = []
    error = None

    try:
        if source == 'json':
            with open('products.json') as f:
                data = json.load(f)
        elif source == 'csv':
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                data = list(reader)
        else:
            error = 'Wrong source'

        if id:
            data = [item for item in data if str(item['id']) == id or str(item.get('id')) == id]
            if not data:
                error = 'Product not found'
    except Exception as e:
        error = str(e)

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)