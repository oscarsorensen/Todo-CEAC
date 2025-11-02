# ==========================================
# UNIT 003 — Uso de estructuras de control (Use of Control Structures)
# Keywords: (condicionales, bucles, if, while, for, operadores lógicos, break, continue, pass)
# ==========================================

# Control structures determine which parts of the program execute and when.


# ---------- 1) CONDITIONALS (condicionales if/elif/else) ----------
# Used to execute different code depending on conditions.

score = 78
if score >= 90:
    grade = "A"                       # Block 1 executes if condition is True
elif score >= 70:
    grade = "B"                       # Block 2 executes if previous failed but this True
else:
    grade = "C"                       # If all fail, execute this block
print("Grade:", grade)


# ---------- 2) FOR LOOP (bucle for) ----------
# A for-loop repeats a block of code for each value in a sequence.
# range(start, stop) produces numbers from start to stop-1.

for i in range(1, 6):                 # i takes values 1,2,3,4,5
    print("Iteration:", i)            # Executed once per loop
# When range runs out, the loop ends automatically.


# ---------- 3) WHILE LOOP (bucle while) ----------
# A while-loop repeats as long as a condition remains True.

count = 0
while count < 3:
    print("Count:", count)
    count += 1                        # Must update variable to avoid infinite loop


# ---------- 4) BREAK, CONTINUE, PASS ----------
# These modify loop behavior.
for n in range(6):
    if n == 2:
        continue                      # Skip this iteration and continue with next
    if n == 4:
        break                         # Exit the loop entirely
    if n == 5:
        pass                          # Placeholder (does nothing)
    print("n =", n)
print("Loop finished")


# ---------- 5) LOGICAL OPERATORS (operadores lógicos) ----------
x, y, z = 5, 10, 20
if x < y and y < z:                   # Both conditions must be True
    print("Values increasing")
if x < y or y > z:                    # At least one True
    print("At least one condition True")
if not (x > y):                       # not reverses result
    print("x is not greater than y")


# ---------- 6) INPUT VALIDATION WITH LOOP ----------
# Program repeats until user gives valid number.
while True:
    entry = input("Enter a number 1–5: ")
    try:
        num = int(entry)
        if 1 <= num <= 5:
            print("Valid number:", num)
            break                      # Exit loop if valid
        else:
            print("Out of range.")
    except ValueError:
        print("Not a number. Try again.")


# ---------- 7) MINI PROJECT: HORSE STABLE PLANNER (planificador de cuadras) ----------
# Example combining input, conditions, math, and date modules.

import math
import datetime

horses = input("Enter number of horses: ")
if horses == "0":
    print("No horses, no stables needed.")
else:
    capacity = input("Stable capacity (horses per stable): ")
    stables_needed = math.ceil(int(horses) / int(capacity))
    today = datetime.date.today()
    is_weekend = today.isoweekday() in (6, 7)   # 6=Saturday,7=Sunday
    print("Date:", today, "Weekend?", is_weekend)
    print("Stables needed:", stables_needed)


# ---------- 8) EXAM TIPS ----------
# - Use indentation correctly for if/elif/else and loops.
# - Show input validation with try/except.
# - Demonstrate break/continue inside a loop.
# - Combine range(), input(), and conditions in one example.
