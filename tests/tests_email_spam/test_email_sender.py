import pytest
from pythonlib.email_spam.email_sender import InvalidEmail, Sender


def test_create_email_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize(
    'addresser',
    ['foo@bar.com.br', 'brunocastromoura@hotmail.com']
)
def test_addresser(addresser):
    sender = Sender()
    result = sender.send(
        addresser,
        'amanda@hotmail.com',
        'Assunto',
        'Corpo do email.'
    )
    assert addresser in result


@pytest.mark.parametrize(
    'addresser',
    ['', 'brunocastromoura']
)
def test_addresser_is_invalid(addresser):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            addresser,
            'amanda@hotmail.com',
            'Assunto',
            'Corpo do email.'
        )
