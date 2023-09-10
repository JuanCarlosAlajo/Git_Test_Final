**Prueba Final**

**Tema:** Registro de Información extraída de un servicio web

1. **OBJETIVO**

El desarrollo de la práctica, tiene como objeto aplicar los conocimientos recibidos en la asignatura de “TRATAMIENTO DE DATOS”, mismo que consiste el registrar información obtenida en medios externos en una base de datos MongoDB.

2. **DESCRIPCIÓN DE LA SOLUCIÓN**

- Identificar un servicio web que entregue información útil e informativa.
- Ejecutar el proceso de extracción de información
- Ejecutar el proceso de registro en la Base de datos.
- Crear y configurar un repositorio en el motor de base de datos Mongo DB
- Identificar registros de tipo colección.
- Respaldar la solución o desarrollo en un repositorio GitHub.

3. **DISEÑO DE LA SOLUCION**

    3.1. **DIAGRAMA DE ARQUITECTURA**

![arquitectura.PNG](Graficos%2Farquitectura.PNG)


3.2. **DICCIONARIO DE DATOS**
- Motor de Base de datos MongoDB
- Base de Datos: pry\_test\_fin\_tratam\_datos
- Colección: REGISTROS_TEST-FINAL
- Campo 1: INSTITUCION
- Campo 2: AVALUO
- Campo 3: FECHA\_REGISTRO

3.3. **DIAGRAMA DE FLUJO**

![Diagrama_Flujo.PNG](Graficos%2FDiagrama_Flujo.PNG)

4. **DESARROLLO**

Para desarrollar el proyecto, se sigue los siguientes pasos:

- Como primer paso, se crea un repositorio GitHub público (Git\_Test\_Final), para respaldar y controlar los versionamientos del proyecto.
- Como requisito del proyecto, se crea una instancia de base de datos MongoDB Atlas, mediante la suscripción de una cuenta de usuario y se opta por seleccionar la versión free.
- Se instala ambientes de desarrollo PyChar
- Se implementa las siguientes librerías en el ambiente de desarrollo PyChar, mediante la inclusión en el archivo “requirements.txt”
  - Flask
  - Pymongo
  - Requests
  - Python-dotenv

- Se crea el archivo utils.py, mismo que contiene la consulta de información a ser utilizada para el registro en la base de datos.
- Se implementa el archivo cnx\_base\_datos, mismo que contiene la clase MongoDriver con sus atributos y métodos a ser consumidos en otros procesos. Cabe señalar que el constructor de esta clase, contiene la cadena de conexión hacia la base de datos MongoDB
- Se crea el archivo app\_registra\_datos.py, mismo que ejecuta las consultas y posterior registro de información obtenida (colección de registros) en la base de datos.

5. **CONCLUSIONES**

- El conocimiento recibido es de gran ayuda para solventar nuevos retos en los desarrollos tecnológicos.
- Utilización de nuevas tecnologías para tratamiento de datos.
- Optimización de recursos, mediante uso de herramientas libres.

6. **REFERENCIAS**

[**https://excalidraw.com/**](https://excalidraw.com/)

[**https://cloud.mongodb.com/**](https://cloud.mongodb.com/)

[**https://www.youtube.com/watch?v=GsCCyN3fRoI**](https://www.youtube.com/watch?v=GsCCyN3fRoI)





