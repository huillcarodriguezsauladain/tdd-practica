"""
Modulo para validar contrasenas siguiendo TDD paso a paso.
"""


def validar_password(pwd):
    errores = []

    # Ciclo 1: Revisamos que la longitud minima sea de 8 caracteres
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")

    return {
        "valida": len(errores) == 0,
        "errores": errores
    }
