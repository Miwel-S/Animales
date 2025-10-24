from domain.ObservableValue import ObservableValue

class Animal:
    def __init__(self, nombre, edad, raza, tipo):
        self.nombre = ObservableValue(nombre)
        self.edad = ObservableValue(edad)
        self.raza = ObservableValue(raza)
        self.tipo = tipo

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre.value = nuevo_nombre

    def cambiar_edad(self, nueva_edad):
        self.edad.value = nueva_edad

    def cambiar_raza(self, nueva_raza):
        self.raza.value = nueva_raza

    def emitir_sonido(self):
        pass

    def moverse(self):
        pass