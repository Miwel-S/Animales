from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre,edad,raza)

    def emitir_sonido(self):
        mensaje = f"¡Guau guau!"
        self.notificar_observadores(mensaje)

    def moverse(self):
        mensaje = f"{self.nombre} corre."
        self.notificar_observadores(mensaje)


class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Gato")

    def emitir_sonido(self):
        mensaje = f"{self.nombre} dice: Miau..."
        self.notificar_observadores(mensaje)

    def moverse(self):
        mensaje = f"{self.nombre} camina por la casa."
        self.notificar_observadores(mensaje)


class Pajaro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Pájaro")

    def emitir_sonido(self):
        mensaje = f"{self.nombre} canta."
        self.notificar_observadores(mensaje)

    def moverse(self):
        mensaje = f"{self.nombre} vuela."
        self.notificar_observadores(mensaje)