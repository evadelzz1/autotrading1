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

class MyUpbit():
    def __init__(self, _upbit):
        print('### Create a MyUpbit Object ###')
        self.upbit = _upbit
        self.isBuy = False
        
    def get_price(self, _ticker):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']
        return price_close

    def watch_and_order(self, _ticker, _orderAmount):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']            # 종가
        percent = infos['percentage'] * 100     # 전일 대비 변화량
        rounded_percent = round(percent, 6)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] [{_ticker}] Current Price : {price_close}, Daily fluctuation rate : {rounded_percent}%")

        if percent < -3 and not isBuy:
            self.upbit.create_market_order(_ticker, "buy", _orderAmount, 1)
            self.isBuy = True

myupbit = MyUpbit(upbit)

while True:
    # print(myupbit.get_price("XRP/KRW"))
    myupbit.watch_and_order("XRP/KRW", 10000)
    time.sleep(3)
