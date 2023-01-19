import unittest 
from money_live import Dollars, Money

class TestMoney(unittest.TestCase):

    def test_multiplication(self):
        ### FIRST CYCLE OF TDD
        five = Dollars(5)
        tenner = five.times(2)
        #return True if 10 == tenner.amount else False
        self.assertEqual(10, tenner.amount)

    ### SECOND CYCLE OF TDD
    def test_multiplication_in_Euro(self):
        ten_euros = Money(10, 'EUR')
        twenty_euros = ten_euros.times(2)
        self.assertEqual(20, twenty_euros.amount)


unittest.main()