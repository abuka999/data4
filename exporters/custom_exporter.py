from prometheus_client import start_http_server, Gauge
import requests
import time

# --- Настройки ---
UPDATE_INTERVAL = 20  # секунд
PORT = 9200           # порт, где будет работать экспортер
CRYPTO_LIST = ["bitcoin", "ethereum", "solana", "bnb", "dogecoin", "cardano", "ripple", "avalanche-2", "polkadot", "sui"]

# --- Метрики ---
price_usd = Gauge('crypto_price_usd', 'Current price in USD', ['symbol'])
market_cap = Gauge('crypto_market_cap_usd', 'Market capitalization in USD', ['symbol'])
volume_24h = Gauge('crypto_volume_24h_usd', '24h trading volume in USD', ['symbol'])
price_change_24h = Gauge('crypto_price_change_24h_percent', 'Price change in 24h (%)', ['symbol'])

def fetch_crypto_data():
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ",".join(CRYPTO_LIST),
        "price_change_percentage": "24h"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        for coin in data:
            symbol = coin["symbol"].upper()
            price_usd.labels(symbol=symbol).set(coin["current_price"])
            market_cap.labels(symbol=symbol).set(coin["market_cap"])
            volume_24h.labels(symbol=symbol).set(coin["total_volume"])
            price_change_24h.labels(symbol=symbol).set(coin["price_change_percentage_24h"])
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    print(f"🚀 Starting Crypto Exporter on port {PORT}...")
    start_http_server(PORT)
    while True:
        fetch_crypto_data()
        time.sleep(UPDATE_INTERVAL)
