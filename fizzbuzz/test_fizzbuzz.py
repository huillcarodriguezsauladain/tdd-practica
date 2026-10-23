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

    # Ciclo 3: Probamos que si el numero se divide entre 5 devuelva 'Buzz'
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    # Ciclo 4: Probamos que si el numero se divide entre 3 y entre 5 devuelva 'FizzBuzz'
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
