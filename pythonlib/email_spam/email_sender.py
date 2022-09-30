class Sender:
    def send(self, addresser, receipts, subject, body):
        if '@' not in addresser:
            raise InvalidEmail(f'invalid sender email: {addresser}')
        return addresser


class InvalidEmail(Exception):
    pass
