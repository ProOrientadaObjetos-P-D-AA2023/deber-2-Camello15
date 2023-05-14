"""

"""
# Crear dos objetos de la clase 01

# objeto 01

# crear

# Presentar objeto; usar el método __st__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
      
      persona1 = Persona("Juan", 30)
persona2 = Persona("Maria", 25)

print(persona1)
print(persona2)

# objeto 02

# crear ingresando valores por teclado

# Presentar objeto; usar el método __st__

class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad}"

nombre = input("Ingrese el nombre de la mascota: ")
tipo = input("Ingrese el tipo de mascota: ")
edad = int(input("Ingrese la edad de la mascota: "))

mascota = Mascota(nombre, tipo, edad)

print(mascota)
