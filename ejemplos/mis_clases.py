"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")
    
    def cumplir_anios(self):
        self.edad += 1
        print("¡Feliz cumpleaños! Ahora tengo", self.edad, "años.")


# clase 02 
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def presentarse(self):
        print("Hola, soy", self.nombre, "un", self.especie, "de", self.edad, "años.")
    
    def cumplir_anios(self):
        self.edad += 1
        print("¡Feliz cumpleaños! Ahora tengo", self.edad, "años.")
