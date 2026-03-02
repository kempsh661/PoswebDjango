Sistema POS - Gestión de Productos con Django
Descripción

Este proyecto consiste en el desarrollo de un módulo de gestión de productos para un sistema POS (Point of Sale), implementado con Django y Bootstrap 5.

El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre productos, incluyendo una interfaz moderna con confirmación de eliminación mediante modal dinámico.

Este proyecto fue desarrollado con fines académicos y de fortalecimiento de competencias en desarrollo backend con Python y Django.

Tecnologías Utilizadas

Python 3.11+

Django

Bootstrap 5

HTML5

JavaScript

SQLite (base de datos por defecto)

Funcionalidades Implementadas

Registro de productos

Listado de productos

Edición de productos

Eliminación con confirmación mediante modal Bootstrap

Interfaz estilizada con Bootstrap 5

Protección CSRF en formularios

Uso de plantillas base para reutilización de estructura

Estructura del Proyecto
poskem/
│
├── manage.py
├── poskem/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── productos/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/
        └── productos/
            ├── base.html
            ├── lista.html
            ├── crear.html
            └── editar.html
Modelo Producto

El modelo principal incluye:

nombre

descripcion

precio

stock

fecha_creacion

Permite administrar inventario básico dentro del sistema POS.
