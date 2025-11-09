
# =====================================================================
# EXAMEN RESUMEN - PROGRAMACIÓN (UNIDADES 001–007)
# Autor: Oscar Sørensen
# Profesor: José Vicente Carratalá (CEAC)
# ---------------------------------------------------------------------
# Este archivo combina todo el contenido de las unidades de Programación.
# Cada bloque está comentado en español y ordenado para servir de repaso.
# ---------------------------------------------------------------------
# 1. Conceptos básicos: variables, operadores, condicionales, bucles
# 2. Funciones y manejo de excepciones
# 3. Clases, constructores, métodos y propiedades
# 4. Lectura/escritura de archivos de texto, JSON y pickle
# 5. Mini-aplicación CRUD con menú en consola
# 6. Ejemplo de integración con base de datos
# =====================================================================



# ====================================================
# Contenido original de: Programacion/001. Identificacion de los elementos/Scripts/stortprogram.py
# ====================================================


#Jocarsa der fortñller vhordan jeg kan lave mit program

url = "https://jocarsa.com/"

try:
    response = requests.get(url, timeout=10)
    
#generelt skal jeg bare følge med i hvad der sker i undervisningen og så lærer jeg hvad jeg skal. Jeg kan lave mit program i python.


# ====================================================
# Contenido original de: Programacion/002. Utilazicion de objetos/005 Methodos estaticos/001 gato.py
# ====================================================


class Gato():
    def __init__(self):
        self.nombre = ""
    def maullar(self):
        return("Miau miau")
    gato1 = Gato()
    gato1.nombre = "Misifu"
    
    gato2 = Gato()
    gato2.nombre = "Belcebu"


# ====================================================
# Contenido original de: Programacion/002. Utilazicion de objetos/005 Methodos estaticos/002 matematicas.py
# ====================================================


class Matematicas():
    def __init__(self):
        self.numero = 0
    def suma(self,a,b):
        return a + b
    
    
operacion1 = Matematicas()
print(operacion1.suma = (4,4))

operacion2 = Matematicas()
print(operacion2.suma = (6,7))




# ====================================================
# Contenido original de: Programacion/002. Utilazicion de objetos/005 Methodos estaticos/003 metodo pseudo.py
# ====================================================




class Matematicas():
    def __init__(self):
        self.numero = 0
    def suma(self,a,b):
        return a + b


print(Matematicas.suma = (6,7))




# ====================================================
# Contenido original de: Programacion/002. Utilazicion de objetos/005 Methodos estaticos/004 metodo estatico.py
# ====================================================



class Matematicas:
    def __init__(self):
        self.numero = 0

    @staticmethod
    def suma(a, b):
        return a + b


print(Matematicas.suma(6, 7))



# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/005-for.py
# ====================================================



for mes in range(1,13):
    for dia in range(1,32):
        print("hoy es el dia",dia,"del mes",mes)


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/006-else.py
# ====================================================



edad = 24
if edad < 20:
    print("Eres muy joven")
else:
    print("No eres tan joven")


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/007-masanaditation.py
# ====================================================


for anio in range(1978, 2006):     # years 1978–2005
    for mes in range(1, 13):       # months 1–12
        for dia in range(1, 32):   # days 1–31 (not checking real month lengths)
            print("Hoy es el dia", dia, "del mes", mes, "del anio", anio)



# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/017-functions.py
# ====================================================



def calculaSuma(operando1, operando2):
    resultado = operando1 + operando2
    return resultado

calculaSuma(4, 3)
print(calculaSuma(4, 3))
print(calculaSuma(10, 5))
print(calculaSuma(7, 8))


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/26.9.py
# ====================================================




# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/Prueba.py
# ====================================================




def divide(dividendo, divisor):
    try:                                 #intenta
        dividendo = int(dividendo)       #convertir dividendo a entero
        divisor = int(divisor)          #

        if divisor != 0:                            
            return dividendo / divisor            
        else:      
            return False                        
    except:
        return "Error: No se puede dividir por texto"


for dividendo in range(-100, 100):
    for divisor in range(-100, 100):
        print(divide(dividendo, divisor))

print(divide(4,"a "))



# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/codigoanadido.py
# ====================================================

edad = 47
if edad < 20:
    if edad < 10:
        print("Eres un niño")
    else:
        print("Eres un adolescente")
else:
    if edad < 30:
        print("Eres un joven")
    else:
        print("Ya no eres un joven")


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/creo.un.gato.py
# ====================================================


class Gato():
    def __init__(self):
        self.color = ""
        self.nombre = ""

gato1 = Gato()
print(gato1)
gato1.nombre = "Garfield"
gato1.color = "naranja"

gato2 = Gato()
print(gato2)
gato2.nombre = "Bob"
gato2.color = "naranja"


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/divisor.py
# ====================================================



def divisor(dividendo,divisor):
    return dividendo/divisor

print(divisor(4,3))


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/elseif.py
# ====================================================



edad = 24
if edad < 10:
    #esto no es menor que 10
    print("Eres un niño")
elif edad >= 10 and edad < 20:
    #se ejecuta si la edad es mayor que 10 y menor que 20
    print("Eres un adolescente")
elif edad >= 20 and edad < 30:
    #se ejecuta si la edad es mayor que 20 y menor que 30
    print("Eres un joven")
else:
    #se ejecuta en cualquier otro caso
    print("Eres un adulto")


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/infopytho.py
# ====================================================


'''
Forskel mellem JavaScript og Python

<script>
var edad = 24;
if(edad <20){
    document.write("Eres muy joven");
}

</script>

'''

#PYTHON

edad = 24
if edad < 20:
    print("Eres muy joven")


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/pythonstart.py
# ====================================================

nombre = "Oscar"
print(nombre)
print("Hello World")


# ====================================================
# Contenido original de: Programacion/003. Uso de estructuras/Python/start python first week/test.py
# ====================================================

'''
Programa calculadora de IVA
(c) 2025 Oscar
Esto es un ejercicio de clase
'''

# Define IVA
IVA = 0.21

# Toma entradas
nombre = input("Introduce el nombre: ")
precio_base = input("Introduce el precio de venta: ")
almacenamiento_gb = input("Introduce la capacidad del dispositivo (GB): ")
peso_g = input("Introduce el peso en gramos: ")
pantalla_pulgadas = input("Introduce el tamaño de la pantalla en pulgadas: ")

# Convierte tipos
precio_base = int(precio_base)
almacenamiento_gb = int(almacenamiento_gb)
peso_g = int(peso_g)
pantalla_pulgadas = int(pantalla_pulgadas)

# Calcula
total_iva = precio_base * IVA
precio_total = precio_base + total_iva
almacenamiento_mb = almacenamiento_gb * 1024
peso_kg = peso_g / 1000

# Compara sin if
presupuesto_max = 800.0
excede_presupuesto = precio_total > presupuesto_max

# Salida
print("Nombre:", nombre)
print("Precio base:", precio_base)
print("Precio total con IVA:", precio_total)
print("Almacenamiento:", almacenamiento_mb, "MB")
print("Peso:", peso_kg, "kg")
print("Excede presupuesto:", excede_presupuesto)

print("el total de IVA es:", total_iva)
print("El precio total es:", precio_total)
print("la cantiad de almacenamiento:", pantalla_pulgadas)
print("el peso en kg es:", peso_kg)
print("el maximo presupuesto es:", presupuesto_max)
print("Excede el presupuesto:", excede_presupuesto)



# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/001regraso de los metodos.py
# ====================================================



class Gato():
    def __init__(self):
        self.color = ""      #esto es  una propiedad
        
    def maulla(self):         #esto es un metodo (es una accion)
        return "miau"

    def setColor(self, nuevocolor):     #define un setter - el metodo es el responsable de cambiar la propiedad
        #por ejemplo aqui podria validar si el color es un color valido para un gato
        self.color = nuevocolor         #Y camvio la propiedad color

    def getColor(self):
        #una vez mas, aqui podria poner validaciones si lo quisiera
        return self.color

    
gato1 = Gato()
gato1.color = "naranja"         #aqui seteamos una propiedad directamente (no es buena practica)
print(gato1.maulla())             #aqui llamamos a un metodo

gato1.setColor("naranja")       #Esto es una practica mucho mejor

print(gato1.color)              #acceco directo, se puede pero no es buena practica

print(gato1.getColor())        #esto es mejor, se recomienda


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/002propiedad.privada.py
# ====================================================




class Gato():
    def __init__(self):
        self.__color = ""      #esto es  una propiedad privada (contrapuesta a publica)
        
gato1 = Gato()
print(gato1.__color)   #esto da error, la propiedad es privada
        



# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/006-applicacion.py
# ====================================================


'''
Applicacion de gestion de productos
(c)2024 Oscar Sorensen

'''

#En esta applicacion no aplica importar librerias

#Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = None
        self.precio = 0.0
# creamos las variables globales 

productos = []

#Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v1.0, Oscar Sorensen")
#Le mostaramos al usuario las opciones que tiene
print("Seleccione una opcion")
print("1.- Crear un nuevo producto")
print("2.- Mostrar los productos")
print("3.- Actualizar un producto")
print("4.- Eliminar un producto")
opcion = int(input("Escoga una opcion (1-4): "))
#en funcion de la opcion que coja el usuario
if opcion == 1:
    #0 bien creamos un nuevo producto
    print("creamos un nuevo producto")
    producto = Producto() #creamos un nuevo producto
    producto.nombre = input("Nombre del producto: ")
    producto.precio =input("Precio del producto: ")
    productos.append(producto) #lo añadimos a la lista de productos
    
    
elif opcion == 2:
    #0 bien mostramos los productos
    print("mostramos los productos")
elif opcion == 3:
    #0 bien actuazamos los productos
    print("actualizamos los productos")
elif opcion == 4:
    #0 bien eliminamos los productos
    print("vamos a eliminar los productos")
# Y volvemos a repetir


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/10.py
# ====================================================


cliente1 = "Juan"
cliente2 = "Jorge"

clientes = ["Juan","Jorge","Jaime","Jose"]

print(clientes)

#Añadir un cliente

clientes.append("Julia")

print(clientes)

#Quito un elemento de la lista

clientes.pop()

print(clientes)



# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/crud.py
# ====================================================

# Defino la clase Cliente (necesario antes de usar Cliente())
class Cliente:
    def __init__(self):
        self.nombre = ""
        self.email = ""
        self.direccion = ""


print("Programa de gestion de clientes c0.1 Oscar Sorensen")
print("1. Insertar un cliente")
print("2. Listar clientes")
print("3. Actualizar cliente")
print("4. Eliminar cliente")
print("5. Salir")

clientes = []  # creo una lista VACÍA

while True:  # Esto desata un bucle infinito pero controlado

    opcion = input("Escoge una opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        print("Vamos a insertar un cliente")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        clientes.append(nuevocliente)
        print("Cliente insertado correctamente")

    elif opcion == 2:
        print("Vamos a ver los clientes")
        for cliente in clientes:
            print(cliente.nombre, cliente.email, cliente.direccion)

    elif opcion == 3:
        print("Vamos a actualizar un cliente")
        nombreabuscar = input("Introduce el nombre del cliente a actualizar: ")
        for cliente in clientes:
            if cliente.nombre == nombreabuscar:
                cliente.email = input("Nuevo email: ")
                cliente.direccion = input("Nueva direccion: ")
                print("Cliente actualizado correctamente")

    elif opcion == 4:
        print("Vamos a eliminar un cliente")
        nombreabuscar = input("Introduce el nombre del cliente a eliminar: ")
        for cliente in clientes:
            if cliente.nombre == nombreabuscar:
                clientes.remove(cliente)
                print("Cliente eliminado correctamente")

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta otra vez")



# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/declarations.py
# ====================================================



#Declaramos una clase

class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

#Usamos la clase istanciando en un objeto

cliente1 = Cliente()
cliente.email = input("email")
cliente.nombre = inpit("nombre")
cliente.direccion = ("direcction")

print(cliente1)
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direcction)


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/proeidades.py
# ====================================================


#las propiedades son como las variables PERO dentro de una clase

class Cliente():
    def __init__(self):
        self.nombre = None
        self.edad = 0
        self.telefonos = []

#Ahora instancio un nueco objeto
cliente1 = Cliente()

#Ahora le escribo una propiedad

cliente1.nombre = "Oscar Sorensen"

print("El nombre del cliente es: ", cliente1.nombre)

cliente1.telefonos.append("587349373")
cliente1.telefonos.append("187349374")

print(cliente1.telefonos)




# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/test.py
# ====================================================




# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/004-Desarollo/testafflask.py
# ====================================================



#sudo apt install python3-flask
#pip install flask - windows

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
    
        <!doctype html>
        <html>
            <head>
                <title></title>
                <style>
                    h1{color: red;}
                </style>
            </head>
            <body>
                <h1>Esto es HTML a tope de power</h1>
                '''
    for dia in range (1, 31):
        cadena += '<div>'+str(dia)+'</div>'
    
    cadena += '''
            </body>
        </html>
    '''
    return cadena

if __name__ == "__main__":
    aplicacion.run(debug=True) 


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/007gatocliente.py
# ====================================================


class Cliente():
    def __init__(self, nombre, apellidos, email, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion  # fixed typo: direccopm → direccion

clientes = []
while True:

    nombre = input("Introduce el nombre del cliente: ")
    apellidos = input("Introduce los apellidos del cliente: ")
    email = input("Introduce el email del cliente: ")
    direccion = input("Introduce la dirección del cliente: ")

    clientes.append(Cliente(nombre, apellidos, email, direccion))

    print(clientes)



# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/ahoraleemos.py
# ====================================================

archivo = open("clientes.txt", "r") # R = Read

contenido = archivo.readline()
#Tambien existe archivo.readlines() 

print(contenido)
archivo.close()


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/bookleinfinito.py
# ====================================================


while True:
    print("Dime lo que quieres hacer")
    print("1. Introduce un nuevo contacto")
    print("2. Leer todos los contactos")
    opcion = input("Escoge tu opcion (1 o 2): ")
    opcion = int(opcion)
    if opcion == 1:
        nombre = input("Dime el nombre del contacto")
        email = input("Dime el email del contacto")
        archivo = open("agenda.txt", "a")  # A = Append
        archivo.write(nombre + "," + email + "\n")
        archivo.close()
    elif opcion == 2:
        archivo = open("agenda.txt", "r")
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
        archivo.close()
    


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/clasematematic2.py
# ====================================================



import math
    

print(round(4.7))
print(round(4.2))
print(math.ceil(4.7))
print(math.floor(4.7))

        


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/clasematematicas.py
# ====================================================



class Matematicas():
    def __init__(self):
        self.PI = 3.1416
        
    def redondeo(self,numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondeo = 0
        else :
            redondeo = 1
        return entero + redondeo
    
    def techo(self,numero):
        return int(numero) + 1
    def suelo(self,numero):
        return int(numero)
    
    
Mate = Matematicas()
print(Mate.redondeo(4.7))
print(Mate.redondeo(4.2))
print(Mate.techo(4.7))
print(Mate.suelo(4.7))

        


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/escribirtexto.py
# ====================================================



archivo = open("clientes.txt", "w") # W = Write

archivo.write("Esto es una prueba")

archivo.close()


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/gato.py
# ====================================================


class Gato():
    def __init__(self,edad,nombre,raza): #el constructor se ejecuta si o si
        self.edad = 0
        self.nombre = nombre
    
    def maulla(self):   #el resto de metodos solo se ejecutan si los llamas
        return "el gato esta maullando"
    
    
gato1 = Gato(5,"micifu","siames")
    





# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005-constructores/gatosperros.py
# ====================================================


class Entidad():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Animal(Entidad):
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""

class Gato(Animal):
    def __init__(self):
       super().__init__()    # Llamada al constructor de la clase "superior". 
                             #meaning, the Animal class.

        
class Perro(Animal):
    def __init__(self):
        super().__init__()

        
class Roca(Entidad):
    def __init__(self):
        super().__init__()
        


        
gato1 = Gato()
print(gato1.edad)
        
perro1 = Perro()
print(perro1.edad)


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005classeCuentaBancaria/001.py
# ====================================================



limitediferenciasaldo = 1000

class CuentaBancaria():
    def __init__(self):
        self.__saldo = 0
        self.__cliente = ""
#Definir setters y getters para el saldo y el cliente
    def setSaldo(self, nuevosaldo):
        #establezco una condicion de que valida si el saldo nuevo es mayor de 100 euros
        if nuevosaldo > self.__saldo + 100:
            #si salta la alarma, avisa y no cambia el saldo
            print("Voy a avisar a la entidad de un ingreso my grande")
        else:
            #si pasa el filtro, solo entonces se cambia el saldo
            self.__saldo = nuevosaldo
        
    def getSaldo(self):
        return self.__saldo
    
cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(10000000)
print(cuentacliente1.getSaldo())


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/005classeCuentaBancaria/010.clasepractico.py
# ====================================================



class Cliente():
    #Este es ek metodo constructor
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
        
    #Entos son setter y getters
    def setNombreCompleto(self, nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self, nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email
    
#CRUD - Create, Read, Update, Delete
#CRUD SQL - INSERT, SELECT, UPDATE, DELETE

clientes = []            ##########Lista vacia de clientes

print("GEstor de clientes v0.1 Oscar Sorensen")
while True:
    print("Selecciona una opcion")
    print("1. Crear cliente")
    print("2. Obtener listado de clientes")
    opcion = int(input("Indica tu opcion (1 o 2): "))

    if opcion == 1:      #Los SETTERS se usan en las operaciones de creacion de nuevos elementes
        print("Voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input("Indica el nombre del cliente: ") #Tomo el dato
        nuevocliente.setNombreCompleto(nombrecliente) #Uso el metodo set para meter el dato en el objeto
        emailcliente = input("Indica el email del cliente: ") #Tomo el dato
        nuevocliente.setEmail(emailcliente) #Uso el metodo set para meter el dato en el objeto
        clientes.append(nuevocliente)  #y por ultimo inserto el objeto en la lista
    elif opcion == 2:       #Los GETTERS se usan en las operaciones de listado
        print("Saco el listado de clientes")
        for cliente in clientes:
            print("nombre", cliente.getNombreCompleto())
            print("email", cliente.getEmail())
            print("--------------")    
        
        


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/006-Librerias/003.py
# ====================================================

import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for linea in contenido:
    print(["############## ARTICULO ##############"])  
    print(linea['titulo']) 
    print(linea['fecha'])
    print(linea['autor'])
    print(linea['contenido'])
    print(['##############  ##############'])
    print([""])


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/006-Librerias/2001.py
# ====================================================


    
archivo = open("blog.txt",'r')

lineas = archivo.readlines()

for linea in lineas:
    print(linea)
    



# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/006-Librerias/import.json.py
# ====================================================


import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

print(contenido)


# ====================================================
# Contenido original de: Programacion/004. Desarollo de classes/006-Librerias/testflask.py
# ====================================================


from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''

<!doctype html>
<html lang="es">
    <head>
        <title>OscarBLOG</title>
        <meta charset="UTF-8">
        <style>
            body{background:steelblue;color:steelblue;font-family:sans-serif;}
            header,main,footer{background:white;padding: 20px;margin:auto;width: 600px;}
            header,footer{text-align: center;}
            main{color: black;}
        </style>
    </head>
    <body>
        <header><h1>OscarBLOG</h1></header>
        <main>
            <article>
                <h3>Titulo de articulo</h3>
                <time>2025-10-16</time>
                <p>Oscar Sorensen</p>
                <p>Este es el contenido de un articulo ficticio</p>
            </article>

        </main>

    <footer>
        (c)2025 Oscar Sorensen
    </footer>

    </body>

'''

#ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/003 open and close files/001.escribir.py
# ====================================================


#"w" laver en fil, "a" laver en NY fil- Meget bedre. 
archivo = open ("basededatos.txt","a")
archivo.write("esto es un contenido"\n)
archivo.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/003 open and close files/002.leer. una linea.py
# ====================================================



archivo = open ("basededatos.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    print(lineas)

archivo.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/003 open and close files/007 pickle escribir.py
# ====================================================


import pickle
archivo = open("datos.bin","rb")
cadena = "Oscar Sorensen"

pickle.dump(cadena,archivo)

archivo.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/003 open and close files/008 pickle read.py
# ====================================================




import pickle
archivo = open("datos.bin","rb")
cadena = "Oscar Sorensen"

pickle.dump(cadena,archivo)

archivo.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/003 open and close files/009 crear cliente.py
# ====================================================



class Cliente():
    def __iniit__(self, nuevonombre, nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes = []

clientes.append(Cliente("Oscar Sorensen","info@oscar.com"))
clientes.append(Cliente("Juan Bob","info@juan.com"))

print(clientes)


class Cliente:
    def __init__(self, nuevonombre, nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}"

clientes = []

clientes.append(Cliente("Oscar Sorensen", "info@oscar.com"))
clientes.append(Cliente("Juan Bob", "info@juan.com"))

for cliente in clientes:
    print(cliente)



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/003 open and close files/010 gurado con pickle.py
# ====================================================

import pickle

class Cliente:
    def __init__(self, nuevonombre, nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail


clientes = []

clientes.append(Cliente("Oscar Sorensen", "info@oscar.com"))
clientes.append(Cliente("Juan Bob", "info@juan.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/003 open and close files/011 recupoero los datos.py
# ====================================================

import pickle

class Cliente:
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail


clientes = []


archivo = open("clientes.bin","rb")
clientes = pickle.load(archivo)
archivo.close()

print(clientes)


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/001 listar contenido.py
# ====================================================



import os

carpeta=input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    print(elemento)
    
    


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/002 atributos.py
# ====================================================



import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    print(ruta)
    print(os.path.getsize(ruta))
    print(os.path.getmtime(ruta))
    


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/004 suma taman╠âo.py
# ====================================================



import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)
suma = 0

for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    suma += os.path.getmtime(ruta)

print("La carpeta ocupa: ")
print(suma/(1024*1024),"MB")

    


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/005  revisar carpeta.py
# ====================================================




import os

carpeta = input("Indica una carpeta: ")

for directorio,carpetas, archivo in os.walk(carpeta):
        print(directorio)
        print(carpetas)
        print(archivo)
        



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/006 taman╠âo recursivo.py
# ====================================================



import os

carpeta = input("Indica una carpeta: ")

suma = 0

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            suma += os.path.getsize(ruta)
        except:
            pass  # Evita errores si un archivo no se puede leer

print("La carpeta ocupa:")
print((suma / (1024 * 1024)), "MB")



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/007 condicion.py
# ====================================================

import os

carpeta = input("Indica una carpeta: ")
grande = 1024 * 1024 * 1024  # 1 GB

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if os.path.getsize(ruta) > grande:
                print(ruta,os.path.getsize(ruta)/(1024*10), "MB")
        except:
            pass  # Evita errores si un archivo no se puede leer





# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/008 escribir archivo.py
# ====================================================



import os

carpeta = input("Indica una carpeta: ")
grande = 1024 * 1024 * 1024  # 1 GB

mapa = open("mapa.txt", "a")

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        mapa.write(ruta + "\n")

mapa.close()




# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/010-minibuscador.py
# ====================================================


cadena = "Esto es ima cadena de prueba"
#Skift manzana med "prueba" pg saa virker det
objetivo = "manzana"   

if objetivo in cadena:
    print("Efictivamente esta")
else:
    print("No esta")
    



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/011 busca mapa.py
# ====================================================



archivo = open("mapa.txt",'r') #READ

lineas = archivo.readlines()

for linea in lineas:
    if "json" in linea:
        print("Encontrado!: ",linea)


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/012 usuario busca.py
# ====================================================




archivo = open("mapa.txt",'r') #READ
busca = input("Introduce el temino a buscar: ")


lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("#######################")
        print("Encontrado!: ",linea)
        


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/001.py
# ====================================================


import os

os.mkdir("mi_carpet123")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/002 micarpeta.py
# ====================================================


import os

os.rmdir("mi_carpet123")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/004.py
# ====================================================


import os

try:
    os.rmdir("mi_carpeta123")
except:
    print("Ha habido un error, continuamos...")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/005 miarchivo.py
# ====================================================



open("miarchivo.txt", "w")



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/006 deletearchivo.py
# ====================================================



import os    
# Crear un archivo para eliminarlo después
  #  open("miarchivo.txt", "w")

os.remove("miarchivo.txt")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/007 nuevoarchivo.py
# ====================================================



archivo = open("miarchivo.txt", "w")

archivo.write("Esto es un texto de prueba.")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/008 comprimir.py
# ====================================================


import zipfile

origen = 'miarchivo.txt'

destino = 'comprimido.zip'

archivo_zip = zipfile.ZipFile(destino, 'w')
archivo.write(origen)


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/009 -2 compresion.py
# ====================================================


import zipfile

origen = '1. Scripts.txt'

destino = 'comprimidoscriptsfile.zip'

archivo_zip = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)

# this changes my file 1. Scripts from 16 bytes to 1 bytes after compression
# destino er det nye navn filen får 
# origen er filen som bliver komprimeret


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/009 tests.py
# ====================================================



import zipfile

origen = '1. Scripts.txt'

destino = 'comprimidoscriptsfile.zip'

archivo_zip = zipfile.ZipFile(destino, 'w')
archivo.write(origen)

# this changes my file 1. Scripts from 16 bytes to 1 bytes after compression
# destino er det nye navn filen får 
# origen er filen som bliver komprimeret


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/010 comprimir.py
# ====================================================

import zipfile
import os

carpeta = "1. Scripts"

for directorio, carpetas, archivos in os.walk(carpeta):
    for nombre_archivo in archivos:
        origen = os.path.join(directorio, nombre_archivo)
        destino = os.path.join(directorio, nombre_archivo + ".zip")
        archivo_zip = zipfile.ZipFile(destino, "w", compression=zipfile.ZIP_DEFLATED)
        archivo_zip.write(origen, arcname=nombre_archivo)
        archivo_zip.close()

print("Comprimido:", destino)

#dette comprimerer alt i mappen 1. Scripts. Individuelt. Ikke skide praktisk.



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/011 comprimir carpeta.py
# ====================================================



import os
import zipfile

origen = "archivos"
destino = "archivos.zip"

archivo_zip = zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED)
for directorio, carpetas, archivos in os.walk(origen):
    for nombre_archivo in archivos:
        rutaarchivo = os.path.join(directorio, nombre_archivo)
        rutarelativa = os.path.relpath(rutaarchivo, origen)
        archivo_zip.write(rutaarchivo, rutarelativa)
        
archivo_zip.close()
    


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/012 ejercito final.py
# ====================================================


'''
Quiero:
1. oedir al usuario una ruta de una carpeta con input
2. repasar todas las subcarpetas y archivos dentro de esa carpeta
3. para cada archivo o carpeta, quiero comprimirla en un zip
4. una vez comprimido, quiero eliminar el archivo o carpeta original
'''

import os
import zipfile
import shutil

'''
  Quiero:
  1.-Pedir al usuario una ruta de una carpeta con input
  2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
  3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
  4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales
'''

ruta = input("Introduce la ruta de la carpeta: ").strip()

try:
  # Comprobamos que la ruta existe y es una carpeta
  if not os.path.isdir(ruta):
    print("La ruta no es válida")
  else:
    # Recorremos SOLO el primer nivel dentro de la ruta dada
    for nombre in os.listdir(ruta):
      origen = os.path.join(ruta, nombre)

      # Evitar recomprimir ZIPs ya existentes
      if os.path.isfile(origen) and origen.lower().endswith(".zip"):
        continue

      # Si es una carpeta: crear un ZIP con todo su contenido y luego eliminarla
      if os.path.isdir(origen):
        destino = origen + ".zip"
        archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
        for directorio, subcarpetas, archivos in os.walk(origen):
          for archivo in archivos:
            rutaarchivo = os.path.join(directorio, archivo)
            rutarelativa = os.path.relpath(rutaarchivo, origen)
            archivozip.write(rutaarchivo, rutarelativa)
        archivozip.close()
        shutil.rmtree(origen)

      # Si es un archivo: comprimirlo y luego eliminar el original
      elif os.path.isfile(origen):
        destino = origen + ".zip"
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre)
        archivo.close()
        os.remove(origen)

except:
  print("Ha habido un error, continuamos")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/013 with gpt.py
# ====================================================

import os
import zipfile
import shutil
import sys
import time

#### CUIDADO CON ESTE PROGRAMA
#### USALO BIEN
#### UN GRAN PODER CONLLEVA UNA GRAN RESPONSABILIDAD

'''
  Quiero:
  1.-Pedir al usuario una ruta de una carpeta con input
  2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
  3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
  4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales (opcional con booleano)
  5.-Mostrar una barra de progreso en consola con porcentaje y estimación de tiempo
'''

# 1) Booleano para activar/desactivar el borrado de originales
borrar_originales = False  # ponlo a False para conservar los originales

# ---- Utilidades para la barra de progreso ----
def formatear_tiempo(segundos):
  segundos = int(segundos)
  h = segundos // 3600
  m = (segundos % 3600) // 60
  s = segundos % 60
  if h > 0:
    return f"{h:02d}:{m:02d}:{s:02d}"
  else:
    return f"{m:02d}:{s:02d}"

def mostrar_progreso(procesados, total, inicio):
  if total == 0:
    return
  porcentaje = (procesados / total)
  ancho_barra = 30
  rellenos = int(ancho_barra * porcentaje)
  barra = "[" + "#" * rellenos + "-" * (ancho_barra - rellenos) + "]"

  transcurrido = time.time() - inicio
  if procesados > 0:
    estimado_total = transcurrido / procesados * total
    restante = max(0, estimado_total - transcurrido)
  else:
    restante = 0

  texto = f"\r{barra} {porcentaje*100:6.2f}%  transcurrido: {formatear_tiempo(transcurrido)}  restante: {formatear_tiempo(restante)}"
  sys.stdout.write(texto)
  sys.stdout.flush()
# ---------------------------------------------

ruta = input("Introduce la ruta de la carpeta: ").strip()

try:
  # Comprobamos que la ruta existe y es una carpeta
  if not os.path.isdir(ruta):
    print("La ruta no es válida")
  else:
    # Preparamos la lista de ítems a procesar (solo primer nivel), excluyendo ZIPs
    items = []
    for nombre in os.listdir(ruta):
      origen = os.path.join(ruta, nombre)
      if os.path.isfile(origen) and origen.lower().endswith(".zip"):
        continue
      items.append(origen)

    total = len(items)
    procesados = 0
    inicio = time.time()
    mostrar_progreso(procesados, total, inicio)

    for origen in items:
      nombre = os.path.basename(origen)

      # Si es una carpeta: crear un ZIP con todo su contenido
      if os.path.isdir(origen):
        destino = origen + ".zip"
        archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
        for directorio, subcarpetas, archivos in os.walk(origen):
          for archivo in archivos:
            rutaarchivo = os.path.join(directorio, archivo)
            rutarelativa = os.path.relpath(rutaarchivo, origen)
            archivozip.write(rutaarchivo, rutarelativa)
        archivozip.close()

        # Borrar carpeta original si está activado
        if borrar_originales:
          shutil.rmtree(origen)

      # Si es un archivo: comprimirlo
      elif os.path.isfile(origen):
        destino = origen + ".zip"
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre)
        archivo.close()

        # Borrar archivo original si está activado
        if borrar_originales:
          os.remove(origen)

      # Actualizamos progreso
      procesados += 1
      mostrar_progreso(procesados, total, inicio)

    print()  # salto de línea al terminar la barra
    print("Proceso completado.")

except:
  print("\nHa habido un error, continuamos")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/003 creamos un contructor.py
# ====================================================




# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/004 contructor con parametros.py
# ====================================================


    
    class Cliente():
        def __init__(self,nombre,apellido,email):
            self.nombre = nombre
            self.apellido = apellido
            self.email = email


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/005 pantalla de bienvenida.py
# ====================================================



    
    class Cliente():
        def __init__(self,nombre,apellido,email):
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/006 bucle infinito.py
# ====================================================


    
    
    
    class Cliente():
        def __init__(self,nombre,apellido,email):
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")


while True:


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/007 creamos lista entidades.py
# ====================================================



    
    class Cliente():
        def __init__(self,nombre,apellido,email):
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

[clientes] = []

while True:


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/008 creamos menu.py
# ====================================================





    
    class Cliente():
        def __init__(self,nombre,apellido,email):
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

[clientes] = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/009 atrapamos las opciones.py
# ====================================================


    class Cliente():
        def __init__(self,nombre,apellido,email):
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

[clientes] = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))
    
    
    
    if opcion == 1:
        
        
    elif opcion == 2:
        
    elif opcion == 3:
        
    elif opcion == 4:


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/010 desarollamos insertar clientes.py
# ====================================================



    class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))
    
    
    
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        
    elif opcion == 2:
        
    elif opcion == 3:
        
    elif opcion == 4:


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/011 aprendicamos.py
# ====================================================




    class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))
    
    
    
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
        
    elif opcion == 2:
        
    elif opcion == 3:
        
    elif opcion == 4:


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/012 pass de momento.py
# ====================================================





    class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))
    
    
    
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
        
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/013 desarollo leer.py
# ====================================================


    class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))
    
    
    
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
        
    elif opcion == 2:
        for cliente in clientes:
            print(cliente.nombre, cliente.apellidos, cliente.email)
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/014 imprimimos mejor el cliente.py
# ====================================================



    class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))
    
    
    
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
        
    elif opcion == 2:
        for cliente in clientes:
            print(cliente.nombre, cliente.apellidos, cliente.email)
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/015 actualizar es como insertar con id.py
# ====================================================


class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


print("**************** Gestion de clientes v0.1 ******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))

    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre, apellidos, email))

    elif opcion == 2:
        for i, cliente in enumerate(clientes):
            print(i, cliente.nombre, cliente.apellidos, cliente.email)

    elif opcion == 3:
        identificador = int(input("Introduce el ID del cliente a actualizar: "))
        nombre = input("Introduce el nuevo nombre del cliente: ")
        apellidos = input("Introduce los nuevos apellidos del cliente: ")
        email = input("Introduce el nuevo email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    elif opcion == 4:
        pass



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/016 chivamos el id.py
# ====================================================

class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


print("**************** Gestion de clientes v0.1 ******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))

    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre, apellidos, email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:", identificador)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el ID del cliente a actualizar: "))
        nombre = input("Introduce el nuevo nombre del cliente: ")
        apellidos = input("Introduce los nuevos apellidos del cliente: ")
        email = input("Introduce el nuevo email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    elif opcion == 4:
        pass



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/017 eliminar elemento.py
# ====================================================

class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


print("**************** Gestion de clientes v0.1 ******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))

    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre, apellidos, email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:", identificador)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el ID del cliente a actualizar: "))
        nombre = input("Introduce el nuevo nombre del cliente: ")
        apellidos = input("Introduce los nuevos apellidos del cliente: ")
        email = input("Introduce el nuevo email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    elif opcion == 4:
        identificador = int(input("Introduce el ID del cliente a eliminar: "))
        confirmacion = input("¿Estás seguro de que deseas eliminar este cliente? (s/n): ")
        if confirmacion == 's' or confirmacion == 'S':
            clientes.pop(identificador) #josevicente uses remove here, but pop is better for index. because we got the id.
            print("Cliente eliminado.")
        elif confirmacion == 'n' or confirmacion == 'N':
            print("Eliminación cancelada.")
        else:
            print("Opción no válida. Eliminación cancelada.")



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/018 guardamos con pickle.py
# ====================================================

import pickle

class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


print("**************** Gestion de clientes v0.1 ******************")
print("****************** Oscar Sorensen **************************")

clientes = []

try: ############## Ojo que igual no existe el archivo ########
    archivo = open("clientes.dat",'rb')
    clientes = pickle.load(archivo)
except:
    print("No existe archivo de datos")

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))

    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre, apellidos, email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:", identificador)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el ID del cliente a actualizar: "))
        nombre = input("Introduce el nuevo nombre del cliente: ")
        apellidos = input("Introduce los nuevos apellidos del cliente: ")
        email = input("Introduce el nuevo email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    elif opcion == 4:
        identificador = int(input("Introduce el ID del cliente a eliminar: "))
        confirmacion = input("¿Estás seguro de que deseas eliminar este cliente? (s/n): ")
        if confirmacion == 's' or confirmacion == 'S':
            clientes.pop(identificador) #josevicente uses remove here, but pop is better for index. because we got the id.
            print("Cliente eliminado.")
        elif confirmacion == 'n' or confirmacion == 'N':
            print("Eliminación cancelada.")
        else:
            print("Opción no válida. Eliminación cancelada.")


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/019 guardamos.py
# ====================================================

import pickle

class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


print("**************** Gestion de clientes v0.1 ******************")
print("****************** Oscar Sorensen **************************")

clientes = []

try: ############## Ojo que igual no existe el archivo ########
    archivo = open("clientes.bin",'rb')
    clientes = pickle.load(archivo)
except:
    print("No existe archivo de datos")

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente") 
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))

    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre, apellidos, email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:", identificador)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el ID del cliente a actualizar: "))
        nombre = input("Introduce el nuevo nombre del cliente: ")
        apellidos = input("Introduce los nuevos apellidos del cliente: ")
        email = input("Introduce el nuevo email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    elif opcion == 4:
        identificador = int(input("Introduce el ID del cliente a eliminar: "))
        confirmacion = input("¿Estás seguro de que deseas eliminar este cliente? (s/n): ")
        if confirmacion == 's' or confirmacion == 'S':
            clientes.pop(identificador) #josevicente uses remove here, but pop is better for index. because we got the id.
            print("Cliente eliminado.")
        elif confirmacion == 'n' or confirmacion == 'N':
            print("Eliminación cancelada.")
        else:
            print("Opción no válida. Eliminación cancelada.")
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes,archivo)
    archivo.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/020 version gpt.py
# ====================================================

import pickle
import os

# Colores ANSI
class Colores:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"

# Clase Cliente
class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

# Banner
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colores.MAGENTA + "═══════════════════════════════════════════════════════")
    print("💼 " + Colores.BOLD + "GESTIÓN DE CLIENTES v2.0".center(47))
    print(Colores.MAGENTA + "═══════════════════════════════════════════════════════")
    print(Colores.CYAN + "👤 Desarrollado por: " + Colores.GREEN + "Oscar Sørensen")
    print(Colores.MAGENTA + "═══════════════════════════════════════════════════════" + Colores.RESET)
    print()

# Cargar datos
clientes = []
try:
    with open("clientes.bin2", "rb") as archivo:
        clientes = pickle.load(archivo)
except:
    print(Colores.YELLOW + "⚠️  No existe archivo de datos. Se creará uno nuevo." + Colores.RESET)

# Funciones
def crear_cliente():
    print(Colores.CYAN + "\n🆕 Crear nuevo cliente\n" + Colores.RESET)
    nombre = input("👉 Nombre: ")
    apellidos = input("👉 Apellidos: ")
    email = input("📧 Email: ")
    clientes.append(Cliente(nombre, apellidos, email))
    print(Colores.GREEN + "✅ Cliente añadido correctamente.\n" + Colores.RESET)

def listar_clientes():
    print(Colores.CYAN + "\n📋 Lista de clientes\n" + Colores.RESET)
    if not clientes:
        print(Colores.YELLOW + "⚠️  No hay clientes registrados.\n" + Colores.RESET)
        return
    for i, cliente in enumerate(clientes):
        print(Colores.BOLD + f"🆔 ID: {i}" + Colores.RESET)
        print(f"👤 {cliente.nombre} {cliente.apellidos}")
        print(f"📧 {cliente.email}")
        print(Colores.MAGENTA + "───────────────────────────────" + Colores.RESET)
    print()

def actualizar_cliente():
    listar_clientes()
    try:
        i = int(input("✏️  Introduce el ID del cliente a actualizar: "))
        clientes[i].nombre = input("👉 Nuevo nombre: ")
        clientes[i].apellidos = input("👉 Nuevos apellidos: ")
        clientes[i].email = input("📧 Nuevo email: ")
        print(Colores.GREEN + "✅ Cliente actualizado correctamente.\n" + Colores.RESET)
    except:
        print(Colores.RED + "❌ Error: ID no válido.\n" + Colores.RESET)

def eliminar_cliente():
    listar_clientes()
    try:
        i = int(input("🗑️  Introduce el ID del cliente a eliminar: "))
        confirm = input("⚠️  ¿Seguro que deseas eliminarlo? (s/n): ").lower()
        if confirm == 's':
            clientes.pop(i)
            print(Colores.RED + "🗑️  Cliente eliminado.\n" + Colores.RESET)
        else:
            print(Colores.YELLOW + "❎ Eliminación cancelada.\n" + Colores.RESET)
    except:
        print(Colores.RED + "❌ Error: ID no válido.\n" + Colores.RESET)

# Guardar datos
def guardar_datos():
    with open("clientes.bin2", "wb") as archivo:
        pickle.dump(clientes, archivo)

# Programa principal
while True:
    banner()
    print(Colores.BOLD + Colores.BLUE + "📌 Menú principal" + Colores.RESET)
    print(Colores.CYAN + """
1️⃣  Crear cliente
2️⃣  Listar clientes
3️⃣  Actualizar cliente
4️⃣  Eliminar cliente
5️⃣  Salir
""" + Colores.RESET)

    try:
        opcion = int(input(Colores.YELLOW + "👉 Escoge una opción: " + Colores.RESET))
    except ValueError:
        print(Colores.RED + "❌ Opción inválida.\n" + Colores.RESET)
        continue

    if opcion == 1:
        crear_cliente()
    elif opcion == 2:
        listar_clientes()
    elif opcion == 3:
        actualizar_cliente()
    elif opcion == 4:
        eliminar_cliente()
    elif opcion == 5:
        guardar_datos()
        print(Colores.GREEN + "💾 Datos guardados. ¡Hasta pronto!\n" + Colores.RESET)
        break
    else:
        print(Colores.RED + "❌ Opción no reconocida.\n" + Colores.RESET)

    input(Colores.MAGENTA + "Presiona ENTER para continuar..." + Colores.RESET)



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/001 tkinter NameSpaces.py
# ====================================================


import tkinter as tk

ventana = tk.Tk() #crea una ventana called Name Space.

tk.Button(ventana,text="Pulsame si te atreves").pack(padx=10,pady=10) #crea un boton en la ventana

ventana.mainloop() #no te salgas


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/003 tk inter command.py
# ====================================================


import tkinter as tk

def accion():
    print("Me has pulsado")

ventana = tk.Tk() #crea una ventana called Name Space.

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10) #crea un boton en la ventana

ventana.mainloop() #no te salgas


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/004 ponemos etiqueta.py
# ====================================================


import tkinter as tk

def accion():
    print("Me has pulsado")

ventana = tk.Tk() #crea una ventana called Name Space.

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10) #crea un boton en la ventana

etiqueta = tk.Label(ventana, text="Has pulsado el boton?") #crea una etiqueta
etiqueta.pack(padx=10,pady=10) #la mete en la ventana

ventana.mainloop() #no te salgas


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/006 salida pantalla.py
# ====================================================

import tkinter as tk

def accion():
   etiqueta.config(text="Me has pulsado") #cambia el texto de la etiqueta

ventana = tk.Tk() #crea una ventana called Name Space.

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10) #crea un boton en la ventana

etiqueta = tk.Label(ventana, text="Has pulsado el boton?") #crea una etiqueta
etiqueta.pack(padx=10,pady=10) #la mete en la ventana

ventana.mainloop() #no te salgas


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/007 microcalculadora.py
# ====================================================

import tkinter as tk


ventana = tk.Tk() #crea una ventana called Name Space.

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Calcular")
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado:")
resultado.pack(padx=10,pady=10)

ventana.mainloop() #no te salgas



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/008 calcular.py
# ====================================================

import tkinter as tk

def calcular():
    op1valor = int(operando1.get())
    op2valor = int(operando2.get())
    suma = op1valor + op2valor
    resultado.config(text=str(suma))

ventana = tk.Tk()

operando1 = tk.Entry()
operando1.pack(padx=10, pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10, pady=10)

boton = tk.Button(text="Calcular", command=calcular)
boton.pack(padx=10, pady=10)

resultado = tk.Label(text="Resultado:")
resultado.pack(padx=10, pady=10)

ventana.mainloop()



# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/001.marcos.py
# ====================================================

import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

tk.Label(marco,text="Introduce el nombre del cliente:").pack(padx=10, pady=10)



marco.pack(padx=10, pady=10)

ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/003 creo un entry.py
# ====================================================


import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

#using dninie, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el dninie del cliente:").pack(padx=10, pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10, pady=10)

#using nombre, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el nombre del cliente:").pack(padx=10, pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10, pady=10)

#using apellidos, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el apellidos del cliente:").pack(padx=10, pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10, pady=10)

#using email, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el email del cliente:").pack(padx=10, pady=10)
email = tk.Entry(marco)
email.pack(padx=10, pady=10)

#all of these arent actually linked to the database yet, but they will be soon i think. Right now its just for show and data.

marco.pack(padx=10, pady=10)

ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/004 creo un boton.py
# ====================================================


import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

#using dninie, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el dninie del cliente:").pack(padx=10, pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10, pady=10)

#using nombre, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el nombre del cliente:").pack(padx=10, pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10, pady=10)

#using apellidos, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el apellidos del cliente:").pack(padx=10, pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10, pady=10)

#using email, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el email del cliente:").pack(padx=10, pady=10)
email = tk.Entry(marco)
email.pack(padx=10, pady=10)

#all of these arent actually linked to the database yet, but they will be soon i think. Right now its just for show and data.

#Boton
tk.Button(marco,text="Insertar Cliente",command=insertar).pack(padx=10, pady=10)

marco.pack(padx=10, pady=10)

ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/005 funcion insertar.py
# ====================================================


import tkinter as tk

ventana = tk.Tk()

def insertar():
    print("Vamos a insertar un cliente: ")

marco = tk.Frame(ventana)

#using dninie, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el dninie del cliente:").pack(padx=10, pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10, pady=10)

#using nombre, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el nombre del cliente:").pack(padx=10, pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10, pady=10)

#using apellidos, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el apellidos del cliente:").pack(padx=10, pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10, pady=10)

#using email, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el email del cliente:").pack(padx=10, pady=10)
email = tk.Entry(marco)
email.pack(padx=10, pady=10)

#all of these arent actually linked to the database yet, but they will be soon i think. Right now its just for show and data.

#Boton
tk.Button(marco,text="Insertar Cliente",command=insertar).pack(padx=10, pady=10)

marco.pack(padx=10, pady=10)

ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/006 mysql.py
# ====================================================

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam2",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    1,
    "12345678A",
    "Jose Vicente",
    "Carratala Sanchis",
    "info@jocarsa.com"
  );
''')

conexion.commit()

cursor.close()
conexion.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/008 seleccionar.py
# ====================================================


select * from clientes;


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/009 insertar.py
# ====================================================

import tkinter as tk
import mysql.connector
conexion = mysql.connector.connect(host="localhost",user="empresadam",password="Empresadam123$",database="empresadam")
cursor = conexion.cursor()
ventana = tk.Tk()
def insertar():
  cursor.execute('''
    INSERT INTO clientes
    VALUES(
      NULL,
      "'''+dninie.get()+'''",
      "'''+nombre.get()+'''",
      "'''+apellidos.get()+'''",
      "'''+email.get()+'''"
    );
  ''')
  conexion.commit()
marco = tk.Frame(ventana)
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=10,pady=10)
marco.pack(padx=20,pady=20)
ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/010 leer de bases de daots.py
# ====================================================

import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  SELECT * FROM clientes;
''')

filas = cursor.fetchall()

for fila in filas:
  print(fila)
  
cursor.close()
conexion.close()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/011 pintamos tablas.py
# ====================================================

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()


arbol = ttk.Treeview(ventana, columns=("nombre", "apellidos"), show="headings")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")

arbol.insert("", "end", values=("Jose Vicente", "Carratala"))
arbol.insert("", "end", values=("Juan", "García Lopez"))

arbol.pack(padx=20,pady=20)

ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/012 frankenstein.py
# ====================================================

import tkinter as tk
from tkinter import ttk
import mysql.connector
conexion = mysql.connector.connect(host="localhost",user="empresadam",password="Empresadam123$",database="empresadam")
cursor = conexion.cursor()
ventana = tk.Tk()
arbol = ttk.Treeview(ventana, columns=("dninie","nombre", "apellidos","email"), show="headings")
arbol.heading("dninie", text="DNI del cliente")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")
arbol.heading("email", text="Email del cliente")
cursor.execute('''SELECT * FROM clientes;''')
filas = cursor.fetchall()
for fila in filas:
  arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))

arbol.pack(padx=20,pady=20)

ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/013 con ia.py
# ====================================================

import tkinter as tk
from tkinter import ttk
import mysql.connector
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# --- Database connection ---
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

# --- Main window setup ---
ventana = tb.Window(themename="superhero")  # try also: "minty", "flatly", "darkly"
ventana.title("Gestión de Clientes")
ventana.geometry("800x600")

# --- Frames layout ---
frame_form = ttk.LabelFrame(ventana, text="Nuevo cliente", padding=20)
frame_form.pack(fill=X, padx=20, pady=10)

frame_tabla = ttk.LabelFrame(ventana, text="Lista de clientes", padding=20)
frame_tabla.pack(fill=BOTH, expand=True, padx=20, pady=10)

# --- Form fields ---
def insertar():
    dni = dninie.get()
    nom = nombre.get()
    ape = apellidos.get()
    ema = email.get()

    if dni == "" or nom == "" or ape == "" or ema == "":
        tb.dialogs.Messagebox.show_warning("Por favor, completa todos los campos", title="Atención")
        return

    cursor.execute('''
        INSERT INTO clientes VALUES (NULL, %s, %s, %s, %s);
    ''', (dni, nom, ape, ema))
    conexion.commit()
    cargar_datos()
    tb.dialogs.Messagebox.show_info("Cliente insertado correctamente", title="Éxito")

    # Limpiar campos
    dninie.delete(0, tk.END)
    nombre.delete(0, tk.END)
    apellidos.delete(0, tk.END)
    email.delete(0, tk.END)

# Form fields (left to right layout)
ttk.Label(frame_form, text="DNI/NIE:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
dninie = ttk.Entry(frame_form, width=20)
dninie.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5, sticky=W)
nombre = ttk.Entry(frame_form, width=20)
nombre.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame_form, text="Apellidos:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
apellidos = ttk.Entry(frame_form, width=20)
apellidos.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Email:").grid(row=1, column=2, padx=5, pady=5, sticky=W)
email = ttk.Entry(frame_form, width=20)
email.grid(row=1, column=3, padx=5, pady=5)

ttk.Button(frame_form, text="Insertar cliente", command=insertar, bootstyle=SUCCESS).grid(
    row=0, column=4, rowspan=2, padx=10, pady=5, sticky=NS
)

# --- Treeview setup ---
columnas = ("dninie", "nombre", "apellidos", "email")
arbol = ttk.Treeview(frame_tabla, columns=columnas, show="headings", bootstyle=INFO)
for col in columnas:
    arbol.heading(col, text=col.capitalize())
    arbol.column(col, width=180, anchor=W)

# Scrollbars
scroll_y = ttk.Scrollbar(frame_tabla, orient=VERTICAL, command=arbol.yview)
scroll_x = ttk.Scrollbar(frame_tabla, orient=HORIZONTAL, command=arbol.xview)
arbol.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

arbol.grid(row=0, column=0, sticky=NSEW)
scroll_y.grid(row=0, column=1, sticky=NS)
scroll_x.grid(row=1, column=0, sticky=EW)

frame_tabla.rowconfigure(0, weight=1)
frame_tabla.columnconfigure(0, weight=1)

# --- Function to load data into the table ---
def cargar_datos():
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    arbol.delete(*arbol.get_children())
    for fila in filas:
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))

# --- Initial load ---
cargar_datos()

ventana.mainloop()


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/001-Identificacio╠ün de los elementos de un programa informa╠ütico/101-Ejercicio de final de unidad.py
# ====================================================

"""
En esta tarea desarrollo un programa en Python que calcula el total de una factura aplicando el IVA y un descuento fijo.
El objetivo es practicar los elementos fundamentales de un programa informático: variables, constantes, entrada de datos, operaciones aritméticas y salida de resultados.
De este modo, se aplica la lógica condicional para determinar si el descuento debe aplicarse según el valor del producto, reforzando la comprensión de estructuras básicas en Python.
El programa comienza definiendo las constantes IVA y DESCUENTO, utilizadas para calcular los importes de la factura.
A continuación, solicita al usuario el nombre del cliente y el precio bruto del producto mediante input(), convirtiendo el valor a tipo float para poder operar con él.

Después se calcula el IVA correspondiente (precio_bruto * IVA) y el subtotal con IVA.
Mediante un operador de comparación, se comprueba si el precio bruto es mayor o igual a 50 €, y se guarda el resultado en una variable booleana.
Si la condición se cumple, se aplica un descuento fijo de 10 €; en caso contrario, el descuento es 0.
Finalmente, se calcula el total a pagar y se muestran todos los datos en pantalla con formato de dos decimales.
"""


"""
Autor: Oscar Sørensen
Versión: 1.0
Descripción: Este programa calcula el total de una factura aplicando IVA (21 %)
y un descuento fijo de 10 €, solo si el precio bruto es mayor o igual a 50 €.
Archivo: factura_con_iva_descuento.py
"""

# 1. Variables y constantes
IVA = 0.21
DESCUENTO = 10.0

# 2. Entrada de datos
nombre_cliente = input("Ingrese el nombre del cliente: ")
precio_bruto = float(input("Ingrese el precio bruto del producto (€): "))

# 3. Cálculos
iva_aplicado = precio_bruto * IVA
subtotal_con_iva = precio_bruto + iva_aplicado

# Determinar si se aplica descuento
aplica_descuento = precio_bruto >= 50

if aplica_descuento:
    descuento_aplicado = DESCUENTO
else:
    descuento_aplicado = 0.0

total_a_pagar = subtotal_con_iva - descuento_aplicado

# 4. Salida de datos
print("\n--- FACTURA ---")
print("Cliente:", nombre_cliente)
print(f"Precio bruto: {precio_bruto:.2f} €")
print(f"IVA aplicado (21%): {iva_aplicado:.2f} €")
print(f"Descuento aplicado: {descuento_aplicado:.2f} €. Descuento solo aplicado si el precio sin IVA es mas que 50 €.")
print(f"Total a pagar: {total_a_pagar:.2f} €")

"""
El ejercicio permite consolidar el uso de variables, constantes y estructuras condicionales en Python.
A través de un caso práctico sencillo, demuestra cómo automatizar cálculos con IVA y descuentos, reforzando la comprensión de la estructura básica de un programa informático.
"""








# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/002-Utilizacio╠ün de objetos/005-Utilizacio╠ün de me╠ütodos esta╠üticos.py
# ====================================================

#En mi tiempo libre, disfruto mucho entrenando en el gimnasio y cocinando comidas saludables.
#Para combinar estos intereses, imagino desarrollar una pequeña aplicación de fitness que ayude a los usuarios a realizar un seguimiento de sus rutinas de entrenamiento.
#En este ejercicio, crearé un método estático que calcule la puntuación de un entrenamiento en función del número de series y repeticiones realizadas.
#Este ejemplo conecta con mis actividades personales en el gimnasio y muestra cómo se puede utilizar la programación para organizar y analizar los datos de entrenamiento de manera eficiente.

#El siguiente código define una clase llamada Entrenamiento que incluye dos propiedades estáticas:

#max_repeticiones: almacena el número máximo de repeticiones permitidas.

#factor_calidad: almacena un factor de calidad que aumenta la puntuación si las repeticiones superan el límite.

#La clase también contiene un método estático llamado calcular_calificacion, que recibe dos parámetros (series y repeticiones) y devuelve una puntuación calculada en función de los criterios dados.


class Entrenamiento:
    max_repeticiones = 18
    factor_calidad = 1.5

    @staticmethod
    def calcular_calificacion(series, repeticiones):
        if repeticiones < Entrenamiento.max_repeticiones:
            return series * repeticiones
        else:
            return (series * repeticiones) + Entrenamiento.factor_calidad

if __name__ == "__main__":
    calificacion = Entrenamiento.calcular_calificacion(4, 20)
    print("Calificación del entrenamiento:", calificacion)  # Output: Calificación del entrenamiento: 81.5

#Este ejercicio muestra cómo se pueden utilizar los métodos estáticos para agrupar operaciones lógicas dentro de una clase sin necesidad de crear objetos.
#Comprender este concepto es fundamental en la programación orientada a objetos, ya que los miembros estáticos nos permiten almacenar datos compartidos o métodos de utilidad que pertenecen a la propia clase.
#En proyectos reales, este mismo enfoque podría utilizarse para tareas como el cálculo de calorías, la puntuación de la intensidad del entrenamiento o el seguimiento del progreso, aspectos esenciales de una aplicación de seguimiento del estado físico.




# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/002-Utilizacio╠ün de objetos/101-Ejercicio de final de unidad.py
# ====================================================

#En este ejercicio desarrollo un pequeño programa en Python llamado planificador de cuadras, que calcula cuántas cuadras son necesarias para alojar a un número determinado de caballos.
#El programa solicita al usuario los datos principales (número de caballos, capacidad de cada cuadra y fecha), utiliza el módulo math para redondear al alza con ceil() y el módulo datetime para obtener propiedades de la fecha actual, como el mes, el año y el día de la semana.


import math
import datetime

horses = input("Enter the number of horses you have: ")  # input devuelve un string
if horses == "0":  # comparamos con string
    print("You have no horses, so you don't need any stables. Enter a valid number of horses next time.")
    exit()

today = datetime.date.today()
is_weekend = today.isoweekday() in (6, 7)  # 6=Saturday, 7=Sunday

todays_date = input("Enter today's date (YYYY-MM-DD) or leave blank for today: ")

capacity_per_stable = input("Enter the capacity of each stable (number of horses it can hold): ")  # input devuelve un string
stables_needed = math.ceil(int(horses) / int(capacity_per_stable))  # convertimos a int para hacer la division

print("Today's date is:", today, ".")
print("We are in month number", today.month, "of the year", today.year, ".")
print("Is today a weekend?", is_weekend)
print("You will need", stables_needed, "stables to accommodate all your horses.")
print("Each stable can hold up to", capacity_per_stable, "horses.", "You have", horses, "horses in total.")


#Este programa demuestra cómo combinar la entrada de datos con operaciones matemáticas y el manejo de fechas mediante módulos estándar de Python.
#El uso de math.ceil() permite calcular las cuadras necesarias de forma precisa, mientras que datetime.date facilita mostrar información temporal relevante.
#Gracias a estas funciones, se obtiene un informe claro y automatizado que cumple con los objetivos del ejercicio.


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/002-Utilizacio╠ün de objetos/mockExam002.py
# ====================================================

#En este ejercicio desarrollo un pequeño programa en Python llamado planificador de cuadras, que calcula cuántas cuadras son necesarias para alojar a un número determinado de caballos.
#El programa solicita al usuario los datos principales (número de caballos, capacidad de cada cuadra y fecha), utiliza el módulo math para redondear al alza con ceil() y el módulo datetime para obtener propiedades de la fecha actual, como el mes, el año y el día de la semana.

import math
import datetime

horses = input("Enter the number of horses you have: ")  # input devuelve un string
if horses == "0":  # comparamos con string
    print("You have no horses, so you don't need any stables. Enter a valid number of horses next time.")
    exit()

today = datetime.date.today()
is_weekend = today.isoweekday() in (6, 7)  # 6=Saturday, 7=Sunday

todays_date = input("Enter today's date (YYYY-MM-DD) or leave blank for today: ")

capacity_per_stable = input("Enter the capacity of each stable (number of horses it can hold): ")  # input devuelve un string
stables_needed = math.ceil(int(horses) / int(capacity_per_stable))  # convertimos a int para hacer la division

print("Today's date is:", today, ".")
print("We are in month number", today.month, "of the year", today.year, ".")
print("Is today a weekend?", is_weekend)
print("You will need", stables_needed, "stables to accommodate all your horses.")
print("Each stable can hold up to", capacity_per_stable, "horses.", "You have", horses, "horses in total.")

#Este programa demuestra cómo combinar la entrada de datos con operaciones matemáticas y el manejo de fechas mediante módulos estándar de Python.
#El uso de math.ceil() permite calcular las cuadras necesarias de forma precisa, mientras que datetime.date facilita mostrar información temporal relevante.
#Gracias a estas funciones, se obtiene un informe claro y automatizado que cumple con los objetivos del ejercicio.


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/004-Control de excepciones.py
# ====================================================



"""
En esta tarea desarrollo un programa para un entrenador fitness que necesita calcular
el promedio de los días que sus clientes han asistido al gimnasio durante el mes.
Es importante manejar excepciones, ya que puede ocurrir un error si no hay registros,
y el programa no debe interrumpirse.
"""

# Definición de variables
dias_al_gimnasio = [1, 3, 4, 0, 2]  # Ejemplo con datos

try:
    # Calcular el promedio de los días registrados
    promedio_dias = sum(dias_al_gimnasio) / len(dias_al_gimnasio)
except ZeroDivisionError:
    # Si la lista está vacía, no se puede dividir entre cero
    promedio_dias = "No hay datos disponibles"

# Salida del resultado
print("Promedio de días al gimnasio:", promedio_dias)

"""
Este ejercicio demuestra la importancia de manejar excepciones como ZeroDivisionError
para evitar que un programa se detenga ante errores comunes. En este caso,
se aplican los conceptos de control de excepciones aprendidos en la unidad,
asegurando que el programa sea más estable y confiable.
"""



# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/005-Aserciones.py
# ====================================================



En esta tarea, practico el uso de aserciones en Python como una forma de validar condiciones lógicas dentro de un programa.
Las aserciones actúan como puntos de control automáticos que verifican si ciertas reglas son ciertas antes de que el programa continúe ejecutándose.
Si una condición falla, Python detiene inmediatamente el programa y muestra un mensaje de error, lo que ayuda al desarrollador a detectar errores de forma temprana.
Con pequeños ejemplos relacionados con la edad, el peso y los niveles de experiencia de los jugadores, esta actividad demuestra cómo se pueden utilizar las aserciones para garantizar que los valores de los datos cumplan requisitos específicos.
Al aprender a utilizar assert, refuerzo mi comprensión de los mecanismos de control y validación en Python, mejorando tanto la fiabilidad como la calidad de mi código.


edad_usuario = 23; # Edad del usuario
assert edad_usuario >= 18, ("Debes ser mayor de edad para entrar") # Aserción: verifica si la edad es mayor o igual a 18
print("Puedes entrar al club") # Mensaje si la aserción es verdadera


peso_usuario = 70; # Peso del usuario en kg
assert peso_usuario >= 50, ("Debes pesar al menos 50 kg para cocinar conmigo") # Aserción: verifica si el peso es mayor o igual a 50
print("Puedes participar en la competencia") # Mensaje si la aserción es verdadera



nivel_jugador = 88; # Nivel del jugador en el juego
assert nivel_jugador >= 10, "No tienes suficiente nivel para continuar" # Aserción: verifica si el nivel es mayor o igual a 10
print("Puedes continuar el juego.") # Mensaje si la aserción es verdadera

En esta tarea, practiqué la validación de diferentes condiciones en Python, como la edad, el peso y el nivel de experiencia.
Estos pequeños programas me ayudaron a comprender cómo detener la ejecución cuando no se cumplen ciertos requisitos.
En la vida real, se puede utilizar una lógica similar para comprobar la información introducida por el usuario en las aplicaciones, por ejemplo, verificando la edad antes de crear una cuenta o confirmando la elegibilidad en un juego o una aplicación de fitness.


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/006-Prueba, depuracio╠ün y documentacio╠ün.py
# ====================================================

#En este ejercicio trabajo con el manejo de errores y la depuración de código en Python.
#El objetivo de mi programa es crear una función llamada divide() que reciba dos parámetros, dividendo y divisor, y devuelva el resultado de dividirlos.
#A través de este ejercicio practico el uso de los bloques try y except, que permiten controlar errores sin que el programa se detenga.
#Este tipo de control es muy útil cuando los datos provienen del usuario, ya que evita fallos inesperados y mejora la fiabilidad del programa.

def divide(dividendo, divisor):
    try:
        dividendo = int(dividendo)
        divisor = int(divisor)

        if divisor != 0:
            return dividendo / divisor
        else:
            return False  # Indica error por división entre cero

    except ValueError:
        return "Error: No se puede dividir por texto"


for dividendo in range(-100, 100):
    for divisor in range(-100, 100):
        print(divide(dividendo, divisor))

print(divide(4, "a"))

#La función divide() que he desarrollado cumple con los requisitos del enunciado: convierte los valores a enteros, devuelve False si el divisor es cero y muestra un mensaje claro cuando el dato no es numérico.
#Gracias a esta práctica he entendido mejor cómo manejar excepciones y comprobar errores en Python, algo esencial para escribir código estable y fácil de depurar.
#El ejercicio me ha ayudado a ver la importancia de validar los datos antes de realizar operaciones como la división.


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/101-Ejercicio de final de unidad.py
# ====================================================

#En este ejercicio desarrollo un programa en Python llamado adivina.py, cuyo objetivo es crear un juego interactivo de adivinanza.
#El programa genera un número secreto entre 1 y 50 utilizando el módulo random y permite al usuario intentar descubrirlo en un máximo de seis intentos.
#Durante el proceso se aplican estructuras condicionales (if/elif/else), bucles while, manejo de errores con try/except, control de flujo con break y continue, y el uso de aserciones para garantizar condiciones invariantes.



import random

def guess_the_number():
    print("Welcome to the Guess the Number Game! You have 6 attempts to guess the secret number between 1 and 50.")
    secret_number = random.randint(1, 50)
    max_attempts = 6
    used_attempts = 0
    print("Debug: The secret number is", secret_number)  # For testing purposes, remove in production
    assert 1 <= secret_number <= 50, "Secret number is out of bounds!"

    while used_attempts < max_attempts:
        try: 
            entry = input("Attempt " + str(used_attempts + 1) + ": Enter your guess: ")
            guess = int(entry)
            
            if guess < 1 or guess > 50:
                print("Your guess must be between 1 and 50. Please try again.")
                continue

            used_attempts += 1

            if guess == secret_number:
                print("Congratulations! You've guessed the secret number:", secret_number)
                break   
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            
            if used_attempts == 3 and guess != secret_number:
                print("Hint: The secret number is", "even." if secret_number % 2 == 0 else "odd.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    if used_attempts == max_attempts:
        print("Sorry, you've used all your attempts. The secret number was:", secret_number)

if __name__ == "__main__":
    guess_the_number()


#Este programa demuestra cómo combinar estructuras de control, validación de datos y manejo de excepciones en un contexto práctico y lúdico.
#Las aserciones garantizan que el número secreto y el contador de intentos se mantengan dentro de los límites establecidos, mientras que el uso de try/except evita errores por entradas no numéricas.
#Gracias a esta implementación, se cumple el objetivo de crear un juego funcional que refuerza los fundamentos de la programación estructurada en Python.


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/mockExam003.py
# ====================================================

#En este ejercicio desarrollo un programa en Python llamado adivina.py, cuyo objetivo es crear un juego interactivo de adivinanza.
#El programa genera un número secreto entre 1 y 50 utilizando el módulo random y permite al usuario intentar descubrirlo en un máximo de seis intentos.
#Durante el proceso se aplican estructuras condicionales (if/elif/else), bucles while, manejo de errores con try/except, control de flujo con break y continue, y el uso de aserciones para garantizar condiciones invariantes.

import random

def guess_the_number():
    print("Welcome to the Guess the Number Game! You have 6 attempts to guess the secret number between 1 and 50.")
    secret_number = random.randint(1, 50)
    max_attempts = 6
    used_attempts = 0
    print("Debug: The secret number is", secret_number)  # For testing purposes, remove in production
    assert 1 <= secret_number <= 50, "Secret number is out of bounds!"

    while used_attempts < max_attempts:
        try: 
            entry = input("Attempt " + str(used_attempts + 1) + ": Enter your guess: ")
            guess = int(entry)
            
            if guess < 1 or guess > 50:
                print("Your guess must be between 1 and 50. Please try again.")
                continue

            used_attempts += 1

            if guess == secret_number:
                print("Congratulations! You've guessed the secret number:", secret_number)
                break   
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            
            if used_attempts == 3 and guess != secret_number:
                print("Hint: The secret number is", "even." if secret_number % 2 == 0 else "odd.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    if used_attempts == max_attempts:
        print("Sorry, you've used all your attempts. The secret number was:", secret_number)

if __name__ == "__main__":
    guess_the_number()


#Este programa demuestra cómo combinar estructuras de control, validación de datos y manejo de excepciones en un contexto práctico y lúdico.
#Las aserciones garantizan que el número secreto y el contador de intentos se mantengan dentro de los límites establecidos, mientras que el uso de try/except evita errores por entradas no numéricas.
#Gracias a esta implementación, se cumple el objetivo de crear un juego funcional que refuerza los fundamentos de la programación estructurada en Python.


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/001-Concepto de clase.py
# ====================================================

"""
En la vida diaria, las clases en programación permiten representar objetos del mundo real. En este caso, la clase Gato refleja cómo puedo organizar información, igual que cuando gestiono mis actividades o pasatiempos como cocinar o entrenar.

Defino la clase Gato con el método __init__() y los atributos nombre y color.
Luego creo dos objetos, Garfield y Gustavo, asignándoles sus respectivos colores y mostrando su estado antes y después de la modificación.
"""

class Gato():
    def __init__(self):
        self.color = ""
        self.nombre = ""

# Crear los gatos (instancias)
gato1 = Gato()
gato2 = Gato()

# Imprimir estado inicial
print("Estado inicial:")
print("Gato 1:", gato1.nombre, gato1.color)
print("Gato 2:", gato2.nombre, gato2.color)

# Modificar atributos
gato1.nombre = "Garfield"
gato1.color = "naranja"
gato2.nombre = "Gustavo"
gato2.color = "blanco"

# Imprimir estado modificado
print("Estado modificado:")
print("Gato 1:", gato1.nombre, gato1.color)
print("Gato 2:", gato2.nombre, gato2.color)

"""
Este ejercicio demuestra cómo los objetos pueden almacenar y cambiar información, igual que en una aplicación real que gestiona mis rutinas o preferencias. Aprender a crear clases me ayuda a estructurar datos de forma lógica y reutilizable.
"""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/002-Estructura y miembros de una clase.py
# ====================================================


"""
Las clases en programación permiten organizar información y comportamientos dentro de una misma estructura. En este tema aprendo a representar objetos del mundo real —como clientes o cuentas bancarias— y a gestionarlos mediante propiedades y métodos, igual que en una aplicación real de gestión personal o profesional.

Defino varias clases (Client, BankAccount) con el método __init__() y atributos bien estructurados.
Implemento métodos que modifican y muestran la información (show_info, deposit, withdraw, get_balance, set_balance), aplicando el principio de encapsulación y un menú CRUD básico para practicar la manipulación de objetos.
"""

# Defino la clase Cliente (necesario antes de usar Cliente())
class Cliente:
    def __init__(self):
        self.nombre = ""
        self.email = ""
        self.direccion = ""


print("Programa de gestion de clientes c0.1 Oscar Sorensen")
print("1. Insertar un cliente")
print("2. Listar clientes")
print("3. Actualizar cliente")
print("4. Eliminar cliente")
print("5. Salir")

clientes = []  # creo una lista VACÍA

while True:  # Esto desata un bucle infinito pero controlado

    opcion = input("Escoge una opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        print("Vamos a insertar un cliente")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        clientes.append(nuevocliente)
        print("Cliente insertado correctamente")

    elif opcion == 2:
        print("Vamos a ver los clientes")
        for cliente in clientes:
            print(cliente.nombre, cliente.email, cliente.direccion)

    elif opcion == 3:
        print("Vamos a actualizar un cliente")
        nombreabuscar = input("Introduce el nombre del cliente a actualizar: ")
        for cliente in clientes:
            if cliente.nombre == nombreabuscar:
                cliente.email = input("Nuevo email: ")
                cliente.direccion = input("Nueva direccion: ")
                print("Cliente actualizado correctamente")

    elif opcion == 4:
        print("Vamos a eliminar un cliente")
        nombreabuscar = input("Introduce el nombre del cliente a eliminar: ")
        for cliente in clientes:
            if cliente.nombre == nombreabuscar:
                clientes.remove(cliente)
                print("Cliente eliminado correctamente")

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta otra vez")


"""
Este ejercicio demuestra cómo las clases permiten unir datos y acciones en un solo bloque lógico.
Gracias a ello puedo crear aplicaciones más organizadas y reutilizables, comprendiendo cómo la programación orientada a objetos se aplica a casos reales como la gestión de clientes o cuentas.
Del mismo modo, podría aplicar estos conceptos para desarrollar una aplicación que gestione mis rutinas de gimnasio o mis recetas de cocina, almacenando información y operaciones de forma estructurada y eficiente.
"""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/003-Creacio╠ün de propiedades.py
# ====================================================

"""
En la vida cotidiana, la programación puede ayudarnos a organizar información sobre nuestras actividades,
como cocinar o entrenar en el gimnasio. En este ejercicio aplico la programación orientada a objetos
para gestionar productos, lo que podría servir para registrar ingredientes, suplementos o materiales deportivos.
"""

# Definición de la clase Producto
class Producto:
    def __init__(self):
        self.nombre = ""
        self.precio = 0.0
        self.categoria = []  # lista (array) de categorías

# Instanciación del objeto
producto1 = Producto()

# Asignación de valores a las propiedades
producto1.nombre = "Proteina Whey"
producto1.precio = 15
producto1.categoria = ["Suplemento", "Gimnasio", "Nutricion"]

# Mostrar información del producto
print("Información del producto:")
print("Nombre:", producto1.nombre)
print("Precio:", producto1.precio, "€")
print("Categorías:", producto1.categoria)

"""
Este ejercicio demuestra cómo una clase puede representar objetos reales,
en este caso productos relacionados con la cocina o el gimnasio.
A través de la instanciación y asignación de propiedades,
aprendo a modelar información que podría utilizar en aplicaciones prácticas,
como un sistema personal de control de ingredientes o suplementos.
"""



# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/004-Creacio╠ün de me╠ütodos.py
# ====================================================


"""
Introducción y contextualización
En este ejercicio aplico los conceptos de clases, constructores y métodos getter y setter
para crear un sistema sencillo de gestión de clientes en una tienda virtual de ropa.
Como me gusta ir al gimnasio, he incluido un método adicional que determina si un cliente
es frecuente, igual que un entrenador evalúa la constancia de sus alumnos.


La clase Cliente utiliza atributos privados (__nombrecompleto, __email y __compras)
para mantener la información encapsulada y evitar accesos directos desde fuera.
Los métodos setter permiten asignar valores a esos atributos, mientras que los getter
devuelven su contenido. Además, se define un método adicional llamado esFrecuente()
que devuelve True si el cliente ha realizado más de 5 compras, y False en caso contrario.
"""


class Cliente:
    def __init__(self):
        self.__nombrecompleto = ""
        self.__email = ""
        self.__compras = 0

    # Setters
    def setNombreCompleto(self, nuevo_nombre):
        self.__nombrecompleto = nuevo_nombre

    def setEmail(self, nuevo_email):
        self.__email = nuevo_email

    def setCompras(self, numero_compras):
        self.__compras = numero_compras

    # Getters
    def getNombreCompleto(self):
        return self.__nombrecompleto

    def getEmail(self):
        return self.__email

    # Método adicional
    def esFrecuente(self):
        return self.__compras > 5


# Ejemplo de uso
cliente1 = Cliente()
cliente1.setNombreCompleto("Oscar Sørensen")
cliente1.setEmail("oscar@example.com")
cliente1.setCompras(7)

print("Nombre completo:", cliente1.getNombreCompleto())
print("Email:", cliente1.getEmail())

if cliente1.esFrecuente():
    print("El cliente es frecuente en la tienda.")
else:
    print("El cliente no es frecuente aún.")

"""
En este ejercicio he aprendido a utilizar clases con encapsulación, métodos getter y setter,
y a implementar un método adicional para evaluar el comportamiento de un cliente.
Este tipo de estructura puede aplicarse fácilmente en sistemas reales de gestión de tiendas,
donde se necesita controlar la información privada y analizar la fidelidad de los clientes.
"""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/005-Creacio╠ün de constructores.py
# ====================================================

"""En este ejercicio, utilizo constructores en Python para crear una clase que muestra una situación real: el registro de clientes de un gimnasio.
Este contexto conecta directamente con uno de mis propios pasatiempos, ir al gimnasio, y me permite comprender cómo la programación orientada a objetos puede ayudar a gestionar información del mundo real.
Al crear una clase Cliente, los datos de cada cliente (nombre, apellidos, correo electrónico y dirección) se pueden organizar y reutilizar de manera eficiente dentro de un programa.
"""

"""La clase Cliente incluye un método constructor __init__, que se ejecuta automáticamente cuando se crea un nuevo objeto.
Este constructor inicializa los cuatro atributos: nombre, apellido, correo electrónico y dirección.
El método show_info imprime la información completa del cliente en la pantalla.

Para probar la clase, el programa solicita al usuario que introduzca los cuatro datos.
A continuación, se crea un nuevo objeto Cliente con estos valores y se almacena en una lista llamada clientes.
Por último, la función list_clientes() recorre la lista e imprime los datos de cada cliente, confirmando que el constructor ha inicializado correctamente el objeto.
"""

"""
Programa: ClienteGimnasio
Versión: 0.1
Autor: Oscar Sorensen
Descripción: Creación de una clase Cliente con un constructor para inicializar los atributos del cliente.
"""

class Cliente:
    def __init__(self, nombre, apellido, email, direccion):   # (constructor)
        self.nombre = nombre               # property (propiedad)
        self.apellido = apellido            # property (propiedad)
        self.email = email                  # property (propiedad)
        self.direccion = direccion          # property (propiedad)

    def show_info(self):                    # method (método)
        print(f"Cliente: {self.nombre}, Apellido: {self.apellido}, "
              f"Email: {self.email}, Dirección: {self.direccion}")


clients = []  # lista global para guardar objetos

def insert_client():
    nombre = input("Name: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    direccion = input("Direccion: ")
    clients.append(Cliente(nombre, apellido, email, direccion))
    print("Inserted.")

def list_clients():
    if len(clients) == 0:
        print("No clients yet.")
        return
    i = 1
    for c in clients:
        print(f"Cliente(nombre='{c.nombre}', apellidos='{c.apellido}', email='{c.email}', direccion='{c.direccion}')")  
        i = i + 1

insert_client()
list_clients()


"""Esta tarea muestra cómo los constructores facilitan la creación e inicialización automática de objetos, garantizando que cada instancia cuente con los atributos necesarios desde el principio.
Mediante el uso de esta estructura, es posible gestionar los datos de los clientes de forma clara y eficiente, un principio que se aplica no solo a este ejemplo, sino a cualquier sistema futuro que almacene y organice información utilizando clases.
"""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/006-Utilizacio╠ün de clases y objetos.py
# ====================================================

"""En esta actividad aplico el concepto de métodos dentro de una clase en Python para realizar operaciones matemáticas básicas.
He creado una clase llamada Matematicas que representa una herramienta sencilla para redondear números, lo cual resulta útil en muchas situaciones cotidianas, como calcular precios, medidas o resultados con decimales.
Este ejercicio me permite relacionar la programación con operaciones matemáticas reales y comprender cómo organizar funciones dentro de una misma clase.
"""

"""La clase Matematicas incluye un constructor __init__() que inicializa el atributo PI, demostrando cómo definir valores internos en una clase.
Dentro de la clase se implementan tres métodos principales:

redondeo(numero): calcula la parte entera y la parte decimal del número. Si el decimal es menor que 0.5, el método devuelve el número redondeado hacia abajo; si es mayor o igual, lo redondea hacia arriba.

techo(numero): devuelve el número redondeado hacia arriba (al siguiente entero) siempre que tenga una parte decimal.

suelo(numero): realiza un redondeo real hacia abajo, incluso con números negativos. Para lograrlo, comprueba si el número es menor que cero y tiene parte decimal, restando uno al valor entero para obtener el resultado correcto.

Cada método utiliza estructuras condicionales if/else para decidir la operación a realizar, sin emplear librerías externas.
Finalmente, se crea un objeto mate = Matematicas() y se prueban los tres métodos con varios valores positivos y negativos, mostrando los resultados en pantalla."""

"""
Programa: RedondeosAlzaBaja
Versión: 0.1
Autor: Oscar Sorensen
Descripción: Implementación de una clase Matematicas para realizar redondeos hacia alza y baja sin usar la librería estándar de Python.
"""

class Matematicas: # Clase para operaciones matemáticas básicas
    def __init__(self):          # Constructor
        self.PI = 3.14159265359

    def redondeo(self, numero): #metodo de redondeo al entero más cercano
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            return entero            # baja
        else:
            return entero + 1        # alza

    def techo(self, numero): # método de redondeo hacia arriba
        entero = int(numero)
        decimal = numero - entero
        if decimal == 0:
            return entero            # ya es entero
        else:
            return entero + 1        # redondeo hacia arriba

    def suelo(self, numero):
        entero = int(numero)
        if numero < 0 and numero != entero:
            return entero - 1   # adjust for negatives
        else:
            return entero



# Pruebas
mate = Matematicas()
print("redondeo(4.7) : ", mate.redondeo(4.7))   
print("redondeo(4.2) : ", mate.redondeo(4.2))   
print("techo(4.2) : ", mate.techo(4.2))      
print("suelo(4.7) : ", mate.suelo(4.7))      


"""Con este ejercicio comprendí cómo definir varios métodos dentro de una misma clase y cómo aplicar condiciones lógicas para controlar su comportamiento.
En especial, el método suelo() me permitió entender la diferencia entre truncar y redondear hacia abajo, algo esencial al trabajar con números negativos.
El uso de clases como Matematicas facilita mantener las funciones organizadas y reutilizables, aplicando los principios básicos de la programación orientada a objetos de forma práctica y estructurada."""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/007-Utilizacio╠ün de clases heredadas.py
# ====================================================



"""
En este ejercicio aplico el concepto de herencia en Python para representar diferentes tipos
de animales dentro de un sistema estructurado. La herencia permite crear clases que comparten
características comunes, reduciendo la repetición de código y facilitando la organización.
Defino una clase base "Animal" con los atributos edad, nombre y raza. Las subclases "Gato"
y "Perro" heredan estos atributos y añaden métodos específicos para mostrar el nombre de cada
animal. Cada constructor utiliza "super().__init__()" para invocar el constructor de la clase
superior y asegurar que los atributos se inicialicen correctamente.
Este enfoque puede aplicarse en cualquier programa que necesite modelar entidades relacionadas
de forma jerárquica y reutilizable.
"""

class Animal:
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""

class Gato(Animal):
    def __init__(self):
        super().__init__()
    def mostrarNombre(self):
        print("El gato se llama", self.nombre)

class Perro(Animal):
    def __init__(self):
        super().__init__()
    def mostrarNombre(self):
        print("El perro se llama", self.nombre)

# Ejemplo de uso
gato1 = Gato()
gato1.nombre = "Garfield"
gato1.mostrarNombre()

perro1 = Perro()
perro1.nombre = "Havana"
perro1.mostrarNombre()


"""
Con este ejercicio he aprendido a utilizar la herencia para crear clases más organizadas y reutilizables. Este concepto puede aplicarse en proyectos más grandes, como aplicaciones que gestionen rutinas de entrenamiento o recetas de cocina.
"""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/004-Desarrollo de clases/UnitExam.py
# ====================================================

"""En este ejercicio aplico el concepto de los métodos set y get dentro de una clase en Python para realizar operaciones básicas de modificación y consulta de datos.
He creado una clase llamada Cliente que representa a una persona con propiedades como nombre, apellidos, dirección y correo electrónico.
Este ejemplo permite relacionar la programación con situaciones del mundo real, donde los datos personales pueden cambiar y deben actualizarse de forma controlada.

La clase Cliente incluye un constructor `` __init__()`` con cuatro propiedades, junto con dos métodos: set_email() y get_email(), tal como indica el enunciado.
Posteriormente, he creado tres instancias de la clase —cliente1, cliente2 y cliente3—, cada una con sus propios valores.
Para demostrar el funcionamiento de los métodos, utilicé set_email() para modificar el correo electrónico de cada cliente y después get_email() para mostrar el nuevo valor y comprobar que el cambio se aplicó correctamente.
Estos métodos permiten acceder y modificar los datos de manera segura, respetando el principio de encapsulación dentro de la programación orientada a objetos.

````
"""
class Client:
    def __init__(self, nombre, apellido, direccion, email):   # (constructor)
        self.nombre = nombre               # property (propiedad)
        self.email = email             # property (propiedad)
        self.apellido = apellido
        self.direccion = direccion
        
    def get_email(self):               # method (método)
        return self.email
    
    def set_email(self, new_email):
        self.email = new_email

#Creamos tres instancias de la clase Client
cliente1 = Client("Oscar", "Sorensen", "calle Maximilia", "oscar@gmail.com")
cliente2 = Client("Sofia", "Sorensen", "Calle Madrid", "sofia@gmail.com")
cliente3 = Client("Jose", "Vicente", "noclue 123", "jose@gmail.com")

#Demostramos que los métodos set y get funcionan para cada una de las instancias
cliente1.set_email("oscarnewemail@gmail.com")
print("Cliente 1 new email:", cliente1.get_email())
cliente2.set_email("sofianewemail")
print("Cliente 2 new nombre:", cliente2.get_email())
cliente3.set_email("josevicentenewemail")
print("Cliente 3 new calle:", cliente3.get_email())
""""
````
Con esta actividad he practicado el uso de los métodos set y get dentro de una clase y su aplicación sobre propiedades específicas.
Estos métodos facilitan la modificación y lectura de los datos de los objetos de forma estructurada, aplicando los principios básicos de la programación orientada a objetos, como la organización, la reutilización del código y la claridad en el diseño.
"""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/001-Flujos. Tipos bytes y caracteres.py
# ====================================================


"""
En este ejercicio aplico los conceptos de lectura y escritura de archivos en Python.
La idea es crear una pequeña agenda digital para guardar nombres y correos electrónicos.
Esto me permite practicar la persistencia de datos y la manipulación básica de archivos.
"""

# Escribir un nuevo contacto
with open("agenda.txt", "a", encoding="utf-8") as archivo:
    archivo.write(input("Introduce el nombre del contacto: ") + "," +
                  input("Introduce el email del contacto: ") + "\n")

print("\nContacto guardado correctamente.\n")

# Leer y mostrar todos los contactos
print("Contactos guardados en la agenda:")
with open("agenda.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, email = linea.strip().split(",")
        print("Nombre:", nombre, "| Email:", email)

"""
Con este ejercicio he aprendido a leer y escribir información en archivos de texto,
guardando los datos de forma permanente. Comprendo cómo estas técnicas pueden aplicarse
en programas reales que necesiten registrar información de contactos, rutinas o recetas.
"""



# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/002-ficheros de datos/leer_blog.py
# ====================================================

"""En esta actividad aplico los conocimientos de lectura y escritura de información en Python utilizando el formato JSON para los datos y HTML para la presentación.
El contexto se centra en José Vicente, un programador al que le apasiona el gimnasio y la cocina saludable, que desea crear un blog sencillo donde compartir sus recetas y rutinas de entrenamiento.
A través de este ejercicio aprendo a conectar el manejo de ficheros con una aplicación práctica cercana a la programación web, transformando datos estructurados en una página visible en el navegador."""

"""El programa utiliza la librería estándar json para abrir y cargar el archivo blog.json mediante json.load(), convirtiendo su contenido en una lista de diccionarios.
Después, el script abre el archivo blog.html en modo escritura y genera la estructura completa de una página web con etiquetas HTML básicas.
Dentro del cuerpo de la página se recorre la lista contenido_blog con un bucle for, escribiendo para cada artículo su título, fecha, autor y contenido dentro de un bloque <article>.
El código finaliza cerrando correctamente el fichero y mostrando un mensaje de confirmación en la consola."""

import json

archivo_json = "blog.json" #this file is in "La Raiz del proyecto"
archivo_html = "blog.html" #this file is in  "La Raiz del proyecto"
contenido_blog = []

# Read JSON
f = open(archivo_json, "r", encoding="utf-8") # Open JSON file for reading. UTF-8 encoding to support special characters
contenido_blog = json.load(f) # Loading JSON content into the Python object
f.close()

# Writing HTML
f = open(archivo_html, "w", encoding="utf-8")

f.write("<!doctype html>\n")
f.write("<html lang='es'>\n")
f.write("  <head>\n")
f.write("    <title>JOCARSAblog</title>\n")
f.write("    <meta charset='utf-8'>\n")
f.write("    <style>\n")
f.write("      body{background:steelblue;color:steelblue;font-family:sans-serif;}\n")
f.write("    </style>\n")
f.write("  </head>\n")
f.write("  <body>\n")
f.write("    <header><h1>JOCARSAblog</h1></header>\n")
f.write("    <main>\n")

for articulo in contenido_blog: # Loop through articles
    f.write("      <article>\n")
    f.write("        <h2>" + articulo["titulo"] + "</h2>\n")
    f.write("        <p><em>" + articulo["fecha"] + " - " + articulo["autor"] + "</em></p>\n")
    f.write("        <p>" + articulo["contenido"] + "</p>\n")
    f.write("      </article>\n")

f.write("    </main>\n")
f.write("    <footer>(c)2025 Jose Vicente Carratalá</footer>\n")
f.write("  </body>\n")
f.write("</html>\n")
f.close()

print("Blog generado correctamente.")


"""Con este ejercicio he aprendido a leer información estructurada desde un archivo JSON y a transformarla en contenido HTML mediante la escritura de ficheros en Python.
Este proceso me ayuda a comprender cómo se combinan los datos y la presentación dentro de un mismo proyecto, un concepto que será fundamental para desarrollar aplicaciones web más completas en el Proyecto Intermodular, como un blog o gestor de contenidos personales."""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/003-Apertura y cierre de ficheros.py
# ====================================================

"""En esta actividad pongo en práctica los conceptos básicos del manejo de ficheros en Python. He aprendido a abrir, escribir, añadir y leer información utilizando diferentes modos de acceso. El ejercicio se basa en Antonio, un aficionado al fitness que quiere registrar sus comidas y entrenamientos en una aplicación personal. A través de este contexto, la actividad muestra cómo se puede guardar y consultar información más adelante, una habilidad fundamental en proyectos reales que necesitan almacenar datos de forma permanente."""

"""Python ofrece la función open() para trabajar con ficheros. Esta función recibe el nombre del fichero y el modo de acceso, que define cómo se va a utilizar. Los modos más comunes son "w" para escribir y crear un nuevo archivo o reemplazar uno existente, "a" para añadir información al final del fichero y "r" para leer su contenido. Una vez abierto el fichero, el programa puede escribir o leer datos, y siempre debe cerrarse con close() para liberar recursos y asegurar que la información se guarde correctamente.

El ejercicio también introduce la librería pickle, que permite guardar y cargar objetos completos de Python en formato binario. Esto hace posible almacenar datos estructurados, como los entrenamientos de Antonio, para poder recuperarlos y mostrarlos más adelante."""

import pickle

# Crear fichero, escribir y leer datos
f = open("comidas.txt", "w") # Modo escritura (write) (w)
f.write("Alimento cocinado: Pizza\n") #\n para salto de línea
f.close() # Cerrar fichero después de escribir. Esto es importante

# Anado una línea más, Hamburguesa
f = open("comidas.txt", "a") # Modo añadir (append) (a)
f.write("Alimento cocinado: Hamburguesa\n")
f.close() 

# Leer el fichero y mostrar la última línea
f = open("comidas.txt", "r") # Modo lectura (read) (r)
for linea in f: 
    ultima = linea
f.close()
print("Último alimento cocinado:", ultima) # Mostrar última línea, con loop


#### segunda parte (4): uso de pickle para guardar objetos ####

# Guardar y recuperar objeto con pickle
class Entrenamiento:
    def __init__(self):
        self.ejercicio = "weightlifting"
        self.duracion = 90   # minutos

# Guardar objeto en fichero binario
archivo = open("entrenamiento.bin", "wb")
pickle.dump(Entrenamiento(), archivo)
archivo.close()

# Recuperar y mostrar objeto
archivo = open("entrenamiento.bin", "rb")
obj = pickle.load(archivo) # Recuperar objeto
archivo.close()

print("Entrenamiento recuperado:")
print("Ejercicio:", obj.ejercicio)
print("Duración:", obj.duracion, "minutos")


"""Este ejercicio me ha ayudado a comprender cómo utilizar los modos de escritura, añadido y lectura en Python para gestionar ficheros de texto, y cómo emplear la librería pickle para guardar objetos en ficheros binarios. Estas técnicas son esenciales para mantener la información disponible entre sesiones y constituyen la base del desarrollo de aplicaciones más avanzadas que gestionan datos de usuario, como el registro de comidas y entrenamientos de Antonio."""


# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/004-Utilizacio╠ün de los sistemas de ficheros.py
# ====================================================

"""
En este ejercicio aplico los conceptos de manejo de archivos y directorios en Python.
El objetivo es calcular el tamaño total de una carpeta y encontrar los archivos que 
ocupan más de un gigabyte. Esto me permite practicar el uso del módulo 'os' y las 
funciones listdir(), walk() y getsize().
"""

import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

suma = 0

for elemento in elementos:
  ruta = os.path.join(carpeta, elemento)
  suma += os.path.getsize(ruta)

print("La carpeta ocupa:")
print(suma/(1024*1024),"MB")

import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024 # 1 giga

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if os.path.getsize(ruta) > grande:
              print(ruta,os.path.getsize(ruta)/(1024*1024),"MB")
        except:
            pass


"""
Con este ejercicio he aprendido a recorrer carpetas con Python, calcular su tamaño
y detectar archivos grandes. Estos conocimientos pueden aplicarse en programas de 
mantenimiento o limpieza del sistema.
"""



# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/005-Creacio╠ün y eliminacio╠ün de ficheros y directorios.py
# ====================================================

"""
En este ejercicio aplico los conceptos de creación, eliminación y compresión de archivos en Python.
El objetivo es practicar el uso de las funciones open(), remove() y la clase ZipFile del módulo zipfile.
Estas operaciones son fundamentales para gestionar y empaquetar información dentro del sistema de archivos.
"""

import os
import zipfile

##parte 1 - creación y eliminación de archivos
with open("miarchivo.txt", "w", encoding="utf-8") as f: # Crear y escribir en un archivo
    f.write("Este es un archivo de prueba.")

print("Archivo 'miarchivo.txt' creado correctamente.")

os.remove("miarchivo.txt")
print("Archivo 'miarchivo.txt' eliminado correctamente.")



##parte 2 - compresión de archivos

origen = "crmca_crmcapitol (1).sql"   # archivo que quiero comprimir
destino = "basededatos.zip"           # nombre del archivo comprimido

with zipfile.ZipFile(destino, "w") as archivo_zip:
    archivo_zip.write(origen, arcname=os.path.basename(origen))

print(f"Archivo '{origen}' comprimido correctamente en '{destino}'.")
os.remove(origen)
print(f"Archivo original '{origen}' eliminado.")




"""
Con este ejercicio he aprendido a crear, escribir, eliminar y comprimir archivos con Python.
Comprendo cómo el módulo zipfile permite agrupar y reducir el tamaño de los datos, y cómo
las funciones open() y remove() me ayudan a gestionar el sistema de archivos de forma segura.
"""



# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/007-Interfaces gra╠üficas.py
# ====================================================

"""
Simple fitness GUI with visible Entry boxes
"""

import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

def calcular():
    try:
        valor1 = entrada1.get()
        valor2 = entrada2.get()

        if valor1 == "" or valor2 == "":
            resultado.config(text="Por favor rellena ambos campos.")
        else:
            total = int(valor1) + int(valor2)
            resultado.config(text="Total de actividad: " + str(total))
    except ValueError:
        resultado.config(text="Introduce solo números.")

ventana = tk.Tk()
ventana.title("App Fitness")
ventana.geometry("300x250")  # force a clear window size

# Campo 1
label1 = tk.Label(ventana, text="Minutos en el gimnasio:")
label1.pack(pady=(15, 5))
entrada1 = tk.Entry(ventana, width=25, bg="white", borderwidth=2)
entrada1.pack(pady=5)

# Campo 2
label2 = tk.Label(ventana, text="Kilómetros corridos:")
label2.pack(pady=5)
entrada2 = tk.Entry(ventana, width=25, bg="white", borderwidth=2)
entrada2.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="Total de actividad: ")
resultado.pack(pady=10)

ventana.mainloop()




# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/008-Concepto de evento.py
# ====================================================




# ====================================================
# Contenido original de: Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/unitExam.py
# ====================================================

""""
En este ejercicio he creado una miniaplicación CRUD en Python utilizando la librería pickle para guardar y recuperar datos de forma persistente.
Aplico los conceptos de clases y propiedades, evitando el uso de métodos, y empleo un bucle while True junto con estructuras condicionales if/elif para construir un menú interactivo en la terminal.
Todo esto me permite crear, leer, actualizar y eliminar datos de clientes dentro de una clase, relacionando la programación con una situación real, donde la información personal puede cambiar y debe actualizarse de manera controlada.

Comencé definiendo una clase llamada Cliente, que representa a una persona y contiene tres propiedades vacías: nombre, email y dirección.
A continuación, añadí varias líneas print() para mostrar el menú principal y guiar al usuario sobre cómo funciona el programa.
Después utilicé un bloque try/except para intentar abrir un archivo llamado clientes.bin, donde se almacenarán los datos. Si el archivo no existe, se crea una lista vacía.
Esto garantiza que el programa pueda iniciarse sin errores y recuperar los clientes guardados previamente.
El núcleo del programa es un bucle while True que muestra las opciones del menú y captura la elección del usuario.
Según la opción seleccionada, se ejecutan las operaciones Crear, Listar, Actualizar o Eliminar clientes.
Para crear un nuevo cliente, empleo nuevocliente = Cliente() y luego clientes.append(nuevocliente) para añadirlo a la lista.
Finalmente, después de cada operación, uso pickle.dump() para guardar la lista actualizada en el archivo binario y cierro el archivo correctamente con archivo.close().
"""

import pickle

# Defino la clase Cliente 
class Cliente:
    def __init__(self):
        self.nombre = ""
        self.email = ""
        self.direccion = ""

print("Programa de gestion de clientes c0.1 Oscar Sorensen")
print("1. Insertar un cliente")
print("2. Listar clientes")
print("3. Actualizar clientes")
print("4. Eliminar clientes")
print("5. Salir")

# --------- Añadido: cargar datos existentes si hay archivo ----------
try:
    archivo = open("clientes.bin", "rb")
    clientes = pickle.load(archivo)
    archivo.close()
    print("Clientes cargados correctamente.")
except:
    print("No existe archivo de datos, se creará uno nuevo.")
    clientes = []
    #la archivo aperece cuando se inserta el primer cliente en "La Raiz del proyecto"
# -------------------------------------------------------------------

while True: # Menu de opciones
    opcion = input("Escoge una opcion: ")
    opcion = int(opcion)

    if opcion == 1: #La archivo aperece cuando se inserta el primer cliente
        print("Vamos a insertar un cliente")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        print("Cliente insertado correctamente.")
        clientes.append(nuevocliente)

    elif opcion == 2: # Listar clientes
        print("Vamos a ver los clientes")
        for c in clientes:
            print("Nombre:", c.nombre, "Email:", c.email, "Direccion:", c.direccion)

    elif opcion == 3: # Actualizar cliente
        print("Vamos a actualizar un cliente")
        nombre_buscar = input("Introduce el nombre del cliente a actualizar: ")
        for c in clientes:
            if c.nombre == nombre_buscar:
                print("Cliente encontrado.")
                c.email = input("Nuevo email: ")
                c.direccion = input("Nueva dirección: ")
                print("Cliente actualizado correctamente.")
                break
        else:
            print("No se encontró un cliente con ese nombre.")

    elif opcion == 4: # Eliminar cliente
        print("Vamos a eliminar un cliente")
        nombre_eliminar = input("Nombre del cliente a eliminar: ")
        for c in clientes:
            if c.nombre == nombre_eliminar:
                clientes.remove(c)
                print("Cliente eliminado.")
                break

    elif opcion == 5: # Salir
        print("Saliendo del programa...")
        break

    # --------- Añadido: guardar los cambios después de cada acción ----------
    archivo = open("clientes.bin", "wb")
    pickle.dump(clientes, archivo)
    archivo.close()
    # -----------------------------------------------------------------------


""""
Con esta actividad he practicado el uso de la librería pickle, junto con estructuras de control como while True y if/elif, para implementar un programa CRUD completo.
El ejercicio refuerza los principios básicos de la programación orientada a objetos, como la organización, la reutilización del código y la claridad en el diseño.
Además, demuestra cómo Python puede manejar datos de manera persistente, combinando clases y almacenamiento binario de forma sencilla y estructurada.
"""


# ====================================================
# Contenido original de: Programacion/Python Notes/NotesGenByFiles/001_Elementos_Explained.py
# ====================================================

# ==========================================
# UNIT 001 — Identificación de los elementos de un programa informático
# Keywords: (bloques, indentación, variables, tipos de datos, literales,
# constantes, operadores, entrada/salida, comentarios, funciones, módulos)
# ==========================================


# ---------- 1) BLOCKS & INDENTATION (bloques, indentación) ----------
# Python uses indentation (spaces at the start of a line) to define blocks of code.
# Standard is 4 spaces. Never mix tabs and spaces.
def show_blocks():                 # Define a function (función)
    for i in range(3):             # Start a loop that runs 3 times
        print("Loop index:", i)    # This line is inside the loop block
    # Back to this column = outside the loop block
show_blocks()                      # Call the function so it runs


# ---------- 2) VARIABLES (variables) ----------
# A variable is a named container for a value. Created by assignment (=).
greeting = "Hello, World"          # str (string / cadena)
age = 25                           # int (entero)
height = 1.82                      # float (decimal)
is_active = True                   # bool (booleano)

# Reassign values and use augmented assignment
age = age + 5                      # 30
age += 2                           # 32 (adds 2)
print("age:", age)

# Naming: snake_case is standard. Identifiers cannot start with digits.
user_name = "oscar_sorensen"       # (identificador en snake_case)


# ---------- 3) DATA TYPES (tipos de datos) ----------
n_int = 7                          # int (entero)
n_float = 2.5                      # float (decimal)
text = "text"                      # str (cadena)
flag = False                       # bool (booleano)
items = [1, 2, 3]                  # list (lista, mutable)
point = (10, 20)                   # tuple (tupla, inmutable)
        # Tuples (tuplas) are ordered collections like lists, but they are IMMUTABLE — 
        # meaning their contents cannot be changed once created. 
        # They use parentheses () instead of square brackets [].
        # Tuples are ideal for storing fixed groups of related data, such as coordinates, colors, or settings.
        # Example: point = (10, 20)
        # You can access elements by index (point[0] -> 10), but you cannot modify them (point[0] = 99 would cause an error).
        # Use tuples when you want data to remain constant throughout the program.

prefs = {"theme": "dark"}          # dict (diccionario, pares clave/valor)
        # Dictionaries (diccionarios) store data as key/value pairs (pares clave/valor). 
        # Each key must be unique and is used to access its corresponding value. 
        # Dictionaries are written with curly braces {} and use a colon (:) between each key and value.
        # Example: prefs = {"theme": "dark"}
        # You can retrieve values by key, e.g. prefs["theme"] -> "dark"
        # Dictionaries are MUTABLE — you can add, modify, or remove items after creation.
        # Example modifications:
        # prefs["language"] = "en"   # add new key/value
        # prefs["theme"] = "light"   # update existing value
        # del prefs["theme"]         # delete a key/value pair

unique = {1, 2, 3}                 # set (conjunto, sin duplicados)
        # Sets (conjuntos) are unordered collections of unique elements (sin duplicados).
        # They are written using curly braces {} like dictionaries, but without key/value pairs.
        # Example: unique = {1, 2, 3}
        # Sets automatically remove duplicates — {1, 2, 2, 3} becomes {1, 2, 3}.
        # They are useful for membership checks, removing duplicates from lists, 
        # and performing mathematical operations like union (|), intersection (&), and difference (-).
        # Example:
        # A = {1, 2, 3}; B = {3, 4, 5}
        # print(A | B)  # union -> {1, 2, 3, 4, 5}
        # print(A & B)  # intersection -> {3}
        # print(A - B)  # difference -> {1, 2}


print(type(items), type(prefs), type(unique))  # Show data types

# Conversions (conversiones de tipos)
n_from_str = int("10")             # "10" -> 10
f_from_str = float("2.5")          # "2.5" -> 2.5
        # The float() function converts a string or integer into a floating-point number (número decimal).
        # In this example, the string "2.5" becomes the numeric value 2.5.
        # This is essential when reading user input, because input() always returns text (str).
        # Example:
        # f_from_str = float("2.5")  # result: 2.5
        # Once converted, you can perform mathematical operations on it:
        # print(f_from_str * 2)  # -> 5.0
        # If the string cannot be converted (e.g., "abc"), Python will raise a ValueError.

s_from_num = str(123)              # 123 -> "123"
        # The bool() function converts a value into a Boolean (True or False).
        # In Python, the number 0 is considered False, and any nonzero number is True.
        # This is often used in conditions to test if a value is "empty" or "zero".
        # Example:
        # b_from_num = bool(0)      # -> False
        # b_from_num = bool(5)      # -> True
        # It also works with other data types:
        # bool("")  -> False (empty string)
        # bool([]) -> False (empty list)
        # bool("text") -> True (non-empty string)
        # This helps simplify conditions, for example:
        # if value: print("Has content")  # executes only if value is not empty or zero


# ---------- 4) LITERALS (literales) ----------
# A literal is a fixed value written directly in code.
answer = 42                        # int literal
pi = 3.14159                       # float literal
truth = True                       # boolean literal
hello = "Hello"                    # string literal
multiline = """This is
a multi-line string."""            # triple-quoted string (multi-línea)
print(hello, pi, truth)
print(multiline)


# ---------- 5) CONSTANTS BY CONVENTION (constantes) ----------
# Python has no enforced constants; we use UPPER_CASE names by convention.
TAX_RATE = 0.21                    # constant by convention
base_price = 100
total_price = base_price * (1 + TAX_RATE)
print("Total with tax:", total_price)


# ---------- 6) OPERATORS (operadores) ----------
a, b = 7, 3                        # multiple assignment

# Arithmetic (aritméticos)
print(a + b, a - b, a * b, a / b)  # + - * /  -> 10 4 21 2.333...
print(a // b)                      # // floor division -> 2 (entero)
print(a % b)                       # % modulus -> remainder 1
print(a ** b)                      # ** exponentiation -> 343

# Comparison (comparación) -> return bool
print(a == b, a != b, a > b, a >= b, a < b, a <= b)

# Logical (lógicos) with booleans
x, y = True, False
print(x and y, x or y, not x)      # and / or / not

# Membership (pertenencia) with sequences/collections
fruits = ["apple", "pear"]
print("apple" in fruits)           # True
print("orange" not in fruits)      # True

# Precedence (precedencia): ** > * / // % > + - > comparaciones > and > or.
# Use parentheses to make evaluation order explicit in exams.

# Comparison operators (operadores de comparación)
# These compare two values and return a Boolean result: True or False.
# They are used inside conditions (if statements, loops) to control program flow.

    # Operator | Meaning (English)              | Example (Result)
    # ------------------------------------------------------------
    # ==       | Equal to                       | 5 == 5   → True
    # !=       | Not equal to                   | 5 != 3   → True
    # >        | Greater than                   | 7 > 3    → True
    # >=       | Greater than or equal to       | 7 >= 7   → True
    # <        | Less than                      | 3 < 5    → True
    # <=       | Less than or equal to          | 4 <= 4   → True
    #
    # Example usage:
    # a, b = 7, 3
    # print(a == b)   # False
    # print(a > b)    # True
    # print(a != b)   # True
    #
    # These expressions are essential in conditional structures like:
    # if a > b:
    #     print("a is greater than b")



# ---------- 7) INPUT / OUTPUT (entrada/salida) ----------
# input() reads a line of user text (always returns str).
# print() shows output.
name = input("Enter your name: ")
age_str = input("Enter your age: ")
try:                               # try/except to catch conversion errors
    age_val = int(age_str)         # convert string to int
    print(f"Hello {name}. In 5 years you will be {age_val + 5}.")
except ValueError:                 # runs if int(...) fails
    print("Age must be a number.")

# The letter f before a string ("f-string") activates formatted string literals (cadenas formateadas).
# It allows you to insert variables or expressions directly inside curly braces {} within the string.
# Example:
# name = "Oscar"
# age_val = 25
# print(f"Hello {name}. In 5 years you will be {age_val + 5}.")
# → Output: Hello Oscar. In 5 years you will be 30.
#
# Without f-strings, you would need slower, more complex syntax:
# print("Hello " + name + ". In 5 years you will be " + str(age_val + 5))
#
# f-strings automatically convert values to text and can include calculations, functions, or formatting:
# print(f"Price: {9.99:.2f}")   # -> "Price: 9.99" (two decimals)
# print(f"Next year: {2025 + 1}")  # -> "Next year: 2026"
#
# In short: f-strings are cleaner, faster, and more readable for dynamic text output.



# ---------- 8) COMMENTS (comentarios) ----------
# Single-line comments start with '#'.
"""
This is a multi-line string often used for docstrings
or block comments to explain larger sections of code.
"""


# ---------- 9) FUNCTIONS & MODULES (funciones, módulos) ----------
# A function is a reusable block of code defined with 'def'.
# A module is a separate file/library you can import (e.g., math).

import math                        # (módulo estándar)

def circle_area(radius):           # Define a function with a parameter
    """Return area of a circle given its radius (radio)."""
    return math.pi * (radius ** 2) # Use math.pi and exponent operator

print("Area (r=2):", circle_area(2))

# Functions (funciones) let you group code into reusable blocks. 
# They are defined with the keyword 'def' followed by a name and parentheses.
# Any value passed between the parentheses is called a *parameter* (parámetro).
# You can then use that parameter inside the function’s code.
#
# The 'return' statement sends a result back to where the function was called.
# This makes functions ideal for calculations and repeated logic.
#
# Example:
# def circle_area(radius):
#     return math.pi * (radius ** 2)
# 
# When you call circle_area(2), Python:
# 1) Creates a variable radius = 2
# 2) Executes the function’s body
# 3) Returns the computed value (π * 2²)
#
# The import math line brings in the standard math module (módulo estándar),
# which contains mathematical constants and functions like math.pi, math.sqrt(), math.ceil(), etc.
#
# Example usage:
# print("Area (r=2):", circle_area(2))  -> Area (r=2): 12.566370614359172
#
# In summary:
# - Use 'def' to define reusable logic.
# - Use 'import' to bring in ready-made functions from other files or Python’s standard library.
# - Always include 'return' if you want the function to send back a value.



# ---------- 10) MINI PRACTICE ----------
# VAT calculator with formatting to 2 decimals
amount = 250
result = amount * (1 + TAX_RATE)
print(f"Amount {amount} -> Total {result:.2f}")

# Quick sanity check with assert (aseveración)
assert isinstance(result, float)   # should be float; raises if False

# The assert statement (aseveración) is used to test that something is True during program execution.
# If the condition inside assert is False, Python stops the program and raises an AssertionError.
# This is a quick way to catch logic errors or invalid results while developing.

# Example:
# assert isinstance(result, float)
# This checks that 'result' is a float (decimal number). 
# - If it IS a float, nothing happens and the program continues normally.
# - If it’s NOT a float, Python stops and prints an error like:
#   AssertionError: 

# You can also include a custom error message:
# assert result > 0, "Result must be positive"

# In short: use assert to confirm that important assumptions about your program are true.
# It’s mostly used for debugging or self-checks, not in final production code.




# ====================================================
# Contenido original de: Programacion/Python Notes/NotesGenByFiles/002_Objetos_Explained.py
# ====================================================

# ==========================================
# UNIT 002 — Utilización de objetos (Using Objects)
# Keywords: (objetos, métodos, propiedades, mutabilidad, cadenas, listas, tuplas, diccionarios, conjuntos)
# ==========================================

# Everything in Python is an object. Objects contain data (attributes) and functions (methods)
# that operate on that data.

# ---------- 1) STRINGS (cadenas) ----------
# Strings are sequences of characters. They are immutable (cannot be changed directly).

text = "  CEAC Programación 2025  "   # A string with spaces
print(text.strip())                    # Removes spaces at start/end
print(text.lower())                    # Converts to lowercase
print(text.upper())                    # Converts to uppercase
print(text.replace("2025", "2026"))    # Replace parts of the string
print("CEAC" in text)                  # Check membership (returns True if found)

# Splitting and joining strings
words = text.split()                   # Split into list of words
joined = "-".join(words)               # Join list back into string
print(words)
print(joined)


# ---------- 2) LISTS (listas) ----------
# Lists are ordered, mutable collections (can be changed).

numbers = [3, 1, 2]                   # Create a list
numbers.append(4)                     # Add element at the end
numbers.sort()                        # Sort list in place
print("Sorted list:", numbers)

numbers.insert(0, 99)                 # Insert 99 at index 0
print("After insert:", numbers)
print(numbers[0], numbers[-1])        # Access first and last element
print(numbers[1:3])                   # Slice (elements from 1 to 2)

removed = numbers.pop()               # Remove last element and return it
print("Removed:", removed, "Now:", numbers)


# ---------- 3) TUPLES (tuplas) ----------
# Tuples are like lists but immutable (cannot be changed).

point = (10, 20)
print(point[0], len(point))
# point[0] = 99  # Would cause error because tuples are immutable


# ---------- 4) DICTIONARIES (diccionarios) ----------
# Dictionaries store key/value pairs. You can add or modify entries dynamically.

student = {"name": "Oscar", "age": 25}
print(student["name"])                 # Access value by key
student["grade"] = 9.5                 # Add new key/value
print(student)

print(list(student.keys()))            # List of keys
print(list(student.values()))          # List of values
print(student.get("city", "Unknown"))  # Safe access (returns default if missing)


# ---------- 5) SETS (conjuntos) ----------
# Sets store unique, unordered elements. Useful for removing duplicates.

A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A | B)                # Union of both sets
print("Intersection:", A & B)         # Common elements
print("Difference:", A - B)           # In A but not B
print("Symmetric diff:", A ^ B)       # In one but not both


# ---------- 6) MUTABILITY (mutabilidad) ----------
# Mutable means the content can change without changing identity.

L = [1, 2, 3]
L[0] = 100                            # Modify first element
T = (1, 2, 3)
# T[0] = 100                          # Error (immutable)
D = {"x": 1}
D["x"] = 2                            # Modify dict value
print(L, D)


# ---------- 7) OBJECT METHODS (métodos de objeto) ----------
# Methods are functions attached to objects.

name = "oscar"
print(name.capitalize())               # Capitalize first letter
print(name.startswith("o"))            # Returns True if starts with "o"
print(",".join(["a", "b", "c"]))       # Join elements of list into a string


# ---------- 8) PRACTICE EXAMPLE ----------
# Normalize a list of emails (strip + lower) and remove duplicates.

emails = ["  A@X.com ", "b@y.com", "a@x.com"]
normalized = [e.strip().lower() for e in emails]   # Clean up each email
unique_emails = sorted(set(normalized))            # Convert to set (remove duplicates)
print(unique_emails)


# ---------- 9) EXAM TIPS ----------
# - Be able to manipulate strings, lists, dicts, and sets.
# - Remember which objects are mutable (list, dict, set) vs immutable (str, tuple).
# - Use methods correctly: list.append(), dict.get(), str.replace(), set.union().



# ====================================================
# Contenido original de: Programacion/Python Notes/NotesGenByFiles/003_Estructuras_de_control_Explained.py
# ====================================================

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

# ---------- 6B) ASSERTIONS (aserciones) ----------
# Used to verify that a condition is True during program execution.
# If the condition is False, the program stops with an AssertionError.

age = 25
assert age > 0, "Age must be positive"
print("Valid age:", age)

# Example: Check that divisor is not zero before dividing.
dividendo = 10
divisor = 2
assert divisor != 0, "Divisor cannot be zero"
resultado = dividendo / divisor
print("Resultado:", resultado)



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

# ---------- 7) MINI PROJECT: PLANIFICADOR DE CUADRAS ----------
# Combines input, math, and datetime modules.

import math
import datetime

print("\n--- PLANIFICADOR DE CUADRAS ---")
horses = input("Introduce el número de caballos: ")

try:
    horses = int(horses)
    if horses == 0:
        print("No hay caballos, no se necesitan cuadras.")
    else:
        capacity = int(input("Capacidad de cada cuadra (caballos por cuadra): "))
        stables_needed = math.ceil(horses / capacity)
        today = datetime.date.today()
        is_weekend = today.isoweekday() in (6, 7)   # 6 = sábado, 7 = domingo

        print("Fecha:", today)
        print("¿Fin de semana?", is_weekend)
        print("Cuadras necesarias:", stables_needed)
except ValueError:
    print("Entrada no válida.")


# ---------- EXTRA: División (operadores matemáticos) ----------
# Dividendo: número que se divide.
# Divisor: número por el que se divide el dividendo.
# Cociente: resultado de la división.
# Resto: parte sobrante si la división no es exacta.
# Ejemplo: 20 ÷ 4 = 5 → dividendo=20, divisor=4, cociente=5, resto=0

# --- Example in Python ---
dividendo = 20
divisor = 3
cociente = dividendo // divisor      # división entera (integer division)
resto = dividendo % divisor          # módulo, devuelve el resto

print("Dividendo:", dividendo)
print("Divisor:", divisor)
print("Cociente:", cociente)
print("Resto:", resto)


# ---------- 8) EXAM TIPS ----------
# - Use indentation correctly for if/elif/else and loops.
# - Show input validation with try/except.
# - Demonstrate break/continue inside a loop.
# - Combine range(), input(), and conditions in one example.



# ====================================================
# Contenido original de: Programacion/Python Notes/NotesGenByFiles/004_Desarrollo_de_clases_Explained.py
# ====================================================

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



# ---------- 3) PRIVATE ATTRIBUTES + GETTERS ----------
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

# ---------- PRIVATE ATTRIBUTES, GETTERS AND SETTERS ----------

# In Python, attributes starting with "_" are considered internal (private use).
# Getters and setters allow safe access and modification of those attributes.

class BankAccount:
    def __init__(self):
        self._balance = 0.0       # private attribute

    # Getter -> returns the value
    def get_balance(self):
        return self._balance

    # Setter -> modifies the value with validation
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")


# Example of use
account = BankAccount()
account.set_balance(150)
print("Balance:", account.get_balance())


# Encapsulation principle:
# Internal data (_balance) is not accessed directly from outside the class,
# but through methods that control how it is read or changed.



# ---------- 4) EXAM TIPS ----------
# - Include at least one __init__ constructor.
# - Show property assignment and access.
# - Demonstrate methods that modify data.
# - Use self consistently inside class methods.



# ====================================================
# Contenido original de: Programacion/Python Notes/NotesGenByFiles/005_Lectura_y_escritura_Explained.py
# ====================================================

# ==========================================
# UNIT 005 — Lectura y escritura de información (Reading and Writing Information)
# Keywords: (archivos, ficheros, lectura, escritura, pickle, binarios, json, persistencia)
# ==========================================

# ---------- 1) TEXT FILES ----------
# Files can be opened in text mode using open(filename, mode, encoding).

# 'w' -> write (overwrites existing file)
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("First line\nSecond line")

# 'a' -> append (adds to end of file)
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")

# 'r' -> read
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())


# ---------- 2) JSON (structured text) ----------
import json
data = {"name": "Oscar", "year": 2025}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    result = json.load(f)
print("JSON loaded:", result)


# ---------- 3) PICKLE (binary files) ----------
import pickle
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"

products = [Product("Shaker", 9.99), Product("Bottle", 5.5)]

# Save binary
with open("products.bin", "wb") as f:
    pickle.dump(products, f)

# Load binary
with open("products.bin", "rb") as f:
    loaded = pickle.load(f)
print("Loaded from binary:", loaded)


# ---------- 4) FILESYSTEM OPERATIONS ----------
import os
print("Files in current folder:", os.listdir("."))

# Calculate total size of all files
total = 0
for root, dirs, files in os.walk("."):
    for fname in files:
        try:
            total += os.path.getsize(os.path.join(root, fname))
        except OSError:
            pass
print("Total bytes:", total)


# ---------- 5) ERROR HANDLING ----------
try:
    with open("maybe.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found -> creating new one.")
    with open("maybe.txt", "w", encoding="utf-8") as f:
        f.write("Created automatically.")


# ---------- 5B) MÉTODOS ESTÁTICOS (static methods) ----------
# Static methods belong to the class, not to individual objects.

class Entrenamiento:
    @staticmethod
    def calcular_puntuacion(series, repeticiones):
        return series * repeticiones

# Uso
resultado = Entrenamiento.calcular_puntuacion(4, 10)
print("Puntuación del entrenamiento:", resultado)

# ---------- 5C) MENÚ CRUD SIMPLE ----------
# Combine insert/list options inside a while-loop menu.

while True:
    print("\n1) Insertar cliente  2) Listar clientes  3) Salir")
    opcion = input("> ")

    if opcion == "1":
        insert_client()
    elif opcion == "2":
        list_clients()
    elif opcion == "3":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")



# ---------- 6) EXAM TIPS ----------
# - Know open() modes: r, w, a, rb, wb.
# - Understand difference between text and binary files.
# - Use pickle for saving/loading Python objects.
# - Handle missing files using try/except.



# ====================================================
# Contenido original de: Programacion/Python Notes/NotesGenByFiles/Programacion_001-005_Explained_All.py
# ====================================================

# ==========================================
# COMBINED UNITS 001–005 (Explained)
# ==========================================



# ==========================================
# UNIT 002 — Utilización de objetos (Using Objects)
# Keywords: (objetos, métodos, propiedades, mutabilidad, cadenas, listas, tuplas, diccionarios, conjuntos)
# ==========================================

# Everything in Python is an object. Objects contain data (attributes) and functions (methods)
# that operate on that data.

# ---------- 1) STRINGS (cadenas) ----------
# Strings are sequences of characters. They are immutable (cannot be changed directly).

text = "  CEAC Programación 2025  "   # A string with spaces
print(text.strip())                    # Removes spaces at start/end
print(text.lower())                    # Converts to lowercase
print(text.upper())                    # Converts to uppercase
print(text.replace("2025", "2026"))    # Replace parts of the string
print("CEAC" in text)                  # Check membership (returns True if found)

# Splitting and joining strings
words = text.split()                   # Split into list of words
joined = "-".join(words)               # Join list back into string
print(words)
print(joined)


# ---------- 2) LISTS (listas) ----------
# Lists are ordered, mutable collections (can be changed).

numbers = [3, 1, 2]                   # Create a list
numbers.append(4)                     # Add element at the end
numbers.sort()                        # Sort list in place
print("Sorted list:", numbers)

numbers.insert(0, 99)                 # Insert 99 at index 0
print("After insert:", numbers)
print(numbers[0], numbers[-1])        # Access first and last element
print(numbers[1:3])                   # Slice (elements from 1 to 2)

removed = numbers.pop()               # Remove last element and return it
print("Removed:", removed, "Now:", numbers)


# ---------- 3) TUPLES (tuplas) ----------
# Tuples are like lists but immutable (cannot be changed).

point = (10, 20)
print(point[0], len(point))
# point[0] = 99  # Would cause error because tuples are immutable


# ---------- 4) DICTIONARIES (diccionarios) ----------
# Dictionaries store key/value pairs. You can add or modify entries dynamically.

student = {"name": "Oscar", "age": 25}
print(student["name"])                 # Access value by key
student["grade"] = 9.5                 # Add new key/value
print(student)

print(list(student.keys()))            # List of keys
print(list(student.values()))          # List of values
print(student.get("city", "Unknown"))  # Safe access (returns default if missing)


# ---------- 5) SETS (conjuntos) ----------
# Sets store unique, unordered elements. Useful for removing duplicates.

A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A | B)                # Union of both sets
print("Intersection:", A & B)         # Common elements
print("Difference:", A - B)           # In A but not B
print("Symmetric diff:", A ^ B)       # In one but not both


# ---------- 6) MUTABILITY (mutabilidad) ----------
# Mutable means the content can change without changing identity.

L = [1, 2, 3]
L[0] = 100                            # Modify first element
T = (1, 2, 3)
# T[0] = 100                          # Error (immutable)
D = {"x": 1}
D["x"] = 2                            # Modify dict value
print(L, D)


# ---------- 7) OBJECT METHODS (métodos de objeto) ----------
# Methods are functions attached to objects.

name = "oscar"
print(name.capitalize())               # Capitalize first letter
print(name.startswith("o"))            # Returns True if starts with "o"
print(",".join(["a", "b", "c"]))       # Join elements of list into a string


# ---------- 8) PRACTICE EXAMPLE ----------
# Normalize a list of emails (strip + lower) and remove duplicates.

emails = ["  A@X.com ", "b@y.com", "a@x.com"]
normalized = [e.strip().lower() for e in emails]   # Clean up each email
unique_emails = sorted(set(normalized))            # Convert to set (remove duplicates)
print(unique_emails)


# ---------- 9) EXAM TIPS ----------
# - Be able to manipulate strings, lists, dicts, and sets.
# - Remember which objects are mutable (list, dict, set) vs immutable (str, tuple).
# - Use methods correctly: list.append(), dict.get(), str.replace(), set.union().


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


# ==========================================
# UNIT 005 — Lectura y escritura de información (Reading and Writing Information)
# Keywords: (archivos, ficheros, lectura, escritura, pickle, binarios, json, persistencia)
# ==========================================

# ---------- 1) TEXT FILES ----------
# Files can be opened in text mode using open(filename, mode, encoding).

# 'w' -> write (overwrites existing file)
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("First line\nSecond line")

# 'a' -> append (adds to end of file)
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")

# 'r' -> read
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())


# ---------- 2) JSON (structured text) ----------
import json
data = {"name": "Oscar", "year": 2025}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    result = json.load(f)
print("JSON loaded:", result)


# ---------- 3) PICKLE (binary files) ----------
import pickle
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"

products = [Product("Shaker", 9.99), Product("Bottle", 5.5)]

# Save binary
with open("products.bin", "wb") as f:
    pickle.dump(products, f)

# Load binary
with open("products.bin", "rb") as f:
    loaded = pickle.load(f)
print("Loaded from binary:", loaded)


# ---------- 4) FILESYSTEM OPERATIONS ----------
import os
print("Files in current folder:", os.listdir("."))

# Calculate total size of all files
total = 0
for root, dirs, files in os.walk("."):
    for fname in files:
        try:
            total += os.path.getsize(os.path.join(root, fname))
        except OSError:
            pass
print("Total bytes:", total)


# ---------- 5) ERROR HANDLING ----------
try:
    with open("maybe.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found -> creating new one.")
    with open("maybe.txt", "w", encoding="utf-8") as f:
        f.write("Created automatically.")


# ---------- 6) EXAM TIPS ----------
# - Know open() modes: r, w, a, rb, wb.
# - Understand difference between text and binary files.
# - Use pickle for saving/loading Python objects.
# - Handle missing files using try/except.



# ====================================================
# Contenido original de: Programacion/Python Notes/NotesGenByFiles/zEXTRA_UNIT_004_005_006_NOTES.py
# ====================================================

# ==========================================
# UNITS 004–005 — File System, Persistence, and Interfaces
# Keywords: (filesystem, os, open, read, write, pickle, json, compression, tkinter, events, mysql)
# ==========================================

# ---------- 1) FILE SYSTEM OPERATIONS ----------
# Python can explore and manipulate the filesystem using the os module.

import os
print(os.listdir('.'))          # List files in current folder
print(os.getcwd())              # Show current working directory
print(os.path.getsize('file'))  # Get file size (bytes)
print(os.path.abspath('file'))  # Get absolute path

# Recursive directory walk
for root, dirs, files in os.walk('.'):
    for name in files:
        print(os.path.join(root, name))

# ---------- 2) FILE ATTRIBUTES ----------
# You can check existence, type, and permissions.

print(os.path.exists('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('folder'))

# ---------- 3) TEXT FILES ----------
# open(filename, mode, encoding)
# Modes: 'r' (read), 'w' (write, overwrite), 'a' (append)

with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('First line\nSecond line')

with open('example.txt', 'a', encoding='utf-8') as f:
    f.write('\nAppended line')

with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print('Line:', line.strip())

# ---------- 4) JSON FILES ----------
import json
data = {'name': 'Oscar', 'year': 2025}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print('JSON loaded:', result)

# ---------- 5) PICKLE (BINARY PERSISTENCE) ----------
import pickle

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f'Product({self.name!r}, {self.price!r})'

products = [Product('Shaker', 9.99), Product('Bottle', 5.5)]

# Save binary
with open('products.bin', 'wb') as f:
    pickle.dump(products, f)

# Load binary
with open('products.bin', 'rb') as f:
    loaded = pickle.load(f)
print('Loaded from binary:', loaded)

# ---------- 6) FILE CREATION / DELETION / COMPRESSION ----------
# Create folder and files
os.mkdir('myfolder')
with open('myfolder/test.txt', 'w') as f:
    f.write('test')

# Delete file or folder
os.remove('myfolder/test.txt')
os.rmdir('myfolder')

# Compress files
import zipfile
with zipfile.ZipFile('archive.zip', 'w') as z:
    z.write('example.txt')

# ---------- 7) ERROR HANDLING ----------
try:
    with open('maybe.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('File not found -> creating new one.')
    with open('maybe.txt', 'w', encoding='utf-8') as f:
        f.write('Created automatically.')

# ---------- 8) STATIC METHODS ----------
class Entrenamiento:
    @staticmethod
    def calcular_puntuacion(series, repeticiones):
        return series * repeticiones

print('Training score:', Entrenamiento.calcular_puntuacion(4, 10))

# ---------- 9) SIMPLE CRUD MENU ----------
def insert_client():
    print('Insert client placeholder')

def list_clients():
    print('List clients placeholder')

while True:
    print('\n1) Insert client  2) List clients  3) Exit')
    option = input('> ')
    if option == '1':
        insert_client()
    elif option == '2':
        list_clients()
    elif option == '3':
        break
    else:
        print('Invalid option.')

# ---------- 10) TKINTER (GRAPHICAL INTERFACES) ----------
from tkinter import *

root = Tk()
root.title('My App')
Label(root, text='Name:').pack()
Entry(root).pack()
Button(root, text='Save').pack()
root.mainloop()

# ---------- 11) EVENTS ----------
# Events are actions triggered by the user (clicks, keys).
# Example of binding an event to a button click.

def on_click():
    print('Button clicked!')

root = Tk()
btn = Button(root, text='Click Me')
btn.pack()
btn.bind('<Button-1>', lambda e: on_click())
root.mainloop()

# ---------- 12) MYSQL CONNECTION (optional) ----------
# Simple connection example (requires mysql-connector-python).

import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='examdb'
)
cursor = conn.cursor()
cursor.execute('SHOW TABLES;')
for row in cursor:
    print(row)
conn.close()

# ---------- 13) KEY CONCEPTS SUMMARY ----------
# open() modes: r, w, a, rb, wb
# pickle: save/load Python objects in binary
# json: structured text format (compatible with other languages)
# os: list, remove, create, navigate files/folders
# tkinter: build graphical interfaces
# events: user interactions like clicks or keys
# mysql.connector: connect to MySQL databases
# try/except: handle errors gracefully



# ====================================================
# Contenido original de: Programacion/Python Notes/UNIT005_Deep_Explained_StudyGuide.py
# ====================================================

# ==========================================
# UNIT 005 — Reading & Writing Information (Deep Study Guide)
# Author: Oscar Sørensen — Study edition (explanations first, then clean, runnable code)
# Style: English learning-style explanations + short exam tip boxes + minimal, clean code blocks
# ==========================================

# ======================================================
# SECTION 0 — FILE BASICS: open(), modes, encodings, and iteration
# ======================================================
"""
BIG PICTURE
-----------
Your computer stores data as files on disk. Python can connect to those files, read data
from them, and write new data to them. The function you use is:
    open(path, mode, encoding)

- path:    file name or path (e.g., "example.txt" or "/Users/oscar/example.txt")
- mode:    what you want to do with the file
           "w"  -> write text (creates/overwrites the file)
           "a"  -> append text (adds at the end; preserves old content)
           "r"  -> read text (error if file does not exist)
           "wb" -> write binary (images, pickle objects, etc.)
           "rb" -> read binary
- encoding: how characters are translated to bytes for text files. Use "utf-8".

WHY 'with open(...) as f:' ?
----------------------------
Files are resources that must be closed after use. If you forget to close them, data might
not be fully saved (because of buffering), or the OS might lock the file. The 'with' block
creates a safe context: when the block ends, Python automatically calls f.close() for you,
even if an error happens inside the block.

WHAT IS f.write()?
------------------
- f is a file object. Think of it as a pen connected to the file.
- f.write(text) sends text from your program into the file on disk.
- It returns the number of characters written (we usually don't use that return value).

WHAT IS '\n'?
-------------
This is the newline character. It means “start a new line” (similar to pressing ENTER).
When you write "Hello\nWorld", the file content becomes:
    Hello
    World
If you forget the newline at the end of a line, the next write will continue on the same line.

HOW DOES READING WORK?
----------------------
When you do:
    for line in f:
Python reads the file line by line. Each 'line' still includes the newline at the end.
That's why we often call .strip() to remove newline and surrounding spaces before printing.

EXAM TIPS
---------
- Always use 'with open(..., mode, encoding="utf-8") as f:' in text tasks.
- Remember modes: 'w' overwrites, 'a' appends, 'r' reads (error if missing).
- Mention that '\\n' is a newline and why we use .strip() when printing lines.
"""

def file_basics_demo():
    # 1) Write (overwrites or creates)
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("First line\nSecond line")     # '\n' -> new line
    
    # 2) Append (preserves old content, adds to the end)
    with open("example.txt", "a", encoding="utf-8") as f:
        f.write("\nAppended line")
    
    # 3) Read (iterate lines, strip newline for clean output)
    with open("example.txt", "r", encoding="utf-8") as f:
        for line in f:
            print("Line:", line.strip())


# ======================================================
# SECTION 1 — TEXT FILE EXERCISE: a simple contact agenda (write & read)
# ======================================================
"""
GOAL
----
Create a minimal contact agenda that:
  1) Asks the user for a name and an email and saves it to 'agenda.txt'.
  2) Reads all contacts from 'agenda.txt' and prints them nicely.

WHY THIS MATTERS
----------------
- You learn persistence (data survives after the program ends).
- You practice modes 'a' (append) and 'r' (read).
- You practice splitting a line into parts using .split(',').

WHAT HAPPENS UNDER THE HOOD
---------------------------
WRITE:
- We ask for two strings using input().
- We open 'agenda.txt' in append mode ("a") so we never destroy existing contacts.
- We write "name,email\n" so each contact is on its own line.

READ:
- We open 'agenda.txt' in read mode ("r").
- We loop through each line. Each line looks like "Name,Email\n".
- We do line.strip() to remove '\n', then split(',') to separate fields into [name, email].
- We print them in a readable format.

COMMON MISTAKES
---------------
- Forgetting the '\n' -> new contact gets glued to the previous one.
- Using "w" accidentally instead of "a" -> you erase the file.
- Assuming the file exists when reading. Use try/except FileNotFoundError for a friendly message.

EXAM TIPS
---------
- Show that you know how to append without overwriting.
- Explain why you use .split(',') and .strip().
- Mention that you close files using 'with' (automatic).
"""

def agenda_write_contact():
    name = input("Enter contact name: ")
    email = input("Enter contact email: ")
    with open("agenda.txt", "a", encoding="utf-8") as f:
        f.write(name + "," + email + "\n")
    print("Contact saved.")

def agenda_read_all():
    print("\nContacts in the agenda:")
    try:
        with open("agenda.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, email = line.strip().split(",")
                print("Name:", name, "| Email:", email)
    except FileNotFoundError:
        print("No 'agenda.txt' found — add a contact first.")


# ======================================================
# SECTION 2 — JSON to HTML: create a blog.html from blog.json
# ======================================================
"""
GOAL
----
Read a JSON file that contains blog posts and generate a simple HTML page that displays them.

WHAT IS JSON?
-------------
JSON is a text format for structured data: objects (dicts) and arrays (lists). In Python:
- json.load(file)  -> read JSON from a file and convert it to Python objects (dicts/lists).
- json.dump(obj)   -> write Python objects as JSON into a file.

WORKFLOW
--------
1) Read "blog.json" using json.load(). We expect a list of dicts like:
   [
     {"titulo":"...", "fecha":"...", "autor":"...", "contenido":"..."},
     ...
   ]
2) Open "blog.html" for writing.
3) Write an HTML header (doctype, <html>, <head>, styles, start of <main>).
4) For each article dict in the list, write an <article> block that includes its data.
5) Close the HTML structure.

WHY THIS MATTERS
----------------
- You learn to transform structured data (JSON) into a presentable format (HTML).
- You see how back-end code (Python) can produce front-end output (HTML page).

EXAM TIPS
---------
- Use the exact variable names if the statement requires them (archivo_json, archivo_html, contenido_blog).
- Explain that json.load() turns text JSON into Python data structures you can iterate over.
- Keep HTML writing clean and minimal. Close the tags.
"""
import json

def blog_json_to_html():
    archivo_json = "blog.json"
    archivo_html = "blog.html"
    contenido_blog = []

    # Read JSON into Python
    with open(archivo_json, "r", encoding="utf-8") as f:
        contenido_blog = json.load(f)

    # Build minimal HTML
    head = """<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSAblog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      main{background:white;color:black;padding:20px;width:800px;margin:40px auto;border-radius:6px;}
      article{border-bottom:1px solid #ddd;padding:10px 0;margin:10px 0;}
      h2{margin:0 0 6px 0;}
      .meta{font-size:12px;color:#555;}
    </style>
  </head>
  <body>
    <header><h1 style="text-align:center;color:white;">JOCARSAblog</h1></header>
    <main>
"""
    tail = """    </main>
    <footer style="text-align:center;color:white;">(c)2025 Jose Vicente Carratalá</footer>
  </body>
</html>
"""

    # Write HTML file
    with open(archivo_html, "w", encoding="utf-8") as f:
        f.write(head)
        for art in contenido_blog:
            titulo = art.get("titulo", "(Sin título)")
            fecha  = art.get("fecha", "")
            autor  = art.get("autor", "")
            cont   = art.get("contenido", "")
            block = f"""      <article>
        <h2>{titulo}</h2>
        <div class="meta">{fecha} — {autor}</div>
        <p>{cont}</p>
      </article>
"""
            f.write(block)
        f.write(tail)
    print("Generated blog.html from blog.json")


# ======================================================
# SECTION 3 — “Antonio” case: write/append, read last line, and pickle an object
# ======================================================
"""
GOAL
----
- Write "Food cooked: Pizza" into 'foods.txt' (overwrite, then append "Hamburger").
- Read the last line from 'foods.txt'.
- Save and load an object using pickle (binary serialization).

WHAT IS PICKLE?
---------------
Pickle converts Python objects into a stream of bytes so you can save them to a file
and load them later. It preserves Python-specific structures (classes, lists, dicts, etc.).

- pickle.dump(obj, file) -> save object to an open file in 'wb' mode.
- pickle.load(file)      -> read object from an open file in 'rb' mode.

IMPORTANT
---------
Pickle is Python-specific. You cannot easily read a pickle file from other languages.
Use JSON for cross-language interchange, and pickle when you want to preserve exact Python objects.

EXAM TIPS
---------
- Remember: text files use "w"/"a"/"r" with encoding; pickle uses "wb"/"rb".
- Demonstrate that you can show the last line by reading all lines and taking the last element.
"""
import pickle

def foods_write_and_append():
    with open("foods.txt", "w", encoding="utf-8") as f:
        f.write("Food cooked: Pizza\n")
    with open("foods.txt", "a", encoding="utf-8") as f:
        f.write("Food cooked: Hamburger\n")
    print("Written and appended to 'foods.txt'.")

def foods_read_last_line():
    try:
        with open("foods.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()                 # returns a list of lines
            if lines:
                print("Last line:", lines[-1].strip())
            else:
                print("File is empty.")
    except FileNotFoundError:
        print("No 'foods.txt' found — run foods_write_and_append() first.")

class Training:
    def __init__(self, date, exercise, sets, reps):
        self.date = date
        self.exercise = exercise
        self.sets = sets
        self.reps = reps

    def __repr__(self):
        return f"Training({self.date!r}, {self.exercise!r}, {self.sets!r}, {self.reps!r})"

def pickle_save_and_load_demo():
    obj = Training("2025-10-20", "Bench press", 4, 10)
    with open("training.bin", "wb") as f:
        pickle.dump(obj, f)          # serialize to bytes and write
    with open("training.bin", "rb") as f:
        loaded = pickle.load(f)      # read bytes and reconstruct object
    print("Loaded object:", loaded)


# ======================================================
# SECTION 4 — Filesystem operations: folder size and files larger than 1 GB
# ======================================================
"""
GOAL
----
- Ask for a folder path and calculate the total size of files in that folder (non-recursive).
- Walk the folder recursively and print files larger than 1 GB.

KEY FUNCTIONS
-------------
- os.listdir(path) -> list of names in a directory (files and subfolders, not recursive).
- os.path.join(a,b) -> safely join folder and name into a full path.
- os.path.getsize(path) -> file size in bytes.
- os.walk(top) -> recursively yields (dirpath, dirnames, filenames) for all subfolders.

WHY BYTES → MB/GB?
------------------
File size is in bytes. We convert to MB/GB by dividing:
- MB  = bytes / (1024 * 1024)
- GB  = bytes / (1024 * 1024 * 1024)

ERRORS
------
- If you try to get the size of a path that is not a file (like a folder), you may get errors.
- Wrap size calls in try/except OSError to skip unreadable files.

EXAM TIPS
---------
- Show both non-recursive (os.listdir) and recursive (os.walk) patterns.
- Use try/except around size calls to be robust.
"""
import os

def folder_size_megabytes():
    folder = input("Enter a folder path: ")
    try:
        names = os.listdir(folder)       # items in the folder (1 level)
    except FileNotFoundError:
        print("Folder not found.")
        return

    total = 0
    for name in names:
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            try:
                total += os.path.getsize(path)
            except OSError:
                pass

    print("Total size:", total/(1024*1024), "MB")

def list_files_over_1gb():
    folder = input("Enter a folder path: ")
    one_gb = 1024 * 1024 * 1024
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            try:
                if os.path.getsize(path) > one_gb:
                    print(path, os.path.getsize(path)/(1024*1024), "MB")
            except OSError:
                pass


# ======================================================
# SECTION 5 — Create, delete, and ZIP files
# ======================================================
"""
GOAL
----
- Create a file and write some text.
- Delete a file using os.remove().
- Compress a file into a .zip using the zipfile module.

WHY ZIP?
--------
ZIP is a very common archive format. You collect files together and compress them, which is
useful for sharing or backups.

KEY FUNCTIONS
-------------
- open(..., "w") to create and write.
- os.remove(path) to delete.
- zipfile.ZipFile("dest.zip", "w") to create a new zip and .write("source").

EXAM TIPS
---------
- Explain the difference between creating/writing and removing.
- Show that you can pick a source file and add it to a zip archive.
"""
import zipfile

def create_and_delete_demo():
    with open("myfile.txt", "w", encoding="utf-8") as f:
        f.write("Sample text\nAnother line")
    print("Created: myfile.txt")

    os.remove("myfile.txt")
    print("Deleted: myfile.txt")

def zip_one_file(source, dest_zip):
    with zipfile.ZipFile(dest_zip, mode="w") as zf:
        zf.write(source, arcname=os.path.basename(source))
    print(f"Compressed '{source}' into '{dest_zip}'.")


# ======================================================
# SECTION 6 — Full console CRUD with pickle persistence (plus UPPER/lower options)
# ======================================================
"""
GOAL
----
Build a menu-driven console program to manage a list of clients using a simple class and
a Python list. Save the list to a file with pickle so it persists between runs.

REQUIREMENTS WE FOLLOW
----------------------
- Class only with properties (+ methods to change case).
- List of clients.
- Menu: insert, list, update, delete, change to UPPERCASE, change to lowercase, exit.
- Use .pop() to delete by index (restriction in your statement).
- Save (pickle) after every insert/update/delete or case-change.

HOW TO THINK ABOUT IT
---------------------
- 'clientes.bin' is your "database" file for this exercise.
- On start: try to load it; if it doesn't exist, start with an empty list.
- Each option is a function. The loop calls the correct function based on user input.

EXAM TIPS
---------
- Welcome message at the start.
- Use while True + if/elif for the menu.
- Use try/except for invalid IDs.
- Respect the "use pop()" rule for deletion.
"""
PICKLE_FILE = "clients.bin"

class Client:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def to_upper(self):
        self.name = self.name.upper()
        self.surname = self.surname.upper()

    def to_lower(self):
        self.name = self.name.lower()
        self.surname = self.surname.lower()

    def __repr__(self):
        return f"Client({self.name!r}, {self.surname!r}, {self.email!r})"

def load_clients():
    try:
        with open(PICKLE_FILE, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
    except Exception:
        return []

def save_clients(clients):
    with open(PICKLE_FILE, "wb") as f:
        pickle.dump(clients, f)

def insert_client(clients):
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")
    clients.append(Client(name, surname, email))
    save_clients(clients)
    print("Client inserted.")

def list_clients(clients):
    for idx, c in enumerate(clients):
        print(f"ID {idx} -> {c.name} {c.surname} {c.email}")

def update_client(clients):
    try:
        idx = int(input("ID to update: "))
        c = clients[idx]
        new_name = input(f"New name ({c.name}): ")
        new_surname = input(f"New surname ({c.surname}): ")
        new_email = input(f"New email ({c.email}): ")
        c.name = new_name or c.name
        c.surname = new_surname or c.surname
        c.email = new_email or c.email
        save_clients(clients)
        print("Client updated.")
    except (ValueError, IndexError):
        print("Invalid ID.")

def delete_client(clients):
    try:
        idx = int(input("ID to delete: "))
        confirm = input("Confirm deletion? (y/n): ")
        if confirm.lower() == "y":
            clients.pop(idx)   # <- required by your statement
            save_clients(clients)
            print("Client deleted.")
        else:
            print("Cancelled.")
    except (ValueError, IndexError):
        print("Invalid ID.")

def all_upper(clients):
    for c in clients:
        c.to_upper()
    save_clients(clients)
    print("All names set to UPPERCASE.")

def all_lower(clients):
    for c in clients:
        c.to_lower()
    save_clients(clients)
    print("All names set to lowercase.")

def clients_menu():
    print("###### Client manager v0.1 ######")
    print("####### Jose Vicente Carratala #######")
    clients = load_clients()

    while True:
        print("\nChoose an option:")
        print("1.-Insert client")
        print("2.-List clients")
        print("3.-Update client")
        print("4.-Delete client")
        print("5.-To UPPERCASE")
        print("6.-To lowercase")
        print("7.-Exit")
        op = input("> ")

        if op == "1":
            insert_client(clients)
        elif op == "2":
            list_clients(clients)
        elif op == "3":
            update_client(clients)
        elif op == "4":
            delete_client(clients)
        elif op == "5":
            all_upper(clients)
        elif op == "6":
            all_lower(clients)
        elif op == "7":
            print("Program finished.")
            break
        else:
            print("Invalid option.")


# ======================================================
# SECTION 7 — Tkinter mini-GUI: sum two numbers and show result
# ======================================================
"""
GOAL
----
Build a tiny window with two input fields, a button, and a label that shows the sum.

HOW TKINTER WORKS
-----------------
- tk.Tk() creates the main window (the application root).
- Widgets like Entry (text inputs), Button, and Label are created and placed in the window.
- The 'command=' of a Button points to a function that runs when clicked.
- .get() reads the current text in an Entry.
- You update the label with .config(text=...).
- .mainloop() starts the event loop so the window responds to clicks and typing.

EXAM TIPS
---------
- Keep it simple: two Entry, one Button, one Label.
- Convert input strings to float (or int) and handle ValueError.
"""
def tkinter_sum_demo():
    try:
        import tkinter as tk
    except ImportError:
        print("tkinter not available in this environment.")
        return

    def calculate():
        try:
            a = float(entry1.get() or "0")
            b = float(entry2.get() or "0")
            result.config(text=f"Total: {a + b}")
        except ValueError:
            result.config(text="Please enter valid numbers.")

    root = tk.Tk()
    root.title("Quick Sum")

    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)
    button = tk.Button(root, text="Calculate", command=calculate)
    result = tk.Label(root, text="Total: 0")

    entry1.pack(padx=10, pady=5)
    entry2.pack(padx=10, pady=5)
    button.pack(padx=10, pady=5)
    result.pack(padx=10, pady=5)

    root.mainloop()


# ======================================================
# SECTION 8 — Tkinter + MySQL (insert rows with a button) — template
# ======================================================
"""
GOAL
----
Create a GUI form that inserts a row into a MySQL table when you click a button.

WHAT YOU NEED BEFORE RUNNING
----------------------------
- MySQL server running locally or accessible.
- A database and a table created (e.g., amigos_gimnasio(name, surname, date)).
- The package 'mysql-connector-python' installed.

LOGIC
-----
- Collect text from Entry widgets.
- Open a DB connection with mysql.connector.connect(...).
- Execute an INSERT with placeholders (%s, %s, %s).
- Commit and close the connection.
- Show a "success" message in a Label.

EXAM TIPS
---------
- Keep credentials outside code in real projects (env vars). For the exam, placeholders are fine.
- Always commit after INSERT/UPDATE/DELETE.
- Show a short success/failure message.
"""
def tkinter_mysql_insert_template():
    try:
        import tkinter as tk
        import mysql.connector
    except ImportError:
        print("tkinter or mysql.connector not available here.")
        return

    def register():
        name = ent_name.get()
        surname = ent_surname.get()
        date = ent_date.get()
        try:
            con = mysql.connector.connect(
                host="localhost", user="useroscar", password="your_password", database="YourDB"
            )
            cur = con.cursor()
            cur.execute(
                "INSERT INTO amigos_gimnasio (nombre, apellidos, fecha) VALUES (%s,%s,%s)",
                (name, surname, date)
            )
            con.commit()
            cur.close(); con.close()
            msg.config(text="Inserted OK.")
        except mysql.connector.Error as e:
            msg.config(text=f"MySQL error: {e}")

    root = tk.Tk(); root.title("MySQL Insert")
    tk.Label(root, text="Name").grid(row=0, column=0, sticky="e")
    tk.Label(root, text="Surname").grid(row=1, column=0, sticky="e")
    tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0, sticky="e")

    ent_name = tk.Entry(root); ent_name.grid(row=0, column=1)
    ent_surname = tk.Entry(root); ent_surname.grid(row=1, column=1)
    ent_date = tk.Entry(root); ent_date.grid(row=2, column=1)

    tk.Button(root, text="Register", command=register).grid(row=3, column=0, columnspan=2, pady=8)
    msg = tk.Label(root, text=""); msg.grid(row=4, column=0, columnspan=2)
    root.mainloop()


# ======================================================
# SECTION 9 — Exam sketch: Console CRUD + Database (MySQL)
# ======================================================
"""
GOAL
----
Produce a small console menu that performs CRUD operations against a MySQL database for
a portfolio schema (Categoria and Pieza with a foreign key).

WHY A SKETCH?
-------------
In the exam, you will likely define your schema in SQL, then write a short Python program
to connect and run queries. Below is a clear skeleton: connection function, simple INSERT
and SELECT, and a minimal menu loop.

EXAM TIPS
---------
- Show a LEFT JOIN and a VIEW when asked in the DB part; in Python, focus on a clean menu.
- Check errors with try/except mysql.connector.Error and print friendly messages.
"""
EXAM_CRUD_SKETCH = r"""
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="useroscar",
        password="your_password",
        database="PortafolioDB"
    )

def insert_category(title, desc):
    cn = connect(); cur = cn.cursor()
    cur.execute("INSERT INTO Categoria(titulo, descripcion) VALUES (%s,%s)", (title, desc))
    cn.commit(); cur.close(); cn.close()

def list_categories():
    cn = connect(); cur = cn.cursor()
    cur.execute("SELECT id, titulo, descripcion FROM Categoria")
    for row in cur.fetchall():
        print(row)
    cur.close(); cn.close()

def menu():
    while True:
        print("1) Insert category  2) List categories  3) Exit")
        op = input("> ")
        if op == "1":
            t = input("Title: "); d = input("Description: ")
            insert_category(t, d)
        elif op == "2":
            list_categories()
        elif op == "3":
            print("Bye"); break
        else:
            print("Invalid option")
"""


# ======================================================
# SECTION 10 — Error handling & practical exam reminders
# ======================================================
"""
WHY EXCEPTIONS?
---------------
Reading/writing files and connecting to databases can fail (missing files, permission
errors, network issues, etc.). Use try/except to handle errors gracefully and keep the
program alive or show a helpful message.

COMMON PATTERNS
---------------
- FileNotFoundError when opening non-existing files in 'r' mode.
- OSError when reading sizes from locked or special files.
- mysql.connector.Error for DB issues (wrong credentials, missing table).

EXAM TIPS
---------
- Wrap file reads in try/except FileNotFoundError (print a friendly message).
- For menus, validate user input and catch ValueError when converting to int.
- Mention persistence (pickle/text/JSON) and explain your choice quickly.
"""

def open_or_create_demo():
    try:
        with open("maybe.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found -> creating a new one.")
        with open("maybe.txt", "w", encoding="utf-8") as f:
            f.write("Created automatically.")


# ======================================================
# __main__ — Uncomment what you want to test locally
# ======================================================
if __name__ == "__main__":
    pass
# --- Agenda ---
# agenda_escribir_contacto()
# agenda_leer_contactos()

# SECTION 0
# file_basics_demo()

# SECTION 1
# agenda_write_contact()
# agenda_read_all()

# SECTION 2
# blog_json_to_html()

# SECTION 3
# foods_write_and_append()
# foods_read_last_line()
# pickle_save_and_load_demo()

# SECTION 4
# folder_size_megabytes()
# list_files_over_1gb()

# SECTION 5
# create_and_delete_demo()
# zip_one_file("example.txt", "example.zip")  # ensure example.txt exists first

# SECTION 6
# clients_menu()

# SECTION 7
# tkinter_sum_demo()

# SECTION 8
# tkinter_mysql_insert_template()

# SECTION 9
# print(EXAM_CRUD_SKETCH)

# SECTION 10
# open_or_create_demo()



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/ALT 001.py
# ====================================================

# ==========================================
# UNIT 1 — Program Basics (Python)
# Topics: blocks & indentation, variables, data types, literals,
# constants (by convention), operators, printing, comments.
# ==========================================

# ---------- 1) BLOCKS & INDENTATION ----------
# Python uses indentation (spaces) to mark code blocks.
# Use 4 spaces per indentation level. Never mix tabs and spaces.

def show_blocks():
    for i in range(3):
        print("Loop index:", i)  # inside the loop block
    # out here -> outside the loop
show_blocks()


# ---------- 2) VARIABLES ----------
# Python creates a variable the moment you assign a value.
# No explicit type declaration required.

greeting = "Hello, World"
age = 25            # int
height = 1.82       # float
is_active = True    # bool

# Reassigning
age = age + 5       # 30
age += 2            # 32
print("age:", age)

# Naming convention: snake_case (lowercase_with_underscores)
user_name = "oscar_sorensen"


# ---------- 3) DATA TYPES ----------
n_int = 7                     # int - int is short for integer (whole number)
n_float = 2.5                 # float
text = "text"                 # str
flag = False                  # bool
items = [1, 2, 3]             # list (mutable sequence)
point = (10, 20)              # tuple (immutable sequence)
prefs = {"theme": "dark"}     # dict (key/value map)
print(type(items), type(prefs))

# Conversions
n_from_str = int("10")        # 10
f_from_str = float("2.5")     # 2.5
s_from_num = str(123)         # "123"
b_from_num = bool(0)          # False (0 -> False; nonzero -> True)


# ---------- 4) LITERALS ----------
answer = 42            # int literal
pi = 3.14159           # float literal
truth = True           # boolean literal
hello = "Hello"        # string literal
multiline = """This is
a multi-line string."""
print(hello, pi, truth)
print(multiline)


# ---------- 5) CONSTANTS (BY CONVENTION) ----------
# Python doesn’t enforce constants; use UPPER_CASE names by convention.
TAX_RATE = 0.21
base_price = 100
total_price = base_price * (1 + TAX_RATE)
print("Total with tax:", total_price)


# ---------- 6) OPERATORS ----------
a, b = 7, 3
# Arithmetic
print(a + b, a - b, a * b, a / b)  # 10 4 21 2.333...
print(a // b)   # floor division -> 2
print(a % b)    # modulus -> 1
print(a ** b)   # exponentiation -> 343

# Comparison -> Boolean
print(a == b, a != b, a > b, a >= b, a < b, a <= b)

# Logical
x, y = True, False
print(x and y, x or y, not x)  # False True False

# Membership
fruits = ["apple", "pear"]
print("apple" in fruits)       # True
print("orange" not in fruits)  # True

# Operator precedence basics: ** > * / // % > + - > comparisons > and > or.
# Use parentheses to make intent explicit in exams.


# ---------- 7) PRINT & COMMENTS ----------
print("Simple output with print()")
# One-line comment
"""
Multi-line comment/docstring-style block.
"""


# ---------- 8) MINI PRACTICE ----------
# Small VAT calculator with formatting
amount = 250
result = amount * (1 + TAX_RATE)
print(f"Amount {amount} -> Total {result:.2f}")

# String formatting examples
name = "Oscar"
print(f"Hello, {name}. Int: {n_int}, Float: {n_float:.2f}")

# !!RELEVANT, BUT NOT FROM CLASS!!
# Quick assert-of-assumptions (unit tests will cover this later)
assert isinstance(result, float)



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/ALT 002.py
# ====================================================

# ==========================================
# UNIT 2 — Working with Objects
# Topics: everything is an object, attributes & methods, instances,
# calling methods with parameters, properties (attributes),
# static methods, simple constructors, basic resource handling.
# ==========================================

# ---------- 1) EVERYTHING IS AN OBJECT ----------
text = "Python DAW"
print(text.upper())   # method (belongs to the string object)
print(len(text))      # built-in function operating on the object

nums = [3, 1, 2]
nums.append(4)        # list method
print(sorted(nums))   # built-in that returns a new sorted list
print(nums)           # original list has [3,1,2,4]

# ---------- 1.2)FUNCTION OR METHOD ----------

# Functions
print(len("Hi"))             # 2
print(sorted([3, 1, 2]))     # [1, 2, 3]
print(sum([1, 2, 3]))        # 6

# Methods
print("hi".upper())          # "HI"
numbers = [3, 1, 2]
numbers.append(4)
print(numbers)               # [3, 1, 2, 4]


# ---------- 2) INSTANCES & NAMESPACES ----------
class Cat:
    pass

my_cat = Cat()        # instance
other_cat = Cat()

# Each instance can carry its own attributes (dynamic in Python)
my_cat.name = "Mishi"
other_cat.name = "Luna"
print(my_cat.name, other_cat.name)   # different namespaces


# ---------- 3) METHODS & PARAMETERS ----------
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print("add:", calc.add(3, 4))


# ---------- 4) PROPERTIES (ATTRIBUTES) ----------
class Customer:
    def __init__(self, name, age):
        self.name = name   # public attribute
        self.age = age

c = Customer("Oscar", 25)
print(f"Customer: {c.name}, age {c.age}")


# ---------- 5) STATIC METHODS ----------
# Static methods don’t use 'self' or object state.

class MathTools:
    @staticmethod
    def double(n):
        return n * 2

print(MathTools.double(5))
mt = MathTools()
print(mt.double(7))  # technically allowed, but prefer calling via class


# ---------- 6) CONSTRUCTORS (BASICS) ----------
from datetime import datetime, date

today = date.today()
now = datetime.now()
print("Today:", today.isoformat(), "Now:", now.strftime("%Y-%m-%d %H:%M:%S"))

class Order:
    def __init__(self, customer, total, created_at=None):
        self.customer = customer
        self.total = float(total)
        self.created_at = created_at or datetime.now()

order = Order("Oscar", 99.9)
print("Order:", order.customer, order.total, order.created_at)


# ---------- 7) RESOURCE MANAGEMENT ----------
# Use 'with' to ensure resources are released automatically.
with open("unit2_output.txt", "w") as f:
    f.write("Resource released automatically when leaving 'with' block.\n")


# !!RELEVANT, BUT NOT FROM CLASS!!
# ---------- 8) classmethod vs staticmethod ----------
class Example:
    factor = 10

    @classmethod
    def from_factor(cls, n):
        # Uses the class (cls). Often used for alternate constructors.
        return n * cls.factor

    @staticmethod
    def triple(n):
        return 3 * n

print("from_factor:", Example.from_factor(2))  # 20
print("triple:", Example.triple(3))            # 9



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/ALT 003.py
# ====================================================

# ==========================================
# UNIT 3 — Control Structures
# Topics: if/elif/else, loops (for/while), break/continue/pass,
# exceptions (try/except/else/finally), assertions, small refactors.
# ==========================================

# ---------- 1) SELECTION (if / elif / else) ----------
x = 10
if x > 10:
    msg = "Greater than 10"
elif x == 10:
    msg = "Equal to 10"
else:
    msg = "Less than 10"
print("selection:", msg)

age = 20
has_license = True
if age >= 18 and has_license:
    print("Can drive")


# ---------- 2) LOOPS ----------
# for with range
for i in range(3):  # 0, 1, 2
    print("for i:", i)

# while
counter = 0
while counter < 3:
    print("while counter:", counter)
    counter += 1

# Accumulator pattern
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print("sum:", total)

# Looping over lists directly
words = ["alpha", "beta", "gamma"]
for w in words:
    print("word:", w)


# ---------- 3) JUMP STATEMENTS ----------
for n in range(1, 8):
    if n == 3:
        continue   # skip this iteration
    if n == 6:
        break      # exit the loop
    if n == 2:
        pass       # placeholder (does nothing)
    print("n:", n)


# ---------- 4) EXCEPTIONS ----------
# try: attempt risky code
# except: handle specific failure gracefully
# else: runs only if no exception
# finally: runs always (cleanup)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: division by zero", e)
        return None
    except TypeError as e:
        print("Type error:", e)
        return None
    else:
        return result
    finally:
        # e.g., close resources if needed
        pass

print("safe_divide 10/2:", safe_divide(10, 2))
print("safe_divide 1/0:", safe_divide(1, 0))

# Pattern from your average exercise:
gym_days = []  # try [] and [1,3,4,0,2]
try:
    avg_days = sum(gym_days) / len(gym_days)
except ZeroDivisionError:
    avg_days = 0.0  # numeric fallback (keeps type numeric)
print("avg_days:", avg_days)

# Explanation (very important to remember):
# 1) Python tries the 'try' block.
# 2) If an error happens (e.g., division by zero), it jumps to the matching 'except'.
# 3) The 'except' block runs (assign 0.0) and the program continues normally.


# ---------- 5) ASSERTIONS ----------
# Assert states assumptions. If false, raises AssertionError.
def sqrt_non_negative(x):
    assert x >= 0, "x must be non-negative"
    return x ** 0.5

print("sqrt_non_negative(9):", sqrt_non_negative(9))
# sqrt_non_negative(-1)  # uncomment to see AssertionError


# ---------- 6) SMALL REFACTOR + DOCSTRINGS ----------
def documented_divide(dividend, divisor):
    """
    Return the quotient dividend/divisor as float.
    Converts inputs to int first; may raise ZeroDivisionError.
    """
    dividend = int(dividend)
    divisor = int(divisor)
    return dividend / divisor

try:
    print("documented_divide:", documented_divide("10", "2"))
except ZeroDivisionError:
    print("Division by zero")

# !!RELEVANT, BUT NOT FROM CLASS!!
# List comprehensions and any/all — high-signal shortcuts
evens = [n for n in range(10) if n % 2 == 0]
print("evens:", evens)
print("any > 5:", any(n > 5 for n in evens))
print("all even:", all(n % 2 == 0 for n in evens))



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/ALT 004.py
# ====================================================

# ==========================================
# UNIT 4 — Building Classes (OOP Basics)
# Topics: defining classes, instance attributes & methods,
# visibility conventions, properties (@property), getters/setters,
# constructors (__init__), simple CRUD patterns, inheritance (basics).
# ==========================================

# ---------- 1) DEFINING A CLASS ----------
class Cat:
    def __init__(self, name):
        self.name = name  # instance attribute

    def meow(self):
        return f"{self.name} says meow"

mishi = Cat("Mishi")
print(mishi.meow())


# ---------- 2) VISIBILITY CONVENTIONS ----------
# Python doesn't enforce private; use naming conventions:
# _name  -> "protected" by convention (don’t touch from outside)
# __name -> name-mangled (avoids accidental collisions)

class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self._balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def balance(self):
        return self._balance

acct = BankAccount("Oscar", 100)
acct.deposit(50)
acct.withdraw(25)
print("Balance:", acct.balance())


# ---------- 3) PROPERTIES (@property) ----------
# Idiomatic Python accessors (instead of manual get_/set_ methods)

class Customer:
    def __init__(self, name, phones=None):
        self._name = name
        self._phones = list(phones or [])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name:
            self._name = new_name

    @property
    def phones(self):
        return self._phones

    def add_phone(self, p):
        if isinstance(p, str) and p:
            self._phones.append(p)

cli = Customer("Oscar")
cli.add_phone("600123123")
print(cli.name, cli.phones)


# ---------- 4) METHODS (getters/setters style) ----------
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name:
            self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price >= 0:
            self._price = float(price)

p = Product("Coffee", 2.5)
p.set_price(2.8)
print(p.get_name(), p.get_price())


# ---------- 5) CONSTRUCTORS (__init__) ----------
class Order:
    def __init__(self, order_id, customer, items=None):
        self.order_id = order_id
        self.customer = customer
        self.items = list(items or [])

    def add_item(self, name, price):
        self.items.append((name, float(price)))

    def total(self):
        return sum(price for _, price in self.items)

order = Order(1, "Oscar")
order.add_item("Apple", 1.2)
order.add_item("Bread", 0.8)
print("Order total:", order.total())


# ---------- 6) SIMPLE IN-MEMORY CRUD ----------
class CustomerManager:
    def __init__(self):
        self._customers = []

    def insert(self, customer: Customer):
        self._customers.append(customer)

    def list_all(self):
        for c in self._customers:
            print("-", c.name, c.phones)

mgr = CustomerManager()
mgr.insert(Customer("Ana", ["600111222"]))
mgr.insert(Customer("Luis"))
mgr.list_all()


# ---------- 7) INHERITANCE (BASICS) ----------
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return "woof"

dog = Dog("Toby")
print(dog.name, dog.sound())


# !!RELEVANT, BUT NOT FROM CLASS!!
# ---------- 8) dataclasses (less boilerplate for data containers) ----------
from dataclasses import dataclass, field

@dataclass
class Article:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)

a = Article("Notebook", 3.5)
a.tags.append("stationery")
print(a)



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/exampractice.py
# ====================================================

# ==========================================
# Object Practice File
# Author: Oscar Sørensen
# Description:
#   Contains simple object-oriented examples
#   for studying Units 2–3 (CEAC DAW).
# ==========================================


# ---------- Example 1: Fruit ----------
class Fruit:
    def __init__(self, kind):
        self.kind = kind

    def kind_is(self):
        print("the kind is", self.kind)


f1 = Fruit("Banana")
f1.kind_is()

f2 = Fruit("Apple")
f2.kind_is()



# ---------- Example 2: Basic Book ----------
class Book:
    def __init__(self, title):
        self.title = title

    def title_is(self):
        print("the title is", self.title)


t1 = Book("Book one")
t1.title_is()

t2 = Book("Book two")
t2.title_is()



# ---------- Example 3: Book with change_title ----------
class Book:
    def __init__(self, title):
        self.title = title

    def title_is(self):
        print("the title is", self.title)

    def change_title(self, new_title):
        self.title = new_title


b1 = Book("Old title")
b1.title_is()

b1.change_title("New title")
b1.title_is()

# ==========================================
# Example 4: Static Methods (Converter)
# Author: Oscar Sørensen
# Description:
#   Demonstrates how to use @staticmethod in a class.
#   Static methods belong to the class, not to individual objects.
#   They do not use "self" and are often used for general calculations.
# ==========================================

class Converter:
    # ---------- Static Methods ----------
    # Static methods do not need "self"
    # They can be called using the class name directly.

    @staticmethod
    def km_to_miles(km):
        # Converts kilometers to miles
        # 1 kilometer = 0.621371 miles
        return km * 0.621371

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        # Converts Celsius to Fahrenheit
        # Formula: (C × 9/5) + 32
        return (celsius * 9/5) + 32


# ---------- Example Usage ----------
# Static methods are called directly from the class name.
# No object creation is required.

print("10 kilometers is", Converter.km_to_miles(10), "miles")
print("25°C is", Converter.celsius_to_fahrenheit(25), "°F")

# Output:
# 10 kilometers is 6.21371 miles
# 25°C is 77.0 °F

# ==========================================
# Example 5: Working with Built-in Objects
# Author: Oscar Sørensen
# Description:
#   Demonstrates that strings, lists, and dictionaries
#   are objects with their own methods.
# ==========================================


# ---------- STRING OBJECT ----------
text = "hello world"

# Methods that belong to the string object
print("Uppercase:", text.upper())       # 'HELLO WORLD'
print("Lowercase:", text.lower())       # 'hello world'
print("Replace:", text.replace("world", "Oscar"))  # 'hello Oscar'
print("Split:", text.split())           # ['hello', 'world']

# len() is a global function, not a method
print("Length:", len(text))             # 11


# ---------- LIST OBJECT ----------
numbers = [3, 1, 4]
print("Original list:", numbers)

# List methods
numbers.append(2)                       # add at the end
print("After append:", numbers)

numbers.sort()                          # sort in place
print("After sort:", numbers)

numbers.remove(1)                       # remove a value
print("After remove:", numbers)

# len() works on lists too
print("List length:", len(numbers))


# ---------- DICTIONARY OBJECT ----------
person = {"name": "Oscar", "age": 25, "country": "Spain"}

# Dictionary methods
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# Access and modify values
print("Name:", person["name"])
person["age"] = 26
print("Updated age:", person["age"])

# Add a new key/value pair
person["language"] = "Python"
print("New dictionary:", person)


# ---------- SUMMARY ----------
# Strings, lists, and dictionaries are all objects.
# Each one has its own set of methods you can call with a dot (.)
# Example: text.upper(), numbers.append(), person.keys()

# !!RELEVANT, BUT NOT FROM CLASS!!
# Some other useful built-in objects:
#   set()  -> unique elements, supports .add() and .remove()
#   tuple  -> immutable ordered collection



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/for2-3.py
# ====================================================

# ==========================================
# EXAM NOTES — UNIDAD 2 & 3 (CEAC DAW)
# Author: Oscar Sørensen
# ==========================================
# These notes summarize everything needed for
# Units 2 (Objects) and 3 (Control Structures)
# for the CEAC "Programación" exam.
# ==========================================


# ==========================================
# --------- UNIT 2 — WORKING WITH OBJECTS ----------
# ==========================================

# ----- CLASSES AND OBJECTS -----
# A class is a blueprint. An object is a specific example.

class Book:
    def __init__(self, title):
        self.title = title          # Attribute belongs to the object

    def show_title(self):
        print("The title is", self.title)


b1 = Book("Example Book")
b1.show_title()


# ----- CONSTRUCTOR -----
# Runs automatically when an object is created.
# Always named __init__.

class Example:
    def __init__(self, value):
        self.value = value


# ----- ATTRIBUTES -----
# Variables that belong to the object.
# Access with self.attribute inside the class,
# or object.attribute outside the class.
x = Example(5)
print("Value:", x.value)


# ----- METHODS -----
# Functions defined inside a class.
# They always have "self" as the first parameter.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


p = Person("Oscar")
p.greet()


# ----- STATIC METHODS -----
# Do not depend on object data.
# Use @staticmethod decorator.
# Called directly from the class.

class Converter:
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


print("10 km =", Converter.km_to_miles(10), "miles")
print("25°C =", Converter.celsius_to_fahrenheit(25), "°F")


# ----- BUILT-IN OBJECTS -----
# Strings, lists, and dictionaries are objects with their own methods.

text = "hello world"
print("Uppercase:", text.upper())
print("Replace:", text.replace("world", "Oscar"))

nums = [3, 1, 2]
nums.append(4) # add element- here 4
nums.sort()
print("List:", nums)

person = {"name": "Oscar", "age": 25}
person["age"] = 26
print("Dictionary:", person)

# !!RELEVANT, BUT NOT FROM CLASS!!
# tuple = immutable ordered collection
# set()  = unordered unique elements


# ==========================================
# --------- UNIT 3 — CONTROL STRUCTURES ----------
# ==========================================

# ----- CONDITIONALS -----
x = 10
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")

# Operators:
# ==  !=  >  <  >=  <=
# and / or / not


# ----- LOOPS -----
# FOR LOOP
for i in range(3):
    print("for i:", i)

# WHILE LOOP
count = 0
while count < 3:
    print("while:", count)
    count += 1


# ----- JUMP STATEMENTS -----
for n in range(1, 6):
    if n == 3:
        continue    # skip this number
    if n == 5:
        break       # stop completely
    print("n =", n)


# ----- TRY / EXCEPT -----
# Used to handle errors without stopping the program.
# Must have at least one except.

try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0
print("Result:", result)


# ----- MULTIPLE EXCEPTIONS -----
try:
    x = int("abc")
    y = 10 / x
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Conversion error")


# ----- ASSERTIONS -----
# Used to check assumptions during runtime.
def positive_square_root(n):
    assert n >= 0, "n must be non-negative"
    return n ** 0.5


print("sqrt(9) =", positive_square_root(9))
# positive_square_root(-1)  # would raise AssertionError


# ----- SMALL PRACTICAL EXAMPLE -----
def safe_divide(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        return 0.0
    except ValueError:
        return "Error: not a number"


print("safe_divide(6, 3) =", safe_divide(6, 3))
print("safe_divide(4, 0) =", safe_divide(4, 0))
print("safe_divide(4, 'a') =", safe_divide(4, "a"))


# ----- FINAL REMINDERS -----
# - Always indent with 4 spaces
# - Use clear variable names
# - Each "if", "for", "while", "def" ends with a colon :
# - Use print() to show results, not return (unless asked)
# - No nested if unless required
# - Use try/except instead of big conditional chains when checking errors
# - Focus on clarity and correctness, not shortcuts



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/notes.py
# ====================================================

# ==========================================
#  PYTHON CHEAT SHEET – OSCAR SØRENSEN
#  Updated: 29 October 2025
# ==========================================

# ---------- 1. VARIABLES & TYPES ----------
x = 5           # int
y = 3.5         # float
name = "Oscar"  # str
active = True   # bool

# check data type
print(type(x))

# type conversion
a = int("10")
b = float("3.14")
c = str(123)
d = bool(1)

# ---------- 2. INPUT / OUTPUT ----------
# input() always returns a string
nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
print("Hola,", nombre, "tienes", edad, "años.")

# ---------- 3. LISTS ----------
dias = [1, 3, 4, 0, 2]
print(dias[0])       # first element
print(len(dias))     # number of elements
print(sum(dias))     # sum of all elements
dias.append(5)       # add new element
dias.remove(0)       # remove element by value

# ---------- 4. LOOPS ----------
# for loop
for numero in range(1, 6):
    print("Número:", numero)

# while loop
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# ---------- 5. CONDITIONS ----------
x = 10
if x > 5:
    print("Mayor que 5")
elif x == 5:
    print("Igual a 5")
else:
    print("Menor que 5")

# ---------- 6. FUNCTIONS ----------
def saludar(nombre):
    print("Hola,", nombre)

saludar("Oscar")

# function with return value
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print("Resultado:", resultado)

testtest
# ---------- 7. EXCEPTION HANDLING ----------
# try / except prevents the program from crashing
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes introducir un número válido.")
finally:
    print("Fin del programa.")

# ---------- 8. STRINGS ----------
texto = "Hola Mundo"
print(texto.lower())   # hola mundo
print(texto.upper())   # HOLA MUNDO
print(texto[0:4])      # Hola
print(len(texto))      # 10

# ---------- 9. FILES (BÁSICO) ----------
# writing to a file
with open("archivo.txt", "w") as f:
    f.write("Hola desde Python.\n")

# reading a file
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# ---------- 10. COMMON BUILT-IN FUNCTIONS ----------
# sum(), len(), range(), type(), print(), input(), int(), float(), str()
# round(), min(), max(), abs(), sorted()

# ---------- 11. COMMENTS ----------
# one-line comment
"""
multi-line
comment
"""

# ---------- 12. SMALL REFERENCE EXAMPLES ----------

# average of list values
dias_al_gimnasio = [1, 3, 4, 0, 2]
try:
    promedio = sum(dias_al_gimnasio) / len(dias_al_gimnasio)
    print("Promedio:", promedio)
except ZeroDivisionError:
    print("No hay datos disponibles")

# dictionary example
persona = {"nombre": "Oscar", "edad": 25, "activo": True}
print(persona["nombre"])
print(persona.keys())
print(persona.values())

# end of cheat sheet
# ==========================================



# ==========================================
# PYTHON OPERATORS CHEAT SHEET
# ==========================================

# ---------- 1. COMPARISON OPERATORS ----------
# Used to compare two values. They always return True or False.

x = 5
y = 3

print(x == y)   # Equal to → False (5 is not equal to 3)
print(x != y)   # Not equal to → True (5 is different from 3)
print(x > y)    # Greater than → True
print(x < y)    # Less than → False
print(x >= y)   # Greater than or equal → True
print(x <= y)   # Less than or equal → False

# You can use these in if-statements:
if x != 0:
    print("x is not zero")

# ---------- 2. LOGICAL OPERATORS ----------
# Used to combine multiple conditions.

a = True
b = False

print(a and b)  # True if both are True → False
print(a or b)   # True if at least one is True → True
print(not a)    # Negates (inverts) a value → False

# Example:
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")

# ---------- 3. ASSIGNMENT OPERATORS ----------
# Used to store or modify variable values.

x = 10      # Assigns 10
x += 5      # Add and assign → x = x + 5 → 15
x -= 3      # Subtract and assign → x = x - 3 → 12
x *= 2      # Multiply and assign → x = x * 2 → 24
x /= 4      # Divide and assign → x = x / 4 → 6.0
x %= 4      # Modulus and assign → x = x % 4 → remainder after division
print(x)

# ---------- 4. MEMBERSHIP OPERATORS ----------
# Check if something is inside a list, string, or other sequence.

frutas = ["manzana", "pera", "plátano"]
print("manzana" in frutas)      # True
print("naranja" not in frutas)  # True

# ---------- 5. IDENTITY OPERATORS ----------
# Check if two variables refer to the same object in memory (rarely needed for CEAC-level work).

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (same object)
print(a is c)   # False (same values, different object)
print(a is not c) # True

# ---------- 6. COMMON COMBINATIONS ----------
edad = 20
if edad > 0 and edad < 120:
    print("Edad válida")

numero = 0
if numero != 0:
    print("No es cero")
else:
    print("Es cero")

# end of cheat sheet
# ==========================================



# ====================================================
# Contenido original de: Programacion/Python Notes/Uorganiserede noter/syntax.py
# ====================================================

# ==========================================
# PYTHON EXAM SYNTAX DISCIPLINE CHECKLIST
# Oscar Sørensen – CEAC DAW
# ==========================================
# Purpose: eliminate careless syntax errors and structure mistakes.
# Focus on: indentation, naming, function layout, control flow, exceptions.
# ==========================================


# ---------- 1) INDENTATION ----------
# • Always 4 spaces per block (NEVER tabs).
# • Blocks must align vertically — every def, if, for, while, etc.
#   must have its body indented exactly one level.
# • VS Code: enable "Render Whitespace" and "Tab Size: 4".
# • Press Shift + Tab to move code LEFT; Tab to move it RIGHT.

def example_indentation():
    for i in range(3):
        print(i)
    print("Done")  # aligned back to function scope


# ---------- 2) CLEAN NAMING ----------
# • Use lowercase_with_underscores for variables/functions.
# • Use CapitalizedWords for classes.
# • Constants in ALL_CAPS.
# • Avoid Spanish/accents/spaces in names (safe ASCII only).
tax_rate = 0.21
def calc_total(base): return base * (1 + tax_rate)
class Customer: pass
MAX_USERS = 10


# ---------- 3) PRINTING & STRINGS ----------
# • Always wrap text in quotes; prefer f-strings.
# • Use commas in print() instead of concatenation when stressed.
name = "Oscar"
print("Hello,", name)
print(f"Hello, {name}!")     # preferred
print("Value:", 10 * 2)


# ---------- 4) IF / ELIF / ELSE ----------
# • Every if-block must end with a colon.
# • elif and else aligned with their if.
x = 10
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")


# ---------- 5) LOOPS ----------
# • for i in range(n): standard counting loop.
# • while condition: needs counter increment inside.
# • Avoid infinite loops unless specifically asked (use break).

for i in range(3):
    print("Loop", i)

counter = 0
while counter < 3:
    print("While", counter)
    counter += 1


# ---------- 6) FUNCTIONS ----------
# • Define with def name(params): (colon mandatory)
# • Return when you need the value later.
# • Keep all code inside one indentation level.

def add(a, b):
    return a + b

result = add(3, 4)
print("Result:", result)


# ---------- 7) TRY / EXCEPT ----------
# • try must have at least one except.
# • No nested ifs unless required.
# • Keep exception types specific (ZeroDivisionError, ValueError).

try:
    x = int(input("Enter number: "))  # only if exam asks for input
    y = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid number")
else:
    print("Result:", y)
finally:
    print("Program finished")

# Example pattern for assignments like average calculator:
data = []
try:
    avg = sum(data) / len(data)
except ZeroDivisionError:
    avg = 0.0
print("Average:", avg)


# ---------- 8) ASSERTIONS ----------
# • Quick validation tool. Use to confirm preconditions.
def sqrt_positive(n):
    assert n >= 0, "n must be non-negative"
    return n ** 0.5


# ---------- 9) CLASS STRUCTURE ----------
# • Always define __init__ correctly.
# • Every method’s first argument must be self.
# • Keep consistent indentation across methods.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total(self, quantity):
        return self.price * quantity

item = Product("Pen", 1.5)
print(item.get_total(3))


# ---------- 10) FILE EXECUTION & ORDER ----------
# • Don’t leave stray code at the top.
# • Wrap test code under this guard to avoid auto-execution on import:
if __name__ == "__main__":
    print("Ready for exam testing.")


# ---------- 11) DEBUGGING QUICKLY ----------
# • SyntaxError → check for missing colon or indentation mismatch.
# • IndentationError → highlight, Shift+Tab or Tab correctly.
# • NameError → variable not defined or typo.
# • TypeError → wrong data type (use int(), float(), str() as needed).
# • Use print() for quick inspection, then remove it before submitting.

# Example:
value = "10"
print(type(value))
value = int(value)
print(type(value))


# ---------- 12) LAST-MINUTE SANITY CHECK ----------
# • Run the file once before submitting.
# • Make sure output matches exercise request exactly.
# • No untranslated comments unless asked.
# • No leftover debug prints.
# • Keep code simple: one function, one loop, clear logic.


# !!RELEVANT, BUT NOT FROM CLASS!!
# 13) WHEN STRESSED: THE 5-LINE STRUCTURE TEMPLATE
# ------------------------------------------------
# def main():
#     try:
#         # logic
#     except Exception as e:
#         print("Error:", e)
#     else:
#         print("Success")
#
# if __name__ == "__main__":
#     main()



# ====================================================
# Contenido original de: Programacion/Python Notes/specifikeksamen.py
# ====================================================

# ==============================================================
# HOW TO USE THIS TEMPLATE (EXAM INSTRUCTIONS)
# ==============================================================
# 1) This is a universal CRUD program ready for exam use.
#    It connects to MySQL and performs Create, Read, Update, Delete.
#
# 2) Change only names to match the exam theme:
#      examdb     →  your database (e.g. blog, journal, ads)
#      category   →  main table (e.g. autores, usuarios)
#      item       →  secondary table (e.g. entradas, anuncios)
#
# 3) What’s already included:
#    - MySQL connection setup
#    - Full CRUD functions (Create, Read, Update, Delete)
#    - Infinite menu loop with if/elif structure
#    - Clean console output
#
# 4) How to test:
#    - Run the SQL template first to create the DB and user
#    - Then execute this Python file in VS Code terminal
#    - Check results with "Read" (option 2)
#
# 5) To adapt fast in exam:
#    a) Ctrl+H to rename table and field names
#    b) Add/remove fields if needed
#    c) Verify connection (no errors on startup)
#
# 6) Compatible with MySQL 8 and Python 3 (CEAC exam setup)
# ==============================================================

import mysql.connector

# ---------- 1) DATABASE CONNECTION ----------
config = {
    "host": "localhost",
    "user": "exam_user",     # same as in SQL script
    "password": "1234",
    "database": "examdb"     # change to your database name
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# ---------- 2) CRUD FUNCTIONS ----------

def create_item():
    title = input("Title: ")
    category_id = input("Category ID: ")
    content = input("Content: ")
    sql = "INSERT INTO item (title, category_id, date, image, content) VALUES (%s, %s, CURDATE(), '', %s)"
    cursor.execute(sql, (title, category_id, content))
    db.commit()
    print("Record created successfully.")

def read_items():
    cursor.execute("SELECT item.id, item.title, category.name FROM item LEFT JOIN category ON item.category_id = category.id")
    results = cursor.fetchall()
    for row in results:
        print(row)

def update_item():
    item_id = input("ID to update: ")
    new_title = input("New title: ")
    sql = "UPDATE item SET title=%s WHERE id=%s"
    cursor.execute(sql, (new_title, item_id))
    db.commit()
    print("Record updated successfully.")

def delete_item():
    item_id = input("ID to delete: ")
    sql = "DELETE FROM item WHERE id=%s"
    cursor.execute(sql, (item_id,))
    db.commit()
    print("Record deleted successfully.")

# ---------- 3) MENU LOOP ----------

def menu():
    while True:
        print("\n=== CONTROL PANEL ===")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            create_item()
        elif option == "2":
            read_items()
        elif option == "3":
            update_item()
        elif option == "4":
            delete_item()
        elif option == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

# ---------- 4) START PROGRAM ----------

if __name__ == "__main__":
    print("Welcome to the CRUD control panel.")
    menu()
    cursor.close()
    db.close()



# ====================================================
# Contenido original de: __MACOSX/Programacion/001. Identificacion de los elementos/Scripts/._stortprogram.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/002. Utilazicion de objetos/005 Methodos estaticos/._001 gato.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/002. Utilazicion de objetos/005 Methodos estaticos/._002 matematicas.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/002. Utilazicion de objetos/005 Methodos estaticos/._003 metodo pseudo.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/002. Utilazicion de objetos/005 Methodos estaticos/._004 metodo estatico.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._005-for.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._006-else.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._007-masanaditation.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._017-functions.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._26.9.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._Prueba.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._codigoanadido.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._creo.un.gato.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._divisor.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._elseif.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._infopytho.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._pythonstart.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/003. Uso de estructuras/Python/start python first week/._test.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._001regraso de los metodos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._002propiedad.privada.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._006-applicacion.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._10.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._crud.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._declarations.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._proeidades.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._test.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/004-Desarollo/._testafflask.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._007gatocliente.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._ahoraleemos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._bookleinfinito.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._clasematematic2.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._clasematematicas.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._escribirtexto.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._gato.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005-constructores/._gatosperros.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005classeCuentaBancaria/._001.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/005classeCuentaBancaria/._010.clasepractico.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/006-Librerias/._003.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/006-Librerias/._2001.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/006-Librerias/._import.json.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/004. Desarollo de classes/006-Librerias/._testflask.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/003 open and close files/._001.escribir.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/003 open and close files/._002.leer. una linea.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/003 open and close files/._007 pickle escribir.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/003 open and close files/._008 pickle read.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/003 open and close files/._009 crear cliente.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/003 open and close files/._010 gurado con pickle.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/003 open and close files/._011 recupoero los datos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._001 listar contenido.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._002 atributos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._004 suma taman╠âo.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._005  revisar carpeta.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._006 taman╠âo recursivo.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._007 condicion.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._008 escribir archivo.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._010-minibuscador.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._011 busca mapa.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/004 ulilizacion de los sistemas de ficheros/._012 usuario busca.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._001.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._002 micarpeta.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._004.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._005 miarchivo.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._006 deletearchivo.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._007 nuevoarchivo.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._008 comprimir.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._009 -2 compresion.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._009 tests.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._010 comprimir.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._011 comprimir carpeta.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._012 ejercito final.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/005 creacion y eli de fichas/._013 with gpt.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._003 creamos un contructor.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._004 contructor con parametros.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._005 pantalla de bienvenida.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._006 bucle infinito.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._007 creamos lista entidades.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._008 creamos menu.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._009 atrapamos las opciones.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._010 desarollamos insertar clientes.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._011 aprendicamos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._012 pass de momento.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._013 desarollo leer.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._014 imprimimos mejor el cliente.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._015 actualizar es como insertar con id.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._016 chivamos el id.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._017 eliminar elemento.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._018 guardamos con pickle.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._019 guardamos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/006 How to pass trimester Exam/._020 version gpt.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/._001 tkinter NameSpaces.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/._003 tk inter command.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/._004 ponemos etiqueta.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/._006 salida pantalla.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/._007 microcalculadora.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/007 Interfaces graficas/._008 calcular.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._001.marcos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._003 creo un entry.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._004 creo un boton.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._005 funcion insertar.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._006 mysql.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._008 seleccionar.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._009 insertar.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._010 leer de bases de daots.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._011 pintamos tablas.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._012 frankenstein.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/005.Lectura y escritura de informacion/008 Concepto de evento/._013 con ia.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/001-Identificacio╠ün de los elementos de un programa informa╠ütico/._101-Ejercicio de final de unidad.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/002-Utilizacio╠ün de objetos/._005-Utilizacio╠ün de me╠ütodos esta╠üticos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/002-Utilizacio╠ün de objetos/._101-Ejercicio de final de unidad.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/002-Utilizacio╠ün de objetos/._mockExam002.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/._004-Control de excepciones.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/._005-Aserciones.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/._006-Prueba, depuracio╠ün y documentacio╠ün.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/._101-Ejercicio de final de unidad.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/003-Uso de estructuras de control/._mockExam003.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._001-Concepto de clase.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._002-Estructura y miembros de una clase.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._003-Creacio╠ün de propiedades.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._004-Creacio╠ün de me╠ütodos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._005-Creacio╠ün de constructores.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._006-Utilizacio╠ün de clases y objetos.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._007-Utilizacio╠ün de clases heredadas.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/004-Desarrollo de clases/._UnitExam.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/._001-Flujos. Tipos bytes y caracteres.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/._003-Apertura y cierre de ficheros.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/._004-Utilizacio╠ün de los sistemas de ficheros.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/._005-Creacio╠ün y eliminacio╠ün de ficheros y directorios.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/._007-Interfaces gra╠üficas.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/._008-Concepto de evento.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/._unitExam.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Jocarsa Opgaver/005-Lectura y escritura de informacio╠ün/002-ficheros de datos/._leer_blog.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/._UNIT005_Deep_Explained_StudyGuide.py
# ====================================================

    Mac OS X            	   2                                             ATTR                               H  com.apple.macl     L   C  %com.apple.metadata:kMDItemWhereFroms        com.apple.provenance      ;  com.apple.quarantine  53D` fJ똬ڌ                                    bplist00_https://chatgpt.com/
                            ! }
q/0281;690f306f;Brave;F31F43CC-17C9-4FDC-89C1-C6385DA5300C 


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/._specifikeksamen.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/NotesGenByFiles/._001_Elementos_Explained.py
# ====================================================

    Mac OS X            	   2                                             ATTR                               H  com.apple.macl     L   C  %com.apple.metadata:kMDItemWhereFroms        com.apple.provenance      ;  com.apple.quarantine  53D`                                                      bplist00_https://chatgpt.com/
                            ! }
q/0281;69075276;Brave;8989A8E3-401E-48EE-BB9A-754912452992 


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/NotesGenByFiles/._002_Objetos_Explained.py
# ====================================================

    Mac OS X            	   2                                             ATTR                               H  com.apple.macl     L   C  %com.apple.metadata:kMDItemWhereFroms        com.apple.provenance      ;  com.apple.quarantine  53D`                                                      bplist00_https://chatgpt.com/
                            ! }
q/0281;69075279;Brave;CBA37C95-9E79-4EAC-87AC-A8DC56943FEF 


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/NotesGenByFiles/._003_Estructuras_de_control_Explained.py
# ====================================================

    Mac OS X            	   2                                             ATTR                               H  com.apple.macl     L   C  %com.apple.metadata:kMDItemWhereFroms        com.apple.provenance      ;  com.apple.quarantine  53D`                                                      bplist00_https://chatgpt.com/
                            ! }
q/0281;6907527b;Brave;8095A2DE-7DAF-49B4-A35C-59E6C47FCCFE 


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/NotesGenByFiles/._004_Desarrollo_de_clases_Explained.py
# ====================================================

    Mac OS X            	   2                                              ATTR            S                     H  com.apple.macl           com.apple.provenance  53D`                                                       }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/NotesGenByFiles/._005_Lectura_y_escritura_Explained.py
# ====================================================

    Mac OS X            	   2                                             ATTR                               H  com.apple.macl     L   C  %com.apple.metadata:kMDItemWhereFroms        com.apple.provenance      ;  com.apple.quarantine  53D`                                                      bplist00_https://chatgpt.com/
                            ! }
q/0281;69075281;Brave;2D4D2909-6D18-4EB2-A3C6-4B9E91D69D42 


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/NotesGenByFiles/._Programacion_001-005_Explained_All.py
# ====================================================

    Mac OS X            	   2                                             ATTR                               H  com.apple.macl     L   C  %com.apple.metadata:kMDItemWhereFroms        com.apple.provenance      ;  com.apple.quarantine  53D`                                                      bplist00_https://chatgpt.com/
                            ! }
q/0281;69075285;Brave;92C99FC2-E269-441B-AFE4-B5D89E1F836D 


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/NotesGenByFiles/._zEXTRA_UNIT_004_005_006_NOTES.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._ALT 001.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._ALT 002.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._ALT 003.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._ALT 004.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._exampractice.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }



# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._for2-3.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._notes.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  w4.$


# ====================================================
# Contenido original de: __MACOSX/Programacion/Python Notes/Uorganiserede noter/._syntax.py
# ====================================================

    Mac OS X            	   2   q                                            ATTR                                    com.apple.provenance  }
