# Proyecto Pruebas Unitarias

## Descripción

Este proyecto es un backend desarrollado en Django para la gestión de un sistema con múltiples modelos de negocio. 
Incluye funcionalidades para manejar proveedores, clientes, usuarios, manicuristas, insumos, roles, y otros elementos del negocio.
El objetivo es garantizar la calidad del software mediante pruebas unitarias que aseguren el correcto funcionamiento de al menos 5 clases principales del modelo.

## Tecnologías usadas

- Python 3.8+
- Django 4.x
- Base de datos SQLite (configuración por defecto)
- Git y GitHub para control de versiones
  
# Requisitos Previos

- Python 3.8 o superior instalado
- Git instalado
- Entorno virtual (opcional pero recomendado)
- Django instalado en el entorno virtual o globalmente

## Cómo desplegar el proyecto

- Intalar requerimientos:
   + pip install -r requirements.txt
  
- Hacer las migraciones:
    + python manage.py makemigrations
    + python manage.py migrate


## Como iniciar el entorno virtual
bash
python -m venv venv

## En Windows
.\venv\Scripts\activate

## En Linux/Mac
source venv/bin/activate

## Este proyecto incluye pruebas unitarias para las siguientes clases de modelo:

- Proveedor
- Cliente
- Manicurista
- Insumo
- Usuario

## Para ejecutar las pruebas, corre los siguientes comandos desde la raíz del proyecto:

- python manage.py test api.tests.test_proveedor
- python manage.py test api.tests.test_cliente
- python manage.py test api.tests.test_manicurista
- python manage.py test api.tests.test_insumo
- python manage.py test api.tests.test_usuario


## Cada comando ejecuta los tests unitarios para una clase específica. También puedes ejecutarlos todos juntos con:

- python manage.py test
