import ccxt
import os
from dotenv import load_dotenv
import pprint

upbit = ccxt.upbit()

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit.apiKey = os.getenv("UPBIT_ACCESS_KEY")
upbit.secret = os.getenv("UPBIT_SECRET_KEY")

# balance
balance = upbit.fetch_balance()
pprint.pprint(balance)


'''
Reference : https://wikidocs.net/179298
'''