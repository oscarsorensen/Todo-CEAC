# UNIT 001 — Identification of Program Elements (Identificación de los elementos de un programa informático)
# Keywords: (variables, operadores, entrada/salida, tipos de datos, funciones, módulos)

"""
SUMMARY:
In Python, a program is made up of variables, operators, data types, input/output operations, 
and modular structures like functions or imports.
"""

# VARIABLES (variables)
age = 25
name = "Oscar"
height = 1.82

# OPERATORS (operadores)
bmi = age / height
print("BMI sample:", bmi)

# INPUT / OUTPUT (entrada / salida)
# Always returns a string, so convert if needed
user_name = input("Enter your name: ")
print("Hello", user_name)

# DATA TYPES (tipos de datos)
integer = 10
decimal = 3.14
text = "hello"
boolean = True

print(type(integer), type(decimal), type(text), type(boolean))

# MODULES AND IMPORTS (módulos)
import math
print("Square root of 16 is", math.sqrt(16))

# EXAM FOCUS
# - Differentiate between int, float, str, and bool
# - Use input() and print()
# - Import a module and use one function from it
