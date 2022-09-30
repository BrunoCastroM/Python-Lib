class Sender:
    def send(self, sender, receipts, subject, body):
        if '@' not in sender:
            raise InvalidEmail(f'invalid sender email: {sender}')
        return sender


class InvalidEmail(Exception):
    pass
