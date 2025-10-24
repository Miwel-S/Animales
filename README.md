# 🐾 Sistema de Animales con Firebase y Patrón Observable  

Este proyecto implementa un sistema orientado a objetos en **Python**, conectado a **Firebase Realtime Database**.  
Cada animal (Perro, Gato, Pájaro y Mapache) posee atributos observables, lo que permite **detectar y sincronizar automáticamente los cambios** en la base de datos.  

Se emplea el **patrón de diseño Observable/Observer**, junto con una clase `FirebaseService` que gestiona la conexión y operaciones CRUD con Firebase.  

---

## 📁 Archivos del proyecto  

| Archivo | Descripción |
|----------|--------------|
| **`.env`** | Contiene las variables de entorno con la ruta del archivo JSON de credenciales y la URL de Firebase. |
| **`firebase_config.json`** | Archivo de credenciales del servicio Firebase (descargado desde tu proyecto). |
| **`FirebaseService.py`** | Clase encargada de manejar la conexión y operaciones CRUD con Firebase. |
| **`ObservableValue.py`** | Clase que implementa el comportamiento observable de los atributos. |
| **`Subanimales.py`** | Define las clases `Perro`, `Gato`, `Pájaro` y `Mapache`, heredadas de `Animal`. |
| **`DatosView.py`** | Observador que reacciona a los cambios en los animales y actualiza Firebase. |
| **`main.py`** | Archivo principal que inicializa, muestra y sincroniza los animales con Firebase. |
| **`requirements.txt`** | Lista de dependencias necesarias para ejecutar el proyecto. |

---

## ⚙️ Instalación y configuración  

1. **Clonar el repositorio o copiar los archivos del proyecto.**  
   ```bash
   git clone https://github.com/Miwel-S/Animales-Observable-Firebase.git
   cd Animales-Observable-Firebase
   
2. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt

3. **Configurar el archivo `.env` con las siguientes variables:**
   ```bash
   FIREBASE_CREDS_JSON=./firebase_config.json
   FIREBASE_DB_URL=https://<tu-base-de-datos>.firebaseio.com/

4. **Agregar el archivo `firebase_config.json` descargado desde Firebase:

---

## Funcionalidades principales
### Clase `ObservableValue`
Permite que los atributos de un animal sean “observables”.
Cuando su valor cambia, notifica a todas las funciones (observadores) registradas.

### Clase `DatosView`
Actúa como observador:
- Escucha los cambios en los animales (nombre, edad, raza).
- Muestra los cambios en consola.
- Sincroniza automáticamente los nuevos valores con Firebase.

### Clase `FirebaseService`
Encapsula las operaciones con la base de datos Firebase (CRUD).
  ### Métodos principales:
  - `create`: Crea un nuevo nodo con los datos especificados.
  - `read`: Lee y devuelve los datos almacenados en la ruta indicada.
  - `update`: Actualiza los valores existentes del nodo indicado.
  - `delete`: Elimina el nodo especificado en la base de datos.

---

## Ejemplo de uso y ejecución
### Ejecución
Ejecuta el archivo principal con:
  ```bash
  python main.py
```

### Ejemplo de salida
- Salida en consola
<img width="469" height="474" alt="image" src="https://github.com/user-attachments/assets/5b87e201-1523-48d1-916f-7bf373380944" />
<img width="314" height="252" alt="image" src="https://github.com/user-attachments/assets/d46dee4a-d3c4-4d51-973e-9cfda979f3f9" />
<img width="289" height="469" alt="image" src="https://github.com/user-attachments/assets/f93ebb61-8a1a-4f1d-b856-d73a431a499e" />


- Datos en Firebase
<img width="364" height="436" alt="image" src="https://github.com/user-attachments/assets/f0437eeb-32cf-4870-b848-0b4b6ed5031d" />

---

## Autor
Miguel Silva
Universidad Nacional de Colombia
