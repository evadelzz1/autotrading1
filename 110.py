import ccxt
import time
from datetime import datetime

upbit = ccxt.upbit()

def get_price(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    return price_close

# def get_price_for_test(_ticker):
#     infos = upbit.fetch_ticker(_ticker)
#     line_delimiter()
#     print(infos)
# 
#     line_delimiter()
#     print(f"# symbol : {infos['symbol']}")
#     print(f"# close  : {infos['close']}")
#     print(f"# high   : {infos['high']}")
# 
# def line_delimiter():
#     print("*" * 100)
    
while True:
    time.sleep(3)

    ticker_lists = ['XRP/KRW']
    for ticker in ticker_lists:
        price = get_price(ticker)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] {ticker} Price: {price}")
