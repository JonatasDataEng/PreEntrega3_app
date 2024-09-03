# PreEntrega3_app

**PreEntrega3_app** es una aplicación de procesamiento de datos que se centra en la extracción, transformación y carga (ETL) de datos desde la API de CoinMarketCap. La aplicación utiliza Apache Airflow para orquestar la ETL y almacena los datos procesados en una base de datos Amazon Redshift.

## Características

- **Extracción de datos**: Obtiene datos de la API de CoinMarketCap.
- **Transformación de datos**: Limpia y transforma los datos extraídos para su análisis.
- **Carga de datos**: Almacena los datos procesados en Amazon Redshift.
- **Programación y orquestación**: Utiliza Apache Airflow para gestionar y ejecutar tareas de ETL.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes elementos instalados:

- Docker
- Docker Compose
- Git

## Configuración del Proyecto

1. **Clonar el Repositorio**

   Primero, clona el repositorio en tu máquina local:

       git clone https://github.com/JonatasDataEng/PreEntrega3_app.git
       cd PreEntrega3_app

2. Configurar Variables de Entorno

Crea un archivo .env en la raíz del proyecto con las siguientes variables. Asegúrate de reemplazar los valores con tus credenciales y detalles reales:

Configurar Variables de Entorno

Crea un archivo .env en la raíz del proyecto con las siguientes variables. Asegúrate de reemplazar los valores con tus credenciales y detalles reales:

.env

   
    REDSHIFT_USER=your_redshift_user
    REDSHIFT_PASSWORD=your_redshift_password
    REDSHIFT_HOST=your_redshift_host
    REDSHIFT_DB=your_redshift_db

Asegúrate de ajustar los valores de conexión a tu base de datos y otros parámetros según sea necesario.

3. Construir la Imagen de Airflow

Inicia los servicios definidos en el archivo docker-compose.yaml:

    docker-compose up
    Esto levantará los contenedores para Apache Airflow, PostgreSQL, Redis y MinIO, entre otros.

4. Cómo Ejecutar la ETL
Acceder a la Interfaz Web de Airflow

Una vez que los servicios estén en ejecución, accede a la interfaz web de Airflow en http://localhost:8080.

Configurar la Conexión a Redshift

Asegúrate de que la conexión a Amazon Redshift esté configurada en Airflow. Puedes hacer esto en la interfaz web de Airflow bajo la sección de "Conexiones".

5. Ejecutar la DAG

En la interfaz de Airflow, encontrarás una DAG llamada etl_coin_market_cap. Activa la DAG y deja que se ejecute según el horario programado.

6. Monitorear y Verificar

Monitorea la ejecución de la DAG en la interfaz de Airflow. Puedes revisar los logs de cada tarea para verificar que los datos se están extrayendo, transformando y cargando correctamente en Amazon Redshift.

7. Problemas Comunes y Soluciones
Error de Conexión: Asegúrate de que las credenciales y la configuración en el archivo .env sean correctas. Verifica que todos los servicios están en funcionamiento.

Errores de Construcción: Si encuentras errores durante la construcción de la imagen de Docker, asegúrate de que todos los archivos necesarios estén presentes y que los comandos en el Dockerfile sean correctos.

Errores de Ejecución: Revisa los logs en la interfaz web de Airflow para obtener detalles específicos sobre cualquier error que ocurra durante la ejecución de la DAG.

8. Contribuciones
Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

Fork el Repositorio
Crea una Rama para tus Cambios
Realiza tus Cambios y Pruebas
Envía un Pull Request
