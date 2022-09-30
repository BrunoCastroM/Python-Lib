from pythonlib.email_spam.db import Connection
from pythonlib.email_spam.models import User


def test_save_user():
    connection = Connection()
    session = connection.generate_session()
    user = User(name='Bruno')
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()
    session.close()
    connection.close()


def test_list_users():
    connection = Connection()
    session = connection.generate_session()
    users = [User(name='Bruno'), User(name='Amanda')]
    for user in users:
        session.save(user)
    assert users == session.list()
    session.roll_back()
    session.close()
    connection.close()
