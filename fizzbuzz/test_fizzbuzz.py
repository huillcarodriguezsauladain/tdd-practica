import unittest
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    # Ciclo 1: Probamos con numeros comunes que no se dividen ni entre 3 ni entre 5
    def test_numero_normal(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(4), "4")


if __name__ == "__main__":
    unittest.main()
