import unittest
from validador.validador import validar_password


class TestValidarPassword(unittest.TestCase):
    # Ciclo 1: Revisamos que la contrasena tenga por lo menos 8 caracteres
    def test_password_muy_corta(self):
        res = validar_password("Abc1!")
        self.assertFalse(res["valida"])
        self.assertIn("Mínimo 8 caracteres", res["errores"])

    def test_password_longitud_ok(self):
        res = validar_password("Abcdefg1!")
        # Verificamos que con 8 o mas caracteres no arroje error de longitud
        self.assertNotIn("Mínimo 8 caracteres", res["errores"])

    # Ciclo 2: Revisamos que tenga al menos una letra mayuscula
    def test_sin_mayuscula(self):
        res = validar_password("abcdefg1!")
        self.assertFalse(res["valida"])
        self.assertIn("Al menos una mayúscula", res["errores"])

    # Ciclo 3: Revisamos que tenga al menos una letra minuscula
    def test_sin_minuscula(self):
        res = validar_password("ABCDEFG1!")
        self.assertFalse(res["valida"])
        self.assertIn("Al menos una minúscula", res["errores"])

    # Ciclo 4: Revisamos que tenga al menos un digito o numero
    def test_sin_digito(self):
        res = validar_password("Abcdefgh!")
        self.assertFalse(res["valida"])
        self.assertIn("Al menos un dígito", res["errores"])

    # Ciclo 5: Revisamos que tenga al menos un caracter especial (!@#$%^&*)
    def test_sin_caracter_especial(self):
        res = validar_password("Abcdefg12")
        self.assertFalse(res["valida"])
        self.assertIn("Al menos un carácter especial", res["errores"])

    # Ciclo 6: Refactor y pruebas integrales
    def test_password_valida_completa(self):
        # Probamos una contrasena que cumple todas las reglas
        res = validar_password("Segura1!abc")
        self.assertTrue(res["valida"])
        self.assertEqual(res["errores"], [])

    def test_multiples_errores(self):
        # Probamos una contrasena con varios fallos a la vez
        res = validar_password("abc")
        self.assertFalse(res["valida"])
        self.assertTrue(len(res["errores"]) >= 3)

    def test_varios_passwords_con_subTest(self):
        # Probamos varios ejemplos en bucle con subTest
        casos = [
            ("Abc1!xyz", True),
            ("abc", False),
            ("ABCDEFGH", False),
            ("Abcdefgh1!", True),
        ]
        for pwd, esperado in casos:
            with self.subTest(pwd=pwd):
                res = validar_password(pwd)
                self.assertEqual(res["valida"], esperado)


if __name__ == "__main__":
    unittest.main()
