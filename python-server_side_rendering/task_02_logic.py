from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            itemsData = json.load(f)
            items = itemsData.get('items', [])
        return render_template("items.html", items=items)
    except FileNotFoundError:
        return "items.json not found", 404
    except json.JSONDecodeError:
        return "Invalid JSON format in items.json", 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
