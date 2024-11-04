import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # ทำให้ได้ผลลัพธ์ตามที่หวัง

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    # subtract the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-10, 3), -13)

    # multiply the following test methods to the TestCalculator class:
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # divide the following test methods to the TestCalculator class:
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # modulo the following test methods to the TestCalculator class:

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    # ทดสอบค่าที่เป็นศูนย์
    def test_modulo_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)


if __name__ == '__main__':
    unittest.main()
