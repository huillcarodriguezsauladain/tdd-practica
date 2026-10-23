"""
Modulo para validar contrasenas siguiendo TDD paso a paso.
"""


def validar_password(pwd):
    errores = []

    # Ciclo 1: Revisamos que la longitud minima sea de 8 caracteres
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")

    # Ciclo 2: Revisamos que contenga al menos una letra mayuscula
    if not any(c.isupper() for c in pwd):
        errores.append("Al menos una mayúscula")

    # Ciclo 3: Revisamos que contenga al menos una letra minuscula
    if not any(c.islower() for c in pwd):
        errores.append("Al menos una minúscula")

    # Ciclo 4: Revisamos que contenga al menos un numero o digito
    if not any(c.isdigit() for c in pwd):
        errores.append("Al menos un dígito")

    return {
        "valida": len(errores) == 0,
        "errores": errores
    }
