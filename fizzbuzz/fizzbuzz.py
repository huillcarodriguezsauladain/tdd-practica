"""
Modulo FizzBuzz desarrollado con TDD (Desarrollo Guiado por Pruebas).
"""


def fizzbuzz(n):
    # Ciclo 2: Si el numero se divide entre 3, devolvemos "Fizz"
    if n % 3 == 0:
        return "Fizz"
    # Ciclo 1: Si no, devolvemos el numero en texto
    return str(n)
