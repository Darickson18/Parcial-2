class vehiculo:
    def __ init __ (marca,modelo):
    self.marca = marca
    self.modelo = modelo

def descripcion(self):
    return f"{self.marca}, modelo: {self.modelo}"

class coche(vehiculo):
    def __ init __ (self.modelo):
    super().__ init __ (modelo)
    self.ruedas = 4

    mi_coche = coche ("Toyota Corolla")
    print(mi_coche.descripcion())

    ¿Cuál es el bug en este código?
La clase Coche intenta heredar de una clase (Vehiculo) que no está definida.
El método descripcion() no existe en ninguna de las clases definidas.
El método __init__ de la clase Vehiculo está mal definido. Respuesta correcta
Falta definir el atributo ruedas en la clase Vehiculo.
