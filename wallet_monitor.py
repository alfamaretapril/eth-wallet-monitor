import requests
import time

ETHERSCAN_API = "https://api.etherscan.io/api"
WALLET_ADDRESS = "0x000000000000000000000000000000000000dEaD"
REFRESH_INTERVAL = 10  # in seconds

def get_eth_balance(address):
    url = f"{ETHERSCAN_API}?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken"
    response = requests.get(url).json()
    if response["status"] == "1":
        return int(response["result"]) / 1e18
    return None

def get_gas_price():
    url = f"{ETHERSCAN_API}?module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
    response = requests.get(url).json()
    if response["status"] == "1":
        return response["result"]["ProposeGasPrice"]
    return None

def main():
    while True:
        balance = get_eth_balance(WALLET_ADDRESS)
        gas_price = get_gas_price()
        print(f"Balance: {balance:.6f} ETH | Gas Price: {gas_price} Gwei")
        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
