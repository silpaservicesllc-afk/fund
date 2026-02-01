import os
import requests
import json
from datetime import datetime

# Your 18 symbols
SYMBOLS = ["AMZN", "GOOGL", "META", "V", "MA", "TSM", "BRK-B", "COST", "WMT", "MCO", "SPGI", "UBER", "TPL", "ZETA", "ASTS", "LMND", "UA", "LUMN"]
API_KEY = os.getenv('ALPHA_VANTAGE_KEY')

def fetch_data():
    market_results = {}
    for symbol in SYMBOLS:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url).json()
        
        if "Global Quote" in response and "10. change percent" in response["Global Quote"]:
            # Convert "0.4500%" to "0.45"
            raw_percent = response["Global Quote"]["10. change percent"].replace('%', '')
            market_results[symbol] = str(round(float(raw_percent), 2))
    
    output = {
        "lastUpdated": datetime.utcnow().isoformat() + "Z",
        "data": market_results
    }
    
    with open('market-data.json', 'w') as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    fetch_data()