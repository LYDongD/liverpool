import requests
import json
import requests

class HttpTest(object):

    def testGetRequst(self):
        r = requests.get('http://customer.jinniubaotouzi.com/api/customer/news/finance')
        return r.text

    def jsonHandle(self):
        response_str = self.testGetRequst()
        response_obj = json.loads(response_str)
        print(response_obj)
        print(response_obj['code'])
        print(response_obj['data']['newsList'][0]['title'])



HttpTest().jsonHandle()
