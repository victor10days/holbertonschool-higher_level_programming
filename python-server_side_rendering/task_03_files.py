from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    """
    Route to display products from different sources (JSON or CSV)
    Query parameters:
        - source: 'json' or 'csv' (required)
        - id: product ID to filter (optional)
    """
    
    source = request.args.get('source') 
    product_id = request.args.get('id')  
    
    products_list = []  
    error = None        
    
    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                products_list = json.load(file)
        except FileNotFoundError:
            error = "JSON file not found"
        except json.JSONDecodeError:
            error = "Invalid JSON format"
    
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as file:
                csv_reader = csv.DictReader(file)
                
                products_list = list(csv_reader)
                
                for product in products_list:
                    product['id'] = int(product['id'])
                    product['price'] = float(product['price'])
        except FileNotFoundError:
            error = "CSV file not found"
        except ValueError as e:
            error = f"Error converting CSV data: {e}"
    
    else:
        error = "Wrong source"
    if product_id and not error:
        try:
            product_id = int(product_id)
            
            filtered_products = [p for p in products_list if p['id'] == product_id]
            
            if filtered_products:
                products_list = filtered_products
            else:
                error = "Product not found"
                products_list = []
        except ValueError:
            error = "Invalid product ID"
            products_list = []
    
    return render_template('product_display.html', 
                        products=products_list, 
                        error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
