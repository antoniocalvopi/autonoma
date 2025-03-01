# **Arquitectura y Tecnologías del Proyecto Autonóma**

## 1. **Introducción**

Este documento describe cómo he estructurado **Autonóma**: una plataforma open-source diseñada para freelancers y pequeños empresarios que buscan gestionar sus proyectos y aspectos administrativos de forma sencilla. El objetivo es integrar funcionalidades clave como la gestión de pedidos, presupuestos, facturación y previsión económica en una sola herramienta. El **MVP** está compuesto por un backend modular usando **Django** y un frontend desarrollado con **Electron**. La arquitectura busca mantener flexibilidad junto con escalabilidad a medida que el proyecto crezca.

---

## 2. **Tecnologías Utilizadas**

### Backend: **Django con MicroBackends (Microservicios)**

Para el backend, he elegido **Django**, un framework robusto, flexible y rápido de desarrollar. En lugar de optar por una arquitectura monolítica, he optado por una estructura modular utilizando **microbackends**. Cada "app" de Django será un microservicio encargado de una funcionalidad específica.

#### ¿Por qué Django?
- **MVC**: Organiza la lógica de negocio, la presentación y la gestión de datos de forma clara.
- **Django Rest Framework (DRF)**: Lo usaré para crear **APIs RESTful**, que permitirán la comunicación entre el frontend y los microservicios.
- **Autenticación**: Implementaré **JWT** o **tokens** para gestionar la autenticación de los usuarios, garantizando la seguridad y control de acceso en cada microservicio.

#### MicroBackends en Django:
El backend se dividirá en varias aplicaciones (microservicios), cada una ofreciendo una funcionalidad específica. Algunas de las microapps que tendrá el sistema son:

- **Pedidos**: Gestión de pedidos recibidos, su estado y la rentabilidad.
- **Presupuestos**: Generación de presupuestos ajustados y análisis de viabilidad.
- **Facturación**: Generación y gestión de facturas.
- **Autenticación**: Gestión de autenticación y roles de usuario.
- **Calendario Laboral**: Seguimiento de horas trabajadas, disponibilidad y planificación de proyectos.

### Frontend: **Electron (Versión Web para el MVP)**

Para el frontend, usaré **Electron**, que permite usar tecnologías web como **HTML**, **CSS** y **JavaScript** para crear aplicaciones de escritorio o web. En esta fase, me centraré en la versión web del frontend para facilitar el desarrollo y la implementación, pero la idea es expandir a aplicaciones de escritorio en el futuro.

#### Ventajas de usar Electron:
- **Desarrollo rápido**: Al usar tecnologías web, el desarrollo se simplifica y es más accesible.
- **Multiplataforma**: La aplicación funcionará en Windows, macOS y Linux sin necesidad de reescribir el código.
- **Escalabilidad**: A medida que el proyecto crezca, el frontend podrá adaptarse fácilmente para convertirse en una aplicación de escritorio.

### Otras Herramientas y Tecnologías:
- **Base de Datos**: Usaré **SQLite** o **PostgreSQL**, dependiendo de los requerimientos para producción.
- **Docker**: Para contenerizar las aplicaciones y microservicios, especialmente cuando pase a producción.

---

## 3. **Arquitectura del Proyecto**

### **Arquitectura del Backend (MicroBackends con Django)**

El backend se basa en **microservicios** gestionados dentro de un único proyecto de Django. Cada microservicio será una **app de Django** separada, lo que facilita el escalado y la modificación de funcionalidades sin afectar al resto del sistema.

#### Estructura del Proyecto Backend:

```bash
autonoma/
├── backend/
│   ├── autonoma/           # Proyecto principal de Django
│   ├── pedidos/            # Microbackend de gestión de pedidos
│   ├── presupuestos/       # Microbackend de presupuestos
│   ├── facturacion/        # Microbackend de facturación
│   ├── auth/               # Microbackend de autenticación y gestión de usuarios
│   ├── calendario/         # Microbackend de gestión de calendario laboral
├── frontend/               # Carpeta con la app de Electron
└── venv/                   # Entorno virtual de Python con las dependencias de Django
```

#### Comunicación entre MicroBackends:
Los microservicios se comunicarán principalmente a través de **APIs RESTful**. Cada microbackend tendrá su propio conjunto de endpoints para interactuar con otros servicios y con el frontend.

### **Arquitectura del Frontend (Electron)**

El frontend se construirá con **Electron** y se comunicará con el backend Django a través de **APIs REST**. Se encargará de mostrar la interfaz y gestionar la interacción con el usuario.

#### Estructura del Proyecto Frontend:

```bash
frontend/
├── src/
│   ├── components/         # Componentes de la interfaz de usuario
│   ├── views/              # Vistas de la aplicación (Pedidos, Presupuestos, etc.)
│   ├── services/           # Servicios para interactuar con el backend (APIs)
├── public/
│   ├── index.html          # Página principal
└── package.json            # Dependencias y configuraciones de Electron
```

El frontend usará **Axios** o **Fetch** para hacer peticiones al backend y actualizar la interfaz cuando recibimos las respuestas.

---

## 4. **Flujo de Trabajo en el MVP**

### **1. Autenticación de Usuario**:
El microbackend **auth** gestionará las credenciales de usuario. Se utilizará **JWT** para autenticar las solicitudes entre el frontend y los microservicios.

### **2. Gestión de Pedidos**:
El microservicio **pedidos** gestionará los pedidos entrantes, su seguimiento, y su análisis de rentabilidad.

### **3. Gestión de Presupuestos**:
El microservicio **presupuestos** permitirá a los usuarios generar presupuestos ajustados en función de parámetros establecidos, y evaluar la rentabilidad de cada uno.

### **4. Facturación**:
El microbackend **facturación** se encargará de generar facturas automáticas y gestionar los pagos recibidos de los clientes.

### **5. Calendario Laboral**:
El microservicio **calendario** permitirá a los usuarios gestionar sus horas de trabajo, disponibilidad y planificación de proyectos.

---

## 5. **Despliegue y Producción**

Durante el desarrollo, utilizaré un enfoque simplificado para el despliegue, pero en la fase de producción, utilizaré **Docker** para contenerizar tanto el frontend como el backend.

### **Fase de MVP**:
- Se lanzará una versión web utilizando **Electron** para facilitar el despliegue y asegurar la accesibilidad desde diferentes dispositivos.

### **Fase de Producción**:
- En producción, se usarán **Docker** y contenedores para mejorar la escalabilidad y autonomía entre los servicios.

---

## **Conclusión**

**Autonóma** sigue una arquitectura modular que facilita el desarrollo rápido pero robusto, usando **microservicios** en el backend con **Django** y un frontend en **Electron**. Este enfoque hace que la plataforma sea fácil de mantener, ampliar y escalar conforme las necesidades de los usuarios crezcan, asegurando una experiencia óptima tanto para freelancers como para pequeños empresarios.
