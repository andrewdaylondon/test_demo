import unittest
import calculator as calculator


class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_numbers(self):
        result = calculator.calc_add(-10, -20)
        self.assertEqual(result, -30)


class TestsCalculator2(unittest.TestCase):
    def test_add_functionality2(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_numbers2(self):
        result = calculator.calc_add(-10, -20)
        self.assertEqual(result, -30)

if __name__ == '__main__':
    unittest.main()


# pip install pytest   