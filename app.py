from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')  # Home page (menu)

@app.route('/list')
def list_page():
    return render_template('list.html')  # List page

@app.route('/cart')
def cart():
    return render_template('cart.html')  # Cart page

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')  # Checkout page

if _name_ == '_main_':
  app.run(host='0.0.0.0', port=5000, debug=True)
