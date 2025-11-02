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
