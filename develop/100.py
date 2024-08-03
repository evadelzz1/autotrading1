import ccxt

upbit = ccxt.upbit()

def line_delimiter():
    print("*" * 100)

def line_delimiter(_line_number=100):
    print("=" * _line_number)

upbit.load_markets()
line_delimiter()

print(upbit.symbols)
line_delimiter()

infos = upbit.fetch_ticker("XRP/KRW")

print(f"# symbol : {infos['symbol']}")
print(f"# close  : {infos['close']}")
print(f"# high   : {infos['high']}")
line_delimiter()

print(infos)
line_delimiter()


# CCXT (CryptoCurrency eXchange Trading Library)
# - 자바스크립트, 파이썬, PHP와 같이 다양한 언어에서 범용적으로 사용할 수 있는 가상화폐 거래소 모듈
# - 업비트, 바이낸스 뿐만 아니라 비트파이넥스 (Bitfinex), 비트렉스 (bittrex), 크라켄 (kraken) 등등
#   125개 거래소의 API를 지원
