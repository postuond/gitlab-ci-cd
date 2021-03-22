from unittest import TestCase
from src.divide-multiply-app import divide, multiply

class TestFunctions(TestCase):
    def test_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)
    
    def test_divide_error_on_zero(self):
        with self.assertRaises(ValueError):
            divide(25, 0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertAlmostEqual(multiply(expected), expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertAlmostEqual(multiply(expected), expected)

    def test_multiply_result(self):
        inputs = (3, 5)
        expected = 15
        self.assertAlmostEqual(multiply(*inputs), expected)

    def test_muliply_result_with_zero(self):
        inputs = (3, 5, 0)
        expected = 0
        self.assertAlmostEqual(multiply(*inputs), expected)

    def test_muliply_negative(self):
        inputs = (3, -5, 2)
        expected = -30
        self.assertAlmostEqual(multiply(*inputs), expected)

    def test_mulitply_float(self):
        inputs = (3.0, 2)
        expected = 6.0
        self.assertAlmostEqual(multiply(*inputs), expected)
