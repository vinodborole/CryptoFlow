import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = {}
        for coin in data:
            prices[coin['name']] = coin['current_price']
        return prices
    else:
        return {coin: "Error fetching price" for coin in [
            "Bitcoin", "Ethereum", "Tether", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano",
            "Avalanche", "TRON", "Chainlink", "Polygon", "Wrapped Bitcoin", "Shiba Inu", "Bitcoin Cash", "NEAR Protocol",
            "Uniswap", "Litecoin", "Polkadot", "LEO Token", "Dai", "Internet Computer", "Kaspa", "Ethereum Classic",
            "Stellar", "Monero", "OKB", "Filecoin", "Cosmos", "Mantle", "Hedera", "Cronos", "Render", "VeChain",
            "Immutable", "Arbitrum", "Optimism", "The Graph", "Algorand", "Theta Network", "Fantom", "Quant",
            "Aave", "Decentraland", "Sandbox", "ApeCoin", "Flow", "Enjin Coin"
        ]}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    return jsonify(fetch_crypto_prices())

if __name__ == '__main__':
    app.run(debug=True)