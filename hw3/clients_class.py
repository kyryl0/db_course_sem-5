class Client:

    def __init__(self, first, last, address):
        self.first = first
        self.last = last
        self.address = address

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Client('{}', '{}', {})".format(self.first, self.last, self.address)
