import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    try:
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
                "Aave", "Decentraland", "Sandbox", "ApeCoin", "Flow", "Enjin Coin", "Maker", "Lido DAO", "Pepe",
                "Sui", "BitTorrent", "Stacks", "Injective", "TrueUSD", "First Digital USD", "Flare", "Pyth Network",
                "JasmyCoin", "Bonk", "dogwifhat", "FLOKI", "Beam", "Worldcoin", "Celestia", "THORChain", "Jupiter",
                "Arweave", "Blur", "MultiversX", "Akash Network", "Axie Infinity", "Helium", "GALA", "Conflux",
                "Mina", "Pendle", "Compound", "Wormhole", "eCash", "Curve DAO Token", "Ondo", "ORDI", "dYdX",
                "Neo", "1inch Network", "Bitcoin SV", "Ronin", "EOS", "IOTA", "Chiliz", "KuCoin Token", "ZKsync",
                "Gnosis", "Ethena USDe", "Aptos", "Lido Staked Ether"
            ]}
    except Exception:
        return {coin: "Error fetching price" for coin in [
            "Bitcoin", "Ethereum", "Tether", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano",
            "Avalanche", "TRON", "Chainlink", "Polygon", "Wrapped Bitcoin", "Shiba Inu", "Bitcoin Cash", "NEAR Protocol",
            "Uniswap", "Litecoin", "Polkadot", "LEO Token", "Dai", "Internet Computer", "Kaspa", "Ethereum Classic",
            "Stellar", "Monero", "OKB", "Filecoin", "Cosmos", "Mantle", "Hedera", "Cronos", "Render", "VeChain",
            "Immutable", "Arbitrum", "Optimism", "The Graph", "Algorand", "Theta Network", "Fantom", "Quant",
            "Aave", "Decentraland", "Sandbox", "ApeCoin", "Flow", "Enjin Coin", "Maker", "Lido DAO", "Pepe",
            "Sui", "BitTorrent", "Stacks", "Injective", "TrueUSD", "First Digital USD", "Flare", "Pyth Network",
            "JasmyCoin", "Bonk", "dogwifhat", "FLOKI", "Beam", "Worldcoin", "Celestia", "THORChain", "Jupiter",
            "Arweave", "Blur", "MultiversX", "Akash Network", "Axie Infinity", "Helium", "GALA", "Conflux",
            "Mina", "Pendle", "Compound", "Wormhole", "eCash", "Curve DAO Token", "Ondo", "ORDI", "dYdX",
            "Neo", "1inch Network", "Bitcoin SV", "Ronin", "EOS", "IOTA", "Chiliz", "KuCoin Token", "ZKsync",
            "Gnosis", "Ethena USDe", "Aptos", "Lido Staked Ether"
        ]}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    return jsonify(fetch_crypto_prices())

if __name__ == '__main__':
    app.run(debug=True)