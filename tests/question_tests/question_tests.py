#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import get_bonus_pay_amount

class Test_Config(unittest.TestCase):

    def test_get_bonus_pay_amount(self):
        self.assertEqual("Invalid arguments", get_bonus_pay_amount(-1))
        self.assertEqual(10, get_bonus_pay_amount(200))
        self.assertEqual(36, get_bonus_pay_amount(600))
        self.assertEqual(70, get_bonus_pay_amount(1000))
        self.assertEqual(120, get_bonus_pay_amount(1500))
        self.assertEqual("Invalid arguments", get_bonus_pay_amount(2000))
