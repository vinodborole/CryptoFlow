import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    # Try to fetch 200 coins at once first
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=200&page=1&sparkline=false"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 200:
                # Successfully got 200 coins in one request
                prices = {}
                for coin in data:
                    prices[coin['name']] = coin['current_price']
                return prices
            else:
                # API might have a lower limit, try multiple requests
                paginated_result = fetch_crypto_prices_paginated()
                if paginated_result:
                    return paginated_result
        else:
            # If single request fails, try paginated approach
            paginated_result = fetch_crypto_prices_paginated()
            if paginated_result:
                return paginated_result
    except:
        # If there's any network/connection error, try paginated approach
        try:
            paginated_result = fetch_crypto_prices_paginated()
            if paginated_result:
                return paginated_result
        except:
            pass  # Fall through to fallback data
    
    # If all approaches fail, return fallback data
    return {coin: "Error fetching price" for coin in [
        "Bitcoin", "Ethereum", "Tether", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano",
        "Avalanche", "TRON", "Chainlink", "Polygon", "Wrapped Bitcoin", "Shiba Inu", "Bitcoin Cash", "NEAR Protocol",
        "Uniswap", "Litecoin", "Polkadot", "LEO Token", "Dai", "Internet Computer", "Kaspa", "Ethereum Classic",
        "Stellar", "Monero", "OKB", "Filecoin", "Cosmos", "Mantle", "Hedera", "Cronos", "Render", "VeChain",
        "Immutable", "Arbitrum", "Optimism", "The Graph", "Algorand", "Theta Network", "Fantom", "Quant",
        "Aave", "Decentraland", "Sandbox", "ApeCoin", "Flow", "Enjin Coin", "Maker", "Lido DAO", "Bitcoin SV",
        "Stacks", "The Sandbox", "Axie Infinity", "Elrond", "Helium", "EOS", "Chiliz", "Theta Fuel", "Mina",
        "Klaytn", "IOTA", "Neo", "Bitcoin Gold", "Zcash", "Waves", "OMG Network", "Loopring", "1inch Network",
        "Sushi", "Compound", "yearn.finance", "Synthetix", "UMA", "Bancor", "0x", "Kyber Network", "Balancer",
        "Curve DAO Token", "Ren", "Storj", "Basic Attention Token", "Golem", "Civic", "Status", "district0x",
        "Numeraire", "Augur", "Gnosis", "TrueUSD", "Paxos Standard", "Gemini Dollar", "USD Coin", "Binance USD",
        "Terra Classic", "Terra", "Anchor Protocol", "Mirror Protocol", "PancakeSwap", "Venus", "Alpaca Finance",
        "Cake Monster", "SafeMoon", "Elongate", "Doge Killer", "Baby Doge Coin", "Pitbull", "Kishu Inu",
        "Akita Inu", "Dogelon Mars", "Hoge Finance", "SafeMars", "Cumrocket", "SpaceMoon", "MoonPirate",
        "SafeGalaxy", "FairSafe", "SafeStar", "EverRise", "Evergrow Coin", "Catgirl", "Floki Inu", "Saitama",
        "Jacy Token", "Luffy Token", "One Piece", "Goku Inu", "Kiba Inu", "Mononoke Inu", "Tsuka",
        "Pepe", "Wojak", "Milady Meme Coin", "Ben", "Turbo", "Bob", "Mog Coin", "Brett", "Andy",
        "Landwolf", "Toshi", "Based", "Degen", "Ponke", "Cat in a dogs world", "Popcat", "Moo Deng",
        "Neiro", "DOGS", "Simon's Cat", "Memes AI", "Goatseus Maximus", "Act I", "Pnut", "Fred",
        "Bonk", "dogwifhat", "Book of Meme", "MAGA", "Jeo Boden", "Daddy Tate", "Based Brett", "Apu Apustaja",
        "Baby Doge Coin", "SafeMoon V2", "Dogelon Mars", "Kishu Inu", "Akita Inu", "Hoge Finance", "SafeMars",
        "Cumrocket", "SpaceMoon", "MoonPirate", "SafeGalaxy", "FairSafe", "SafeStar", "EverRise", "Evergrow Coin",
        "Catgirl", "Floki Inu", "Saitama", "Jacy Token", "Luffy Token", "One Piece", "Goku Inu", "Kiba Inu",
        "Chainlink", "Aave", "Uniswap", "Compound", "Synthetix", "Maker", "yearn.finance", "Curve DAO Token",
        "SushiSwap", "1inch Network", "Balancer", "0x", "Kyber Network", "Bancor", "Loopring", "OMG Network",
        "Polygon", "Arbitrum", "Optimism", "Immutable X", "Starknet", "zkSync", "Metis", "Boba Network",
        "Fantom", "Avalanche", "Harmony", "NEAR Protocol", "Solana", "Cosmos", "Polkadot", "Kusama",
        "Moonbeam", "Moonriver", "Acala", "Karura", "Parallel Finance", "Bifrost", "Centrifuge", "Interlay",
        "Kava", "Secret", "Osmosis", "Injective", "Juno", "Stargaze", "REGEN", "Sentinel", "Persistence", "Comdex",
        "Chihuahua", "Omniflix", "Bitcanna", "Likecoin", "Desmos", "AssetMantle", "FetchAI", "OmniFlix"
    ]}

def fetch_crypto_prices_paginated():
    """Fetch 200 crypto prices using multiple paginated requests (50 per page, 4 pages)"""
    all_prices = {}
    
    for page in range(1, 5):  # Pages 1, 2, 3, 4 to get 200 total (50 each)
        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page={page}&sparkline=false"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for coin in data:
                    all_prices[coin['name']] = coin['current_price']
            else:
                return None  # If any page fails, return None to trigger fallback
        except:
            return None  # If any request fails, return None to trigger fallback
    
    return all_prices if len(all_prices) >= 150 else None  # Return only if we got a reasonable amount

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    return jsonify(fetch_crypto_prices())

if __name__ == '__main__':
    app.run(debug=True)