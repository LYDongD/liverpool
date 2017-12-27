from strategy.sqlBase import DBSession
from strategy.CoinQuoteRequest import *

session = DBSession()


def main():
    price = CoinQuoteRequest.get_coin_quote_last_price('ltc_btc')
    print(price)


if __name__ == '__main__':
    main()
