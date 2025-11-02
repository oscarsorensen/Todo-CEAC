# COMBINED NOTES — Units 001–005

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


# UNIT 002 — Use of Objects (Utilización de objetos)
# Keywords: (objetos, métodos, propiedades, mutabilidad, listas, diccionarios)

"""
SUMMARY:
Everything in Python is an object. Objects have properties (attributes) and methods (functions that belong to the object).
This unit focuses on working with built-in objects like strings, lists, tuples, and dictionaries.
"""

# STRINGS (cadenas)
text = "Hello World"
print(text.upper())  # (método)
print(text.replace("World", "Oscar"))

# LISTS (listas)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add new item
print(fruits[0], len(fruits))

# DICTIONARIES (diccionarios)
person = {"name": "Oscar", "age": 25}
print(person["name"], person.get("age"))
person["city"] = "Valencia"

# MUTABILITY (mutabilidad)
numbers = [1, 2, 3]
numbers[0] = 100  # Lists are mutable
print(numbers)

tuple_data = (1, 2, 3)
# tuple_data[0] = 100  # Error: tuples are immutable

# OBJECT METHODS (métodos)
print(fruits.pop())
print(person.keys())

# EXAM FOCUS
# - Know list, tuple, and dictionary syntax
# - Understand mutability vs immutability
# - Demonstrate use of object methods like .append(), .get(), .replace()


# UNIT 003 — Use of Control Structures (Uso de estructuras de control)
# Keywords: (estructuras de control, condicionales, bucles, operadores lógicos)

"""
SUMMARY:
Control structures guide the flow of execution. Python uses indentation for blocks.
Key elements: if/elif/else, for loops, while loops, and logical operators.
"""

# CONDITIONALS (condicionales)
age = 20
if age >= 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

# FOR LOOP (bucle for)
for i in range(3):
    print("Iteration", i)

# WHILE LOOP (bucle while)
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# LOGICAL OPERATORS (operadores lógicos)
x, y = 5, 10
if x < y and y < 20:
    print("x is smaller, y is reasonable")

# CONTROL KEYWORDS (break, continue, pass)
for i in range(5):
    if i == 3:
        continue  # Skip 3
    if i == 4:
        break
    print(i)

# EXAM FOCUS
# - Know if/elif/else, while, for
# - Use range() and increment logic
# - Include logical operators correctly


# UNIT 004 — Class Development (Desarrollo de clases)
# Keywords: (clases, objetos, métodos, propiedades, constructor, CRUD)

"""
SUMMARY:
Classes group data (attributes) and behavior (methods). You can create multiple instances (objects) from one class.
"""

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print(f"Client: {self.name} — Email: {self.email}")

clients = []  # list to store Client objects

def insert_client():
    name = input("Name: ")
    email = input("Email: ")
    clients.append(Client(name, email))
    print("Inserted.")

def list_clients():
    for i, c in enumerate(clients, start=1):
        print(i, c.name, c.email)

# Simple CRUD menu
while True:
    print("\n1) Insert  2) List  3) Exit")
    op = input("> ")
    if op == "1": insert_client()
    elif op == "2": list_clients()
    elif op == "3": break
    else: print("Invalid option")

# EXAM FOCUS
# - Correct class syntax with __init__ and self
# - Build a list of objects and loop over them
# - Menu-driven CRUD application


# UNIT 005 (HTML content shown separately)
