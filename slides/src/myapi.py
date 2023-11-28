# Create an api in python that takes in customer information and returns a prediction of their lifetime value.
# Input: Customer Name, Customer Email, Stock Symbol, Purchase Price, Purchase Date
# Output: Predicted Lifetime Value

# Path: slides/src/myapi.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract information from the request
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    stock_symbol = data.get('stock_symbol')
    purchase_price = data.get('purchase_price')
    purchase_date = data.get('purchase_date')

    # TODO: Add your prediction logic here
    # For now, we'll just return a dummy value
    predicted_lifetime_value = caculate_new_value(purchase_price, purchase_date)

    return jsonify({
        'name': name,
        'email': email,
        'stock_symbol': stock_symbol,
        'purchase_price': purchase_price,
        'purchase_date': purchase_date,
        'predicted_lifetime_value': predicted_lifetime_value
    })

def caculate_new_value(purchase_price, purchase_date):
    current_price = 100
    return purchase_price - current_price

if __name__ == '__main__':
    app.run(debug=True)


