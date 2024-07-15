from flask import Flask, render_template
import json
app = Flask(__name__)

# Route for index.html file
@app.route('/')
def index():
    return render_template("index.html")

# Route for about.html file
@app.route('/about')
def about():
    return render_template("about.html")

# Route for contact.html file
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Route for items.html file
@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        itemsData = json.load(f)
    return render_template("items.html", items=itemsData['items'])

if __name__ == "__main__":
    app.run(debug=True, port=5000)