class Dollars:
    
    def __init__(self, value):
        self.amount = value

    def times(self, num):
        return Dollars(num * self.amount)

    def __repr__(self):
        return self.amount

class Money:

    def __init__(self, value, currency):
        self.amount = value
        self.currency = currency

    def times(self, num):
        return Money(num * self.amount, 'EUR')

    def __repr__(self):
        return self.amount