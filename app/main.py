from presentation.Subanimales import Perro, Gato, Pajaro, Mapache
from presentation.DatosView import DatosView
from data.FirebaseService import FirebaseService


def main():
    # Inicializar servicio Firebase
    firebase = FirebaseService()

    # Intentar leer datos existentes desde Firebase
    data_perro = firebase.read("animales/Perro")
    data_gato = firebase.read("animales/Gato")
    data_pajaro = firebase.read("animales/Pájaro")
    data_mapache = firebase.read("animales/Mapache")

    # Comprobar que existen los datos, si no, crearlos
    if not data_perro:
        data_perro = {"nombre": "Firulais", "edad": 3, "raza": "Snauzer"}
        firebase.create("animales/Perro", data_perro)
        print("Perro creado en Firebase.")

    if not data_gato:
        data_gato = {"nombre": "Micifu", "edad": 2, "raza": "Siamés"}
        firebase.create("animales/Gato", data_gato)
        print("Gato creado en Firebase.")

    if not data_pajaro:
        data_pajaro = {"nombre": "Mordecai", "edad": 1, "raza": "Azulejo"}
        firebase.create("animales/Pájaro", data_pajaro)
        print("Pájaro creado en Firebase.")

    if not data_mapache:
        data_mapache = {"nombre": "Rigby", "edad": 4, "raza": "Marrón"}
        firebase.create("animales/Mapache", data_mapache)
        print("Mapache creado en Firebase.")

    # Crear objetos de animales con los datos existentes
    perro = Perro(data_perro["nombre"], data_perro["edad"], data_perro["raza"])
    gato = Gato(data_gato["nombre"], data_gato["edad"], data_gato["raza"])
    pajaro = Pajaro(data_pajaro["nombre"], data_pajaro["edad"], data_pajaro["raza"])
    mapache = Mapache(data_mapache["nombre"], data_mapache["edad"], data_mapache["raza"])

    # Crear la vista que sincroniza con Firebase
    vista = DatosView(perro, gato, pajaro)

    # Mostrar los datos iniciales
    print("\n=== DATOS INICIALES ===")
    vista.mostrar_datos(perro)
    vista.mostrar_datos(gato)
    vista.mostrar_datos(pajaro)
    vista.mostrar_datos(mapache)

    # Actualizar datos (cambios también se sincronizan con Firebase)
    print("\n=== ACTUALIZANDO DATOS ===")
    vista.actualizar_datos(perro, nombre="Max", edad=4)
    vista.actualizar_datos(gato, nombre="Pelusa", raza="Persa")
    vista.actualizar_datos(pajaro, edad=2, raza="Canario")
    vista.actualizar_datos(mapache, nombre="Rocket", edad=5, raza="Gris")

    # Mostrar resultados finales
    print("\n=== DATOS ACTUALIZADOS ===")
    vista.mostrar_datos(perro)
    vista.mostrar_datos(gato)
    vista.mostrar_datos(pajaro)
    vista.mostrar_datos(mapache)



if __name__ == "__main__":
    main()