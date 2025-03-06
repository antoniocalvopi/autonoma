# **Guía de Pull Requests (PRs)**

Esta guía establece las convenciones y buenas prácticas para los pull requests dentro del proyecto **Autonóma**. Seguir estas normas ayudará a mantener un historial claro y facilitará la colaboración.

---

## **3. Normas para Pull Requests (PRs)**

### **Requisitos para un PR**
- La rama debe estar actualizada con `dev` antes de hacer el PR.
- Describir claramente los cambios y su propósito en la descripción del PR.
- Incluir referencias a issues si aplica.
- Seguir la estructura de commits establecida.
- No incluir cambios no relacionados con el propósito del PR.
- Si es un PR grande, dividirlo en varios más pequeños si es posible.

### **Estructura del PR**

**Título:** Breve descripción del cambio.

**Descripción:**
- Explicación clara de lo que se implementó.
- Issue relacionado (si aplica).
- Pruebas realizadas.

**Ejemplo:**
```
### Agrega autenticación con JWT

Se ha implementado el sistema de autenticación con JWT en el microbackend de auth.

Closes #15
```