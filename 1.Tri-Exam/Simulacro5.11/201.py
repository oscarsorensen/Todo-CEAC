import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="useroscar",
    password="Oscar081100!",
    database="PortafolioDB"
)


cursor = connection.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);
""")
connection.commit()

#########################################

print("=== CLIENT MANAGEMENT PROGRAM (MySQL) ===")

while True:
    print("""
1. Create new client
2. List all clients
3. Update client
4. Delete client
5. Exit
""")

    option = int(input("Choose an option: "))

    if option == 1:
        nombre = input("Name: ")
        apellidos = input("Surname: ")
        email = input("Email: ")
        cursor.execute("""
        INSERT INTO clientes (nombre, apellidos, email)
        VALUES (%s, %s, %s);
        """, (nombre, apellidos, email))
        connection.commit()
        print("Client added.")

    elif option == 2:
        cursor.execute("SELECT * FROM clientes;")
        for row in cursor.fetchall():
            print(row)

    elif option == 3:
        identificador = input("Client ID to update: ")
        nombre = input("New name: ")
        apellidos = input("New surname: ")
        email = input("New email: ")
        cursor.execute("""
        UPDATE clientes
        SET nombre = %s, apellidos = %s, email = %s
        WHERE Identificador = %s;
        """, (nombre, apellidos, email, identificador))
        connection.commit()
        print("Client updated.")

    elif option == 4:
        identificador = input("Client ID to delete: ")
        cursor.execute("DELETE FROM clientes WHERE Identificador = %s;", (identificador,))
        connection.commit()
        print("Client deleted.")

    elif option == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

connection.close()
