## EVALUACIÓN


- Crea un proyecto FastAPI desde cero.

- Define una clase modelo (Pydantic) llamada **User**, que representará la estructura de datos para un usuario. La clase **User** debe tener los siguientes campos:

###### **id**: Identificador único del usuario (entero).
###### **username**: Nombre de usuario (cadena, entre 3 y 20 caracteres).
###### **email**: Dirección de correo electrónico válida.
###### **password**: Contraseña (cadena, al menos 8 caracteres).

- Implementa la lógica para crear una tabla **users** en una base de datos SQLite utilizando SQLAlchemy. La tabla **users** debe tener los mismos campos que la clase **User**.

- Crea un endpoint **/users/** para crear nuevos usuarios. El endpoint debe aceptar una solicitud HTTP POST con un objeto JSON que represente un usuario y debe validar los datos utilizando el modelo **User** de Pydantic antes de insertarlos en la base de datos. Debe devolver una respuesta JSON con el usuario creado y el ID asignado por la base de datos.

- Implementa otro endpoint **/users/{user_id}** para obtener los detalles de un usuario específico. El endpoint debe aceptar una solicitud HTTP GET con el ID del usuario en la URL y devolver una respuesta JSON con los detalles del usuario correspondiente.

- Realiza pruebas utilizando herramientas como cURL o Postman para probar el funcionamiento de los endpoints y verificar que las validaciones con Pydantic funcionen correctamente.

- Agrega comentarios en el código explicando la funcionalidad y la lógica implementada.



### Puntos de evaluación:

* Correcta definición de la clase **User** con validaciones utilizando Pydantic.
* Creación exitosa de la tabla **user**s en la base de datos SQLite.
* Implementación de los endpoints **/users/** y **/users/{user_id}** con sus respectivas validaciones.
* Correcta manipulación de errores y respuestas en los endpoints.
* Correcto funcionamiento de la API y las validaciones con Pydantic.

## Enviar un PR, usando su nombre_apellido como nombre de la rama
