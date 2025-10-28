class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola,", self.nombre, self.edad)

    
    def saludarmenos(self):
        print("Hola,", self.nombre)
    
   

p1 = Persona("Oscar", 24)
p1.saludar()   # prints: Hola, Oscar

p2 = Persona("Ana", 30)
p2.saludar()   # prints: Hola, Ana

p1.saludarmenos()  # prints: Hola, Oscar
