#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_get_day_of_week(self):
        self.assertEqual("Invalid number", get_day_of_week(0))
        self.assertEqual("Monday", get_day_of_week(1))
        self.assertEqual("Tuesday", get_day_of_week(2))
        self.assertEqual("Wednesday", get_day_of_week(3))
        self.assertEqual("Invalid number", get_day_of_week(8))
