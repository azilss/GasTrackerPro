import requests

def fetch_etherscan_gas():
    url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourEtherscanAPIKey"
    r = requests.get(url).json()
    if r["status"] == "1":
        return int(r["result"]["ProposeGasPrice"])
    return None

def fetch_ethgasstation_gas():
    url = "https://ethgasstation.info/api/ethgasAPI.json"
    r = requests.get(url).json()
    return int(r["fast"] / 10) if "fast" in r else None

def main():
    etherscan_price = fetch_etherscan_gas()
    ethgasstation_price = fetch_ethgasstation_gas()
    prices = [p for p in [etherscan_price, ethgasstation_price] if p]
    if prices:
        average = sum(prices) / len(prices)
        print(f"Average recommended gas price: {average} Gwei")
    else:
        print("Failed to fetch gas prices.")

if __name__ == "__main__":
    main()
