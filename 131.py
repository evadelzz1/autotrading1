from ConfigUpbit import upbit
import time
from datetime import datetime

isBuy = False

def get_price(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    return price_close

def watch_and_order(_ticker):
    global isBuy
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']            # 종가
    percent = infos['percentage'] * 100     # 전일 대비 변화량
    rounded_percent = round(percent, 2)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] [{_ticker}] Current Price : {price_close}, Daily fluctuation rate : {rounded_percent}%")

    if percent < -3 and not isBuy:
        upbit.create_market_order(_ticker, "buy", 1000, 1)
        isBuy = True 

while True:
    time.sleep(3)
    watch_and_order("XRP/KRW")