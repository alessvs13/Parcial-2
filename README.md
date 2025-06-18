# Parcial-2
IMAGENES DEL FUNCIONAMIENTO DEL PROGRAMA


![image](https://github.com/user-attachments/assets/a6d6f1bc-353c-4aba-9d57-e746372eb306)


Se registro el libro


![image](https://github.com/user-attachments/assets/2929847a-5a01-4bad-a532-1088d4722a09)


Mensaje de confirmacion 
![image](https://github.com/user-attachments/assets/9d41c0f0-67ac-4e3e-902a-1eef276eb860)
#Queda registrado en la base de datos 
![image](https://github.com/user-attachments/assets/f4e0a319-8775-4f8b-bc1f-8924ce603625)
#Para buscar el libro se filtra la busqueda por titulo o por autor
![image](https://github.com/user-attachments/assets/2650241b-c0d2-4369-b5a2-bcae7abd45ab)
Al marcarse como prestado deja de aparcer disponible y al marcarse como devuelto queda disponible otra vez

1. Descripción de las funciones y estructuras de datos implementadas
Funciones puras (programación funcional)
crear_libro(titulo, autor, categoria)
Devuelve un diccionario representando un libro con campos: id (UUID), titulo, autor, categoria, y disponible (por defecto en True).

guardar_libro(libro)
Guarda el libro en Firebase, usando su id como clave.

consultar_libros()
Recupera todos los libros desde Firebase y los devuelve como una lista de diccionarios.

buscar_libros(filtro, valor)
Filtra la lista de libros según un campo (titulo o autor) comparando insensiblemente el valor ingresado.

actualizar_disponibilidad(libro_id, disponible)
Actualiza el campo disponible de un libro en la base de datos.

Estructuras de datos
Libro: Diccionario con campos id, titulo, autor, categoria, disponible.

Firebase: Base de datos NoSQL en la nube utilizada para persistencia, organizada como diccionarios anidados.

Treeview: Widget de tkinter.ttk usado como tabla para mostrar resultados.

Clase GUI: BibliotecaApp
Contiene dos pestañas:

Registrar: Permite al usuario ingresar título, autor y categoría de un libro.

Consultar: Permite buscar libros por título o autor y cambiar su estado (prestado/devuelto).

2. Justificación técnica de las decisiones de diseño
Librería GUI: Tkinter
Simplicidad para aplicaciones de escritorio.

Incluye componentes como Notebook, Entry, Button, y Treeview ideales para formularios y vistas tabulares.

Preinstalada con Python (no requiere instalación adicional).

Persistencia: Firebase Realtime Database
lmacenamiento NoSQL flexible, ideal para estructuras de datos anidadas como los libros.

Acceso en tiempo real y persistente desde la nube.

Uso de identificadores únicos (UUID) permite acceso directo y sin colisiones.

Enfoque funcional
Las funciones como crear_libro y buscar_libros son puras: no dependen del estado externo ni lo modifican.

Esto facilita pruebas unitarias y separación de lógica de negocio de la interfaz.

3. Análisis de dificultades y posibles mejoras
Dificultades detectadas

Búsqueda exacta 
Aunque se intenta hacer lower(), no permite búsquedas parciales (ej. solo una parte del título).

No hay validación completa de campos
Se valida si están vacíos, pero no se valida longitud, caracteres válidos o categorías incorrectas.

El campo "disponible" es un booleano simple
No se guarda información de cuándo se prestó o devolvió el libro.

No hay autenticación de usuarios
Cualquier persona puede registrar o modificar libros sin restricciones.

Posibles mejoras
Agregar búsqueda parcial o por coincidencia (fuzzy search).

Incluir autenticación con Firebase Auth para seguridad.

Registrar fecha y hora de préstamo/devolución.

Manejar errores de conexión y notificar al usuario.

Permitir editar o eliminar libros registrados.

Agregar paginación o filtros avanzados para colecciones grandes.
