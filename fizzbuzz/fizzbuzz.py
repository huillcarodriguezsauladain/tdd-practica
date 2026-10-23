"""
Modulo FizzBuzz desarrollado con TDD (Desarrollo Guiado por Pruebas).
"""


def fizzbuzz(n):
    # Ciclo 2: Si el numero se divide entre 3, devolvemos "Fizz"
    if n % 3 == 0:
        return "Fizz"
    # Ciclo 3: Si el numero se divide entre 5, devolvemos "Buzz"
    if n % 5 == 0:
        return "Buzz"
    # Ciclo 1: Si no, devolvemos el numero en texto
    return str(n)
