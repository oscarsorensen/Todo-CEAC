# ==========================================
# UNIT 3 — Control Structures (Python)
# (Uso de estructuras de control)
# Keywords: (condicionales if/elif/else, bucles for/while,
# operadores lógicos, break, continue, range, assert)
# ==========================================

# ---------- 1) IF / ELIF / ELSE (condicionales) ----------
score = 78
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"
print("grade:", grade)

# ---------- 2) FOR (bucle for) ----------
for i in range(1, 6):  # 1..5
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

# ---------- 3) WHILE (bucle while) ----------
count = 0
while count < 3:
    print("count:", count)
    count += 1

# ---------- 4) BREAK / CONTINUE / PASS ----------
for n in range(10):
    if n == 3:
        continue
    if n == 7:
        break
    if n == 5:
        pass
    print(n, end=" ")
print()

# ---------- 5) LOGICAL OPERATORS (operadores lógicos) ----------
x, y, z = 5, 10, 20
if x < y and y < z:
    print("strictly increasing")

# ---------- 6) INPUT VALIDATION + LOOP ----------
# Guess the number mini (structure only)
import random
secret = random.randint(1, 10)
attempts = 0
while attempts < 3:
    try:
        guess = int(input("Guess 1..10: "))
        if guess < 1 or guess > 10:
            print("Out of range"); continue
        attempts += 1
        if guess == secret:
            print("Correct!"); break
        print("Higher" if guess < secret else "Lower")
    except ValueError:
        print("Enter a valid number")
else:
    print("No more attempts. Secret:", secret)

# ---------- 7) ASSERTIONS ----------
assert 1 <= secret <= 10, "Secret out of range"

# EXAM TIPS:
# - Show a complete loop with validation and control flow keywords.
# - Avoid infinite loops unless intended; ensure terminating condition.
