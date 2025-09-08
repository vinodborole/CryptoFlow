import requests
from flask import Flask, jsonify, render_template

# Define a constant for the number of cryptocurrencies to fetch
CRYPTO_COUNT = 100

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page={CRYPTO_COUNT}&page=1&sparkline=false"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = {}
        for coin in data:
            prices[coin['name']] = coin['current_price']
        return prices
    else:
        return {f"Crypto_{i+1}": "Error fetching price" for i in range(CRYPTO_COUNT)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    return jsonify(fetch_crypto_prices())

if __name__ == '__main__':
    app.run(debug=True)