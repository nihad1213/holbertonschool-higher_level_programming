from flask import Flask, render_template, request, jsonify
import json
import csv

app = Flask(__name__)

# Function to read JSON data
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to read CSV data
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        try:
            products = read_json('data/products.json')
        except Exception as e:
            error = f"Error reading JSON file: {e}"
    elif source == 'csv':
        try:
            products = read_csv('data/products.csv')
        except Exception as e:
            error = f"Error reading CSV file: {e}"
    else:
        error = "Wrong source. Please specify either 'json' or 'csv'."

    if not error and product_id is not None:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            error = "Product not found."

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
