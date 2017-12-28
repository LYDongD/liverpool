from strategy.sqlBase import DBSession
import strategy.DigitalCurrencyExchange
import requests
from strategy.CoinQuoteRequest import *
import time

session = DBSession()


def main():
    while True:
        ltc_btc = CoinQuoteRequest.get_coin_quote_last_price('ltc_btc')
        print('ltc/btc价格: %f' % (ltc_btc))

        bch_btc = CoinQuoteRequest.get_coin_quote_last_price('bch_btc')
        print('bch_btc价格: %f' % (bch_btc))

        ltc_bch = CoinQuoteRequest.get_coin_quote_last_price('ltc_bch')
        print('ltc/btc价格: %f' % (ltc_bch))

        strategy.DigitalCurrencyExchange.isPrice(ltc_btc, bch_btc, ltc_bch)

        time.sleep(3)


if __name__ == '__main__':
    main()
