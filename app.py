import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = {}
        for coin in data:
            prices[coin['name']] = coin['current_price']
        return prices
    else:
        # If error, return empty dict for top 100 (names not known in advance)
        return {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/price')
def get_price():
    return jsonify(fetch_crypto_prices())

if __name__ == '__main__':
    app.run(debug=True)