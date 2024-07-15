from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True, port=5000)