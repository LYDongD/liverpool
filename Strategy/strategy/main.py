from strategy.model.User import User
from strategy.sqlBase import DBSession


session = DBSession()


def main():
    user_id = User.add(session, name='pony3')
    print(User.get(session, user_id=user_id))


if __name__ == '__main__':
    main()
