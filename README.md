# Práctica de TDD (Desarrollo Guiado por Pruebas) - Semana 10

¡Hola! Este repositorio contiene la solución completa de la práctica de la **Semana 10** del curso **Construcción de Software** en la **Universidad Continental**.

Aquí construimos dos programas en Python desde cero usando la técnica **TDD** (Test-Driven Development).

---

## 👨‍💻 Datos del Estudiante y Curso

- **Estudiante:** Saul Adain Huillca Rodriguez
- **Correo Institucional:** 74401464@continental.edu.pe
- **Asignatura:** Construcción de Software
- **Docente:** Ing. Henderson Nozart Gibaja Reyes
- **Semana:** 10 (Unidad 3)

---

## 🤔 ¿Qué es TDD en palabras sencillas?

Normalmente uno se acostumbra a programar primero la lógica y recién al final (si queda tiempo) probar si funciona. 

En **TDD** hacemos exactamente lo contrario: **primero escribimos la prueba y después escribimos el código**. Es como construir una cerradura teniendo ya la llave en la mano.

El método funciona como un semáforo de 3 pasos:

1. 🔴 **Rojo (Red):** Escribimos una prueba para una regla o función que todavía no existe. Al ejecutarla, la prueba **falla obligatoriamente**. Esto nos asegura que la prueba realmente detecta errores.
2. 🟢 **Verde (Green):** Escribimos el código **más simple y directo posible** solo para que la prueba se ponga en verde (pase con éxito). No intentamos hacer código elegante ni meter cosas de más.
3. 🔵 **Refactor (Mejorar):** Con la prueba ya en verde, ordenamos y limpiamos el código para que quede prolijo, asegurándonos de que todas las pruebas sigan pasando.

---

## 📁 Estructura del Proyecto

El proyecto está organizado tal como pide la guía:

```text
tdd-practica/
├── fizzbuzz/
│   ├── __init__.py
│   ├── fizzbuzz.py         # Código de la función fizzbuzz
│   └── test_fizzbuzz.py    # 5 pruebas automáticas (incluye subTest)
├── validador/
│   ├── __init__.py
│   ├── validador.py        # Código del validador de contraseñas
│   └── test_validador.py   # 9 pruebas automáticas (reglas + integral + subTest)
├── .gitignore              # Archivos temporales que no van a Git
└── README.md               # Esta explicación
```

---

## 🛠️ Los dos ejercicios explicados

### 1. Módulo FizzBuzz (`fizzbuzz/`)
Este ejercicio consiste en una función `fizzbuzz(n)` que recibe un número entero y devuelve un texto según estas reglas:
- Si el número se divide entre **3**, devuelve `"Fizz"`.
- Si el número se divide entre **5**, devuelve `"Buzz"`.
- Si se divide entre **ambos (3 y 5)**, devuelve `"FizzBuzz"`.
- Para cualquier otro número normal, devuelve el mismo número en texto (por ejemplo `1` -> `"1"`).

**¿Cómo lo construimos con TDD?**
- **Ciclo 1:** Probamos números comunes (1, 2, 4). Falló (rojo), creamos la función devolviendo `str(n)` y pasó (verde).
- **Ciclo 2:** Agregamos la prueba para el 3, 6, 9. Falló, pusimos la condición del 3 y pasó.
- **Ciclo 3:** Agregamos la prueba para el 5 y 10. Falló, pusimos la condición del 5 y pasó.
- **Ciclo 4:** Agregamos la prueba para el 15 y 30. Fallaba porque entraba primero a la regla del 3, así que pusimos la regla del 15 arriba de todas y pasó.
- **Ciclo 5:** Agregamos una prueba completa con `subTest` para chequear un lote de números (1 al 45) y confirmar que nada se rompa.

---

### 2. Módulo Validador de Contraseñas (`validador/`)
Creamos la función `validar_password(pwd)` para revisar si una contraseña es segura. Devuelve un diccionario con dos datos:
- `"valida"`: `True` si cumple todo, o `False` si falla algo.
- `"errores"`: una lista con los mensajes exactos de lo que faltó corregir.

**Reglas de seguridad que evalúa:**
1. Mínimo 8 caracteres $\rightarrow$ `"Mínimo 8 caracteres"`
2. Al menos una mayúscula $\rightarrow$ `"Al menos una mayúscula"`
3. Al menos una minúscula $\rightarrow$ `"Al menos una minúscula"`
4. Al menos un dígito $\rightarrow$ `"Al menos un dígito"`
5. Al menos un carácter especial (`!@#$%^&*`) $\rightarrow$ `"Al menos un carácter especial"`

**¿Cómo lo construimos con TDD?**
Fuimos regla por regla: primero el test con contraseña que falla esa regla (Rojo), luego agregamos la comprobación mínima (Verde) y repetimos. Al final agregamos pruebas de contraseñas que cumplen todo, contraseñas con varios errores juntos y un `subTest` con varios ejemplos.

---

## 🚀 ¿Cómo ejecutar las pruebas automáticas?

Abre tu terminal en la carpeta `tdd-practica` y escribe cualquiera de estos comandos:

### 1. Correr todas las pruebas del proyecto (14 pruebas en total)
```bash
python -m unittest discover -v
```
*(Si en tu computadora usas el lanzador de Python, también puedes escribir `py -m unittest discover -v`)*.

### 2. Probar solo FizzBuzz
```bash
python -m unittest fizzbuzz/test_fizzbuzz.py -v
```

### 3. Probar solo el Validador de contraseñas
```bash
python -m unittest validador/test_validador.py -v
```

Deberás ver que todas las pruebas muestran `ok` y finalizan con un mensaje `OK`.

---

## 📜 Historial de Commits (Evolución TDD)

La guía solicita un mínimo de 5 commits que evidencien el ciclo paso a paso. En este proyecto realizamos **13 commits** organizados:

1. `estructura inicial del proyeccto y carpetas`
2. `fizzbuzz ciclo 1 numeros normales primero red luego green`
3. `fizzbuzz ciclo 2 regla para fizz en multiplos de 3`
4. `fizzbuzz ciclo 3 agregando buzz para los multiplos de 5`
5. `fizzbuzz ciclo 4 caso fizzbuzz divisible entre 15`
6. `fizzbuzz ciclo 5 refactor y subtest con varios casos`
7. `validador ciclo 1 longitud minima de 8 caracteres red y green`
8. `validador ciclo 2 regla de mayuscula red a green`
9. `validador ciclo 3 validacion de minusculas red a green`
10. `validador ciclo 4 validando q tenga digito o numero`
11. `validador ciclo 5 caracter especial para q pase el test`
12. `validador ciclo 6 refactorizando codigo y prueba completa con subtest`
13. `readme explicando como funciona tdd y como correr los test`

Puedes verificar este historial en cualquier momento con:
```bash
git log --oneline
```
