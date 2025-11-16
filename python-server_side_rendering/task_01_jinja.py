from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Route for home page - renders index.html"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Route for about page - renders about.html"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Route for contact page - renders contact.html"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
