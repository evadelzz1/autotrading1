import ccxt
import os
from dotenv import load_dotenv

upbit = ccxt.upbit()
isBuy = False

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit.apiKey = os.getenv("UPBIT_ACCESS_KEY")
upbit.secret = os.getenv("UPBIT_SECRET_KEY")

def get_price(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    return price_close

def watch_and_order(_ticker):
    global isBuy
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    percent = infos['percentage'] * 100
    rounded_percent = round(percent, 2)
    print(f"[{_ticker}] Current Price : {price_close}, Daily fluctuation rate : {rounded_percent}%")
    # print(f"현재 코인의 가격은 {price_close} 원이고, 전일대비 {rounded_percent}% 입니다.")

    if percent < -3 and not isBuy:
        upbit.create_market_order("ALGO/KRW", "buy", 1000, 1)
        isBuy = True

watch_and_order("XRP/KRW")
exit(0)

while True:
    time.sleep(3)
    watch_and_order("XRP/KRW")
    
try:
    # 시장가 주문 : 업비트, 최소 주문금액 5,000원
    upbit.create_market_order("ALGO/KRW", "buy", 1000, 1)   # (종목, buy, 금액, 비용(1))
    upbit.create_market_order("ALGO/KRW", "sell", 5)        # (종목, sell, 금액이 아닌 갯수)

    # 지정가 주문
    upbit.create_limit_order("ALGO/KRW", "buy", 10, 600)    # (종목, buy, 구매 수량, 지정 금액)
    upbit.create_limit_order("ALGO/KRW", "sell", 10, 600)

except Exception as e:
    print(e)


