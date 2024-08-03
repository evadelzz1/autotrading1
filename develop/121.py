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

upbit.load_markets()
symbols = upbit.symbols
# symbols = ["BTC/KRW", "ETH/KRW"], "XRP/KRW"]

mySymbols = ["BTC/KRW", "ETH/KRW", "XRP/KRW"]

for symbol in symbols:
    if not symbol in mySymbols:
        continue

    float_value = float(get_price(symbol))
    # price = format(float_value, "0<10.10f")
    price = f"{float_value: >20.10f}"  # 왼쪽 공백을 포함하여 20자리, 소수점 이하 10자리
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Closed Price : {price} - {symbol}")
    
