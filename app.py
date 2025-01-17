from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manage-product')
def manage_product():
    return render_template('manage-product.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)