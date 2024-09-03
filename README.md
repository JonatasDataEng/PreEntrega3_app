# PreEntrega3_app

**PreEntrega3_app** es una aplicación de procesamiento de datos que se centra en la extracción, transformación y carga (ETL) de datos desde la API de CoinMarketCap. La aplicación utiliza Apache Airflow para orquestar la ETL y almacena los datos procesados en una base de datos Amazon Redshift.

## Características

- **Extracción de datos**: Obtiene datos de la API de CoinMarketCap.
- **Transformación de datos**: Limpia y transforma los datos extraídos para su análisis.
- **Carga de datos**: Almacena los datos procesados en Amazon Redshift.
- **Programación y orquestación**: Utiliza Apache Airflow para gestionar y ejecutar tareas de ETL.

## 1. Requisitos

Antes de comenzar, asegúrate de tener los siguientes elementos instalados:

- Docker
- Docker Compose
- Git

## 2. Configuración del Proyecto

**Clonar el Repositorio**

   2.1 - Primero, clona el repositorio en tu máquina local:

       git clone https://github.com/JonatasDataEng/PreEntrega3_app.git
       cd PreEntrega3_app

3. Configurar Variables de Entorno

   3.1 -  Crea un archivo .env en la raíz del proyecto con las siguientes variables. Asegúrate de reemplazar los valores con tus credenciales y detalles reales:

   3.2 - Configurar Variables de Entorno

   3.3 - Crea un archivo .env en la raíz del proyecto con las siguientes variables. Asegúrate de reemplazar los valores con tus credenciales y detalles reales:

.env

   
    REDSHIFT_USER=your_redshift_user
    REDSHIFT_PASSWORD=your_redshift_password
    REDSHIFT_HOST=your_redshift_host
    REDSHIFT_DB=your_redshift_db

   3.4 - Asegúrate de ajustar los valores de conexión a tu base de datos y otros parámetros según sea necesario.

## 4. Construir la Imagen de Airflow

   4.1 - Inicia los servicios definidos en el archivo docker-compose.yaml:

    docker-compose up
    Esto levantará los contenedores para Apache Airflow, PostgreSQL, Redis, entre otros.

## 5. Cómo Ejecutar la ETL

   5.1 - Acceder a la Interfaz Web de Airflow

   5.2 - Una vez que los servicios estén en ejecución, accede a la interfaz web de Airflow en http://localhost:8080.

   5.3 - Configurar la Conexión a Redshift

   5.4 - Asegúrate de que la conexión a Amazon Redshift esté configurada en Airflow. Puedes hacer esto en la interfaz web de Airflow bajo la sección de "Conexiones".

## 6. Ejecutar la DAG

   6.1 - En la interfaz de Airflow, encontrarás una DAG llamada etl_coin_market_cap. Activa la DAG y deja que se ejecute según el horario programado.

## 7. Monitorear y Verificar

   7.1 - Monitorea la ejecución de la DAG en la interfaz de Airflow. Puedes revisar los logs de cada tarea para verificar que los datos se están extrayendo, transformando y cargando correctamente en Amazon Redshift.

## 8. Problemas Comunes y Soluciones

   8.1 - Error de Conexión: Asegúrate de que las credenciales y la configuración en el archivo .env sean correctas. Verifica que todos los servicios están en funcionamiento.

   8.2 - Errores de Construcción: Si encuentras errores durante la construcción de la imagen de Docker, asegúrate de que todos los archivos necesarios estén presentes y que los comandos en el Dockerfile sean correctos.

   8.3 - Errores de Ejecución: Revisa los logs en la interfaz web de Airflow para obtener detalles específicos sobre cualquier error que ocurra durante la ejecución de la DAG.

## 9. Contribuciones
Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

   9.1 - Fork el Repositorio
   
   9.2 - Crea una Rama para tus Cambios
   
   9.3 - Realiza tus Cambios y Pruebas
   
   9.4 - Envía un Pull Request
