from flask import Flask, render_template
import json
app = Flask(__name__)

# Route for items.html file
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            itemsData = json.load(f)
        items_list = itemsData.get('items', [])  # Use .get() to avoid KeyError
        return render_template("items.html", items=items_list)
    except FileNotFoundError:
        return "Error: items.json not found", 404
    except json.JSONDecodeError:
        return "Error: items.json is not valid JSON", 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)