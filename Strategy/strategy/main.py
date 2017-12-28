from strategy.sqlBase import DBSession
import requests
from strategy.CoinQuoteRequest import *
import time
from strategy.DigitalCurrencyExchange import DigitalCurrencyExchange

session = DBSession()


def main():
    vo = DigitalCurrencyExchange()

    while True:
        ltc_btc = CoinQuoteRequest.get_coin_quote_last_price('ltc_btc')

        bch_btc = CoinQuoteRequest.get_coin_quote_last_price('bch_btc')

        ltc_bch = CoinQuoteRequest.get_coin_quote_last_price('ltc_bch')
        print('ltc/btc市场价格: %f' % (ltc_bch))

        vo.isPrice(ltc_bch, bch_btc, ltc_bch)
        time.sleep(3)


if __name__ == '__main__':
    main()
