import ccxt
import os
from dotenv import load_dotenv
import time
from datetime import datetime

upbit = ccxt.upbit()

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit.apiKey = os.getenv("UPBIT_ACCESS_KEY")
upbit.secret = os.getenv("UPBIT_SECRET_KEY")

# Fetch balances and display them
def get_balances():
    try:
        balance = upbit.fetch_balance()
        for asset, details in balance['total'].items():
            if details > 0:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{now}] {asset}: {details}")
    except Exception as e:
        print(f"Error fetching balance: {e}")

if __name__ == "__main__":
    # upbit.fetch_balance()
    get_balances()


'''
Reference : https://wikidocs.net/179298
'''