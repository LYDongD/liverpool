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
<<<<<<< HEAD
=======
        print('ltc/btc价格: %f' % (ltc_btc))
>>>>>>> ec3743176431c1dd7c3d2b4197f4bee5304320e6

        bch_btc = CoinQuoteRequest.get_coin_quote_last_price('bch_btc')

        ltc_bch = CoinQuoteRequest.get_coin_quote_last_price('ltc_bch')
        print('ltc/btc市场价格: %f' % (ltc_bch))

<<<<<<< HEAD
        vo = DigitalCurrencyExchange()
        vo.isPrice(ltc_btc, bch_btc, ltc_bch)
=======
        vo.isPrice(ltc_bch, bch_btc, ltc_bch)
>>>>>>> ec3743176431c1dd7c3d2b4197f4bee5304320e6
        time.sleep(3)


if __name__ == '__main__':
    main()
