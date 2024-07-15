from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def show_items():
    with open('items.json', 'r') as f:
        items_data = json.load(f)
    
    items = items_data['items']
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
