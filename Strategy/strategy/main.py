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

        eth_btc = CoinQuoteRequest.get_coin_quote_last_price('eth_btc')

        ltc_eth = CoinQuoteRequest.get_coin_quote_last_price('ltc_eth')
        print('ltc/btc市场价格: %f' % (ltc_eth))

        vo.isPrice(ltc_btc, eth_btc, ltc_eth)
        vo.shortSelling(ltc_btc, eth_btc, ltc_eth)
        
        time.sleep(3)


if __name__ == '__main__':
    main()
