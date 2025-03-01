# **Arquitectura y Tecnologías del Proyecto Dev0psHub**

## 1. **Introducción**

Este documento te va a contar cómo hemos montado **Dev0psHub**: una plataforma open-source pensada para equipos pequeños que quieren gestionar proyectos de desarrollo de forma sencilla. El objetivo es juntar varias funcionalidades clave como gestión de tareas, chat y métricas, todo en una sola herramienta. El MVP está compuesto por un backend modular con microservicios usando **Django** y un frontend hecho con **Electron**. Con esto buscamos tener una arquitectura flexible y fácil de escalar según el proyecto crezca.

---

## 2. **Tecnologías Utilizadas**

### Backend: **Django con MicroBackends (Microservicios)**

Para el backend, vamos a usar **Django**, un framework robusto, escalable y que permite desarrollar rápido. Pero, en lugar de tener una sola app monolítica, vamos a hacer todo modular usando **microbackends**. Cada "app" de Django será un microservicio encargado de una funcionalidad específica.

#### ¿Por qué Django?
- **MVC**: Separa bien la lógica de negocio, la presentación y la gestión de datos.
- **Django Rest Framework (DRF)**: Lo usaremos para crear **APIs RESTful** que permitirán que el frontend y los microservicios se comuniquen.
- **Autenticación**: Usaremos **JWT** o **tokens** para gestionar la autenticación de los usuarios, asegurando el control de acceso en cada microservicio.

#### MicroBackends en Django:
Vamos a dividir el backend en varias apps que ofrecerán funcionalidades concretas. Algunas de las microapps que tendrá el sistema son:

- **Tasks (Kanban)**: Gestión de tareas en un tablero Kanban.
- **Chat**: Comunicación en tiempo real entre los miembros del equipo.
- **Git Integration**: Conexión con plataformas como **GitLab** o **Gitea** para ver commits y actividad de los repositorios.
- **Auth**: Gestión de autenticación y roles de usuario.

### Frontend: **Electron (Versión Web para el MVP)**

Para el frontend, vamos a usar **Electron**. ¿Por qué? Porque nos permite usar tecnologías web como **HTML**, **CSS** y **JavaScript** para crear una aplicación de escritorio o web. Para el MVP, nos centraremos en la versión web para facilitar el desarrollo y la implementación, pero la idea es que se pueda expandir a versión de escritorio en el futuro.

#### Ventajas de usar Electron:
- **Desarrollo rápido**: Si sabes tecnologías web, esto es pan comido.
- **Multiplataforma**: Con Electron, tu aplicación funcionará en Windows, macOS y Linux sin tener que rehacer todo el código.
- **Escalabilidad**: El frontend podrá crecer de forma sencilla hacia aplicaciones de escritorio cuando el proyecto lo necesite.

### Otras Herramientas y Tecnologías:
- **Base de Datos**: Usaremos **SQLite** o **PostgreSQL**, dependiendo de lo que necesitemos para la producción.
- **Docker**: Lo usaremos para contenerizar las aplicaciones y microservicios, especialmente cuando pasemos a producción.
- **WebSockets**: Para el chat en tiempo real, implementaremos **Django Channels** y **WebSockets**.
- **Git Integration (GitLab/Gitea API)**: La integración con **GitLab** o **Gitea** nos permitirá extraer información de los commits y mostrarla en tiempo real.

---

## 3. **Arquitectura del Proyecto**

### **Arquitectura del Backend (MicroBackends con Django)**

El backend está basado en **microservicios** gestionados dentro de un solo proyecto de Django. Cada microservicio será una **app de Django** separada. Esto hace que el sistema sea más fácil de escalar y modificar sin tocar el resto de los servicios.

#### Estructura del Proyecto Backend:

```bash
dev0pshub/
├── backend/
│   ├── dev0pshub/          # Proyecto principal de Django
│   ├── tasks/              # Microbackend de tareas (Kanban)
│   ├── chat/               # Microbackend de chat
│   ├── git_integration/    # Microbackend de integración con Git
│   ├── auth/               # Microbackend de autenticación y gestión de usuarios
├── frontend/               # Carpeta con la app de Electron
├── /....                   # Otros ficheros generados por Django     
└── venv/                   # Entorno virtual de Python con las dependencias de Django
```

#### Comunicación entre MicroBackends:
Los microservicios se van a comunicar principalmente a través de **APIs RESTful**. Cada microbackend tendrá su propio conjunto de endpoints para interactuar con otros servicios y con el frontend.

### **Arquitectura del Frontend (Electron)**

El frontend se construirá con **Electron**, que se va a comunicar con el backend Django mediante **APIs REST**. Será el encargado de mostrar la interfaz y manejar la interacción con el usuario.

#### Estructura del Proyecto Frontend:

```bash
frontend/
├── src/
│   ├── components/         # Componentes de la interfaz de usuario
│   ├── views/              # Vistas de la aplicación (Kanban, Chat, etc.)
│   ├── services/           # Servicios para interactuar con el backend (APIs)
├── public/
│   ├── index.html          # Página principal
└── package.json            # Dependencias y configuraciones de Electron
```

El frontend usará **Axios** o **Fetch** para hacer peticiones al backend y actualizar la interfaz cuando recibamos la respuesta.

---

## 4. **Flujo de Trabajo en el MVP**

### **1. Autenticación de Usuario**:
El microbackend **auth** será el encargado de gestionar las credenciales de usuario. Usaremos **JWT** para autenticar las solicitudes entre el frontend y los microservicios.

### **2. Gestión de Tareas (Kanban)**:
El microservicio **tasks** se encargará de gestionar las tareas. Los usuarios podrán crear tareas, asignarlas y moverlas entre diferentes estados (Pendiente, En Progreso, Completado) en un tablero Kanban.

### **3. Comunicación en Tiempo Real (Chat)**:
El microservicio **chat** permitirá la comunicación en tiempo real entre los usuarios. Usaremos **Django Channels** y **WebSockets** para los mensajes en vivo.

### **4. Integración con Git**:
El microservicio **git_integration** se conectará con plataformas como **GitLab** o **Gitea** para mostrar la actividad de los commits en tiempo real.

---

## 5. **Despliegue y Producción**

Durante el desarrollo, vamos a usar un enfoque de despliegue simplificado, pero cuando estemos listos para producción, lo haremos con **Docker** para contenerizar tanto el frontend como el backend.

### **Fase de MVP**:
- Se lanzará una versión web utilizando **Electron** para simplificar el despliegue.

### **Fase de Producción**:
- En producción, usaremos **Docker** para contenedores, lo que nos permitirá escalar el proyecto de forma sencilla y tener independencia entre los servicios.

---

## **Conclusión**

**Dev0psHub** tiene una arquitectura modular que hace el desarrollo rápido, pero a la vez robusto y escalable. Usamos **microservicios** en el backend con **Django** y un **frontend** con **Electron** para crear un sistema fácil de mantener y ampliar. Aunque comencemos con una versión sencilla, esta estructura permitirá crecer de forma controlada y eficiente.