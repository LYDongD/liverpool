from strategy.sqlBase import DBSession
import strategy.digitalCurrencyExchange
import requests
from strategy.CoinQuoteRequest import *


session = DBSession()


def main():

    while True:

    ltc_btc = CoinQuoteRequest.get_coin_quote_last_price('ltc_btc')
    bch_btc = CoinQuoteRequest.get_coin_quote_last_price('bch_btc')
    ltc_bch = CoinQuoteRequest.get_coin_quote_last_price('ltc_bch')

    strategy.digitalCurrencyExchange.isPrice(ltc_btc, bch_btc, ltc_bch)




if __name__ == '__main__':
    main()




