#CRUD
#Create
#Read
#Update
#Delete


# Defino la clase Cliente (necesario antes de usar Cliente())
class Cliente:
    def __init__(self):
        self.nombre = ""
        self.email = ""
        self.direccion = ""


print("Programa de gestion de clientes c0.1 Oscar Sorensen")
#Muestro opciones en el menu para el usuario
print("1. Insertar un cliente")
print("2. listar clientes")
print("3. actualizar clientes")
print("4 Eliminar clientes")


clientes = [] #creo una lista VACIO

while True: #Esto deseta un bucle infinito pero controlado
    
    #le permito escoger una opcion
    opcion = input("Escoge una opcion")
    opcion = int(opcion) #convierto a entero
    
    if opcion == 1:
        print("Vamos a insertar un cliente")
        #primero creamos un nuecvo cliente
        nuevocliente = Cliente()
        #Ahora le ponemos propiedades
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        # A la lista de clientes añadimos nuestro cliente
        clientes.append(nuevocliente)

    elif opcion == 2:
        print("Vamos a ver los clientes")
        
    elif opcion == 3:
        print("Vamos a actualizat un cliente")
    elif opcion == 4:
        print("Vamos a eliminar un cliente")
        break

