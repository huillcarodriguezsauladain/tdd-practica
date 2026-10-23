import unittest
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    # Ciclo 1: Probamos con numeros comunes que no se dividen ni entre 3 ni entre 5
    def test_numero_normal(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(4), "4")

    # Ciclo 2: Probamos que si el numero se divide entre 3 devuelva 'Fizz'
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")


if __name__ == "__main__":
    unittest.main()
