class Animal:
    def __init__(self,nombre:str,edad:int,raza:str):
         self.nombre=nombre
         self.edad=edad
         self.raza=raza
    
    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(self, mensaje)

    def caminar(self):
        pass
    
    def emitir_sonido(self):
        pass