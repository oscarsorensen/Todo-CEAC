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
