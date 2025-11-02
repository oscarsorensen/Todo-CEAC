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
