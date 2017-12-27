import requests
import json


class CoinQuoteRequest(object):

    @staticmethod
    def get_coin_quote_last_price(symbol):
        r = requests.get('http://localhost:20000/api/customer/quote/coins')
        response_dic = r.json()
        data_str = response_dic['data'][symbol]
        data_obj = json.loads(data_str)
        return data_obj['ticker']['last']









