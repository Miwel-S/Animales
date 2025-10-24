from Subanimales import Perro, Gato, Pajaro, Mapache

class DatosView:
    def __init__(self, perro: Perro, gato: Gato, pajaro: Pajaro, mapache:Mapache):
        self.perro, self.gato, self.pajaro, self.mapache = perro, gato, pajaro, mapache

        # Agregar los observadores
        # Se utiliza un lambda para capturar el animal correspondiente en cada callback
        # Así, cuando se notifica un cambio, sabemos a qué animal pertenece
        # Ademas, asi posteriormente es mas facil guardar en firebase
        for animal in [self.perro, self.gato, self.pajaro, self.mapache]:
            animal.nombre.agregar(lambda valor, a=animal: self._nombre_cambiado(a, valor)) 
            animal.edad.agregar(lambda valor, a=animal: self._edad_cambiada(a, valor))
            animal.raza.agregar(lambda valor, a=animal: self._raza_cambiada(a, valor))

    def _nombre_cambiado(self,animal, nuevo_valor):
        print(f"🐾 Nombre actualizado a: {nuevo_valor}")
        self._guardar_en_firebase(animal)

    def _edad_cambiada(self,animal, nuevo_valor):
        print(f"📆 Edad actualizada a: {nuevo_valor}")
        self._guardar_en_firebase(animal)

    def _raza_cambiada(self,animal, nuevo_valor):
        print(f"🧬 Raza actualizada a: {nuevo_valor}")
        self._guardar_en_firebase(animal)

    def mostrar_datos(self, animal):
        print(f"\n[{animal.tipo}]")
        print(f"Nombre: {animal.nombre.value}")
        print(f"Edad: {animal.edad.value}")
        print(f"Raza: {animal.raza.value}")

    def actualizar_datos(self, animal, nombre=None, edad=None, raza=None):
        if nombre:
            animal.cambiar_nombre(nombre)
        if edad:
            animal.cambiar_edad(edad)
        if raza:
            animal.cambiar_raza(raza)

    def _guardar_en_firebase(self, animal):
        data = {
            "nombre": animal.nombre.value,
            "edad": animal.edad.value,
            "raza": animal.raza.value
        }
        path = f"animales/{animal.tipo}"
        self.firebase.update(path, data)