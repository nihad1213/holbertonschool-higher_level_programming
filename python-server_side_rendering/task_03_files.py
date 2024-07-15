from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to read JSON file
def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to read CSV file
def read_csv(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            return render_template('product_display.html', error='File not found: products.json')
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            return render_template('product_display.html', error='File not found: products.csv')
    else:
        return render_template('product_display.html', error='Wrong source parameter')

    if id:
        filtered_products = [product for product in products if str(product['id']) == id]
        if not filtered_products:
            return render_template('product_display.html', error=f'Product with id {id} not found')
        return render_template('product_display.html', products=filtered_products)
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
