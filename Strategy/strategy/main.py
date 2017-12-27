from strategy.model.User import User
from strategy.sqlBase import DBSession
import strategy.digitalCurrencyExchange
import requests

session = DBSession()


def main():
    #user_id = User.add(session, name='pony3')
    #print(User.get(session, user_id=user_id))

    a = 0.18050114
    b = 0.01745870
    c = 0.09723543
    strategy.digitalCurrencyExchange.isPrice(a, b, c)

if __name__ == '__main__':
    main()




