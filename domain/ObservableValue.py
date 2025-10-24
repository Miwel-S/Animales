class ObservableValue:
    def __init__(self, value):
        self._value = value
        self._observadores = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, nuevo_valor):
        self._value = nuevo_valor
        self._notificar_observadores(nuevo_valor)

    def agregar(self, callback):
        self._observadores.append(callback)

    def _notificar_observadores(self, nuevo_valor):
        for observador in self._observadores:
            observador(nuevo_valor)
