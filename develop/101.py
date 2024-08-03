import ccxt
from typing import List

def line_delimiter(_line_number: int = 100) -> None:
    print("=" * _line_number)

def get_market_symbol_list(_symbol_list: List[str], _market: str) -> None:
    symbols = [symbol for symbol in _symbol_list if _market in symbol]
    line_delimiter()
    print("### Market : " + _market)
    line_delimiter(30)
    print(symbols)

def get_ticker_info(_ticker_infos):
    line_delimiter(30)
    print(f"# symbol : {_ticker_infos['symbol']}")
    print(f"# close  : {_ticker_infos['close']}")
    print(f"# high   : {_ticker_infos['high']}")
    line_delimiter(30)
    
    print(_ticker_infos)
        
def main() -> None:
    upbit = ccxt.upbit()
    
    upbit.load_markets()
    symbols = upbit.symbols
    print(symbols)
    line_delimiter()

    # symbol list by market
    market_lists = ['KRW', 'BTC', 'USDT']
    for market in market_lists:
        get_market_symbol_list(symbols, market)

    print()
    
    # ticker info
    ticker_lists = ['XRP/KRW', 'ETH/KRW']
    for ticker in ticker_lists:
        ticker_infos = upbit.fetch_ticker(ticker)
        get_ticker_info(ticker_infos)

if __name__ == "__main__":
    main()


# CCXT (CryptoCurrency eXchange Trading Library)
# - 자바스크립트, 파이썬, PHP와 같이 다양한 언어에서 범용적으로 사용할 수 있는 가상화폐 거래소 모듈
# - 업비트, 바이낸스 뿐만 아니라 비트파이넥스 (Bitfinex), 비트렉스 (bittrex), 크라켄 (kraken) 등등
#   125개 거래소의 API를 지원






