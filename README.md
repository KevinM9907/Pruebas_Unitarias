Proyecto Pruebas Unitarias

Descripción
Este proyecto es un backend desarrollado en Django para la gestión de un sistema con múltiples modelos de negocio. Incluye funcionalidades para manejar proveedores, clientes, usuarios, manicuristas, insumos, roles, y otros elementos del negocio.

El objetivo es garantizar la calidad del software mediante pruebas unitarias que aseguren el correcto funcionamiento de al menos 5 clases principales del modelo.

Tecnologías usadas:

Python 3.8+

Django 4.x

Base de datos SQLite (configuración por defecto)

Git y GitHub para control de versiones

Requisitos Previos
Python 3.8 o superior instalado

Git instalado

Entorno virtual (opcional pero recomendado)

Django instalado en el entorno virtual o globalmente

Cómo desplegar el proyecto
Clonar el repositorio

bash
git clone [https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio](https://github.com/KevinM9907/Pruebas_Unitarias.git)
Crear y activar entorno virtual (opcional pero recomendado)

bash
python -m venv venv
# En Windows
.\venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
Instalar dependencias

bash
pip install -r requirements.txt
Ejecutar migraciones para preparar la base de datos SQLite

bash
python manage.py makemigrations
python manage.py migrate
(Opcional) Crear un superusuario para acceder al admin

bash
python manage.py createsuperuser
Para levantar el servidor local y validar que funciona:

bash
python manage.py runserver
Instrucciones para ejecutar pruebas unitarias
Este proyecto incluye pruebas unitarias para las siguientes clases de modelo:

Proveedor

Cliente

Manicurista

Insumo

Usuario

Para ejecutar las pruebas, corre los siguientes comandos desde la raíz del proyecto:

bash
python manage.py test api.tests.test_proveedor
python manage.py test api.tests.test_cliente
python manage.py test api.tests.test_manicurista
python manage.py test api.tests.test_insumo
python manage.py test api.tests.test_usuario
Cada comando ejecuta los tests unitarios para una clase específica. También puedes ejecutarlos todos juntos con:

bash
python manage.py test
Importar base de datos
Para importar la base de datos en otra máquina, se incluye el archivo import_data.sql en la carpeta /database que contiene el script para crear y poblar la base de datos SQLite.

Para usarlo, sigue estos pasos:

Asegúrate de tener SQLite instalado o usa herramientas compatibles.

Ejecuta el script para recrear la base:

bash
sqlite3 db.sqlite3 < database/import_data.sql
Recuerda ejecutar antes las migraciones para asegurar que la estructura está actualizada.

