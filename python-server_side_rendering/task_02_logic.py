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
@app.route('/items', strict_slashes=False)
def items():
    try:
        with open('items.json', 'r') as f:
            items_data = json.load(f)
        items_list = items_data['items']
        return render_template('items.html', items=items_list)
    except FileNotFoundError:
        return "Error: Could not find items.json", 404
    except KeyError:
        return "Error: Missing 'items' key in items.json", 500
    except Exception as e:
        return f"Error: {str(e)}", 50


if __name__ == "__main__":
    app.run(debug=True, port=5000)
