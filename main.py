from ConfigUpbit import upbit
from Class import UpbitBot
from datetime import datetime
import time

def line_delimiter(_line_number=100):
    print("=" * _line_number)

def get_myAsset(_myUpbitBot):
    line_delimiter()
    print("####### My Assets #######")
    line_delimiter(50)
    _myUpbitBot.get_balances()
    line_delimiter()
    

myUpbitBot = UpbitBot(upbit)
get_myAsset(myUpbitBot)

ticker = "BTT/KRW"
print(f"Ticker : {ticker}")

sleepTime = 3

while True:
    try:
        price = myUpbitBot.get_price(ticker)

        price_close, rounded_percent, nowDate = myUpbitBot.get_price2(ticker)
        print(f"[{nowDate}] [{ticker}] Current Price : {price_close:15.6f}, Daily fluctuation rate : {rounded_percent:10.6f}%")
        
        # myUpbitBot.watch_and_order("buy", "BTT/KRW", 10000, 3.6)    # watch_and_order(_orderType, _ticker, _orderAmount, _watch_percent):
        # myUpbitBot.sell_market_price("BTT/KRW", 8900000)            # sell_market_price(_ticker, _orderCount):

    except Exception as e:
        print(e)
        exit(1)

    time.sleep(sleepTime)
