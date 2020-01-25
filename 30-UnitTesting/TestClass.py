import unittest
import UnitTesting

class TestUppercase(unittest.TestCase):

    def test_singular_word(self):
        str = "Hello"
        result = UnitTesting.to_uppercase(str)
        self.assertEqual(result, "HELLO")

    def test_multiple_words(self):
        str = "Hello there"
        result = UnitTesting.to_uppercase(str)
        self.assertEqual(result, "HELLO THERE")

if __name__ == "__main__":
    unittest.main()