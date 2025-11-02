# ==========================================
# UNIT 004 — Desarrollo de clases (Class Development)
# Keywords: (clase, objeto, propiedades, métodos, constructor, CRUD, getters, setters)
# ==========================================

# Classes combine data (attributes) and behavior (methods).
# You create multiple objects (instances) from one class.

# ---------- 1) DEFINE CLASS AND CONSTRUCTOR ----------
class Client:
    def __init__(self, name, email):   # (constructor)
        # 'self' refers to the specific object being created
        self.name = name               # property (propiedad)
        self.email = email             # property (propiedad)

    def show_info(self):               # method (método)
        print(f"Client: {self.name}, Email: {self.email}")

# Create and use an object
c = Client("Oscar", "o@example.com")
c.show_info()


# ---------- 2) LIST OF OBJECTS + CRUD MENU ----------
clients = []                           # lista para guardar objetos

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def insert_client():
    name = input("Name: ")
    email = input("Email: ")
    clients.append(Client(name, email))
    print("Inserted.")

def list_clients():
    if len(clients) == 0: 
        print("No clients yet.")
        return
    i = 1
    for c in clients:
        print(i, c.name, c.email)
        i = i + 1

# Simple CRUD (Create, Read, Update, Delete) simulation
while True:
    print("\n1) Insert  2) List  3) Exit")
    op = input("> ")
    if op == "1":
        insert_client()
    elif op == "2":
        list_clients()
    elif op == "3":
        break
    else:
        print("Invalid option")



# ---------- 3) PRIVATE ATTRIBUTES + GETTERS/SETTERS ----------
class BankAccount:
    def __init__(self):
        self._balance = 0.0            # underscore indicates internal use (privado)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance

acc = BankAccount()
acc.deposit(100)
acc.withdraw(40)
print("Balance:", acc.get_balance())


# ---------- 4) EXAM TIPS ----------
# - Include at least one __init__ constructor.
# - Show property assignment and access.
# - Demonstrate methods that modify data.
# - Use self consistently inside class methods.
