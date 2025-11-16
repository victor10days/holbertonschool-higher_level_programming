from flask import Flask, render_template
import json

# Create Flask application instance
app = Flask(__name__)

@app.route('/items')
def items():
    """Route to display items from JSON file"""
    
    # Open and read the JSON file
    # 'r' mode means read-only
    with open('items.json', 'r') as file:
        # json.load() parses JSON into Python dictionary
        data = json.load(file)
    
    # Pass the 'items' list to the template
    # data['items'] extracts the list from {"items": [...]}
    # Template will receive this as variable named 'items'
    return render_template('items.html', items=data['items'])

if __name__ == '__main__':
    # Run Flask on port 5000 with debug mode
    app.run(debug=True, port=5000)
