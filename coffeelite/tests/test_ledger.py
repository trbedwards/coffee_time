import unittest
from coffeelite.ledger import *

class TestCustomer(unittest.TestCase):
    def test___init__(self):
        customer = Customer(name='Tom', credit=15.50)
        self.test_type_of_attributes(customer)
        self.assertEqual(customer.name, 'Tom')
        self.assertEqual(customer.credit, 15.50)

    def test_type_of_attributes(self,customer=Customer()):
        self.assertEqual(type(customer.name), type(str()))
        self.assertEqual(type(customer.credit), type(float()))

class TestLedger(unittest.TestCase):
    def test___init__(self):
        ledger = Ledger()
        assert True # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()