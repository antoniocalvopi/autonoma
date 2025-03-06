# **Guía de Commits**

Esta guía establece las convenciones y buenas prácticas para los commits dentro del proyecto **Autonóma**. Seguir estas normas ayudará a mantener un historial claro y facilitará la colaboración.

---

## **1. Convenciones para Commits**

### **Formato de Mensajes de Commit**
Para garantizar consistencia, usamos el formato **Conventional Commits**:

```
<tipo>(<área>): <breve descripción>

[opcional] Cuerpo del commit explicando más detalles.

[opcional] Referencias a issues relacionados (#123, etc.).
```

### **Tipos de Commits**
- **feat**: Nueva funcionalidad o característica.
- **fix**: Corrección de errores.
- **docs**: Cambios en la documentación.
- **style**: Cambios de formato (espacios, indentación, etc.) sin afectar la lógica.
- **refactor**: Refactorización del código sin cambiar funcionalidad.
- **test**: Adición o modificación de pruebas.
- **chore**: Cambios en tareas de mantenimiento del proyecto (dependencias, CI/CD, etc.).

### **Ejemplo de Commit Correcto**
```
feat(auth): agregar autenticación con JWT

Se implementa el sistema de autenticación con JWT en el microbackend de auth.

Closes #15
```