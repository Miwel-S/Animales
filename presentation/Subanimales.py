from domain.Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza, "Perro")

    def emitir_sonido(self):
        print(f"{self.nombre.value} dice: ¡Guau guau!")

    def moverse(self):
        print(f"{self.nombre.value} corre por el parque.")


class Gato(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza, "Gato")

    def emitir_sonido(self):
        print(f"{self.nombre.value} dice: Miau...")

    def moverse(self):
        print(f"{self.nombre.value} camina por la casa.")


class Pajaro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza, "Pájaro")

    def emitir_sonido(self):
        print(f"{self.nombre.value} silba.")

    def moverse(self):
        print(f"{self.nombre.value} vuela.")


class Mapache(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza, "Mapache")

    def emitir_sonido(self):
        print(f"{self.nombre.value} hace un sonido de mapache.")

    def moverse(self):
        print(f"{self.nombre.value} se mueve sigilosamente.")