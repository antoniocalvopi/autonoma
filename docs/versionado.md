# **Guía de Versionado**

Esta guía establece el esquema de versionado del proyecto **Autonóma** para asegurar consistencia y claridad en el control de versiones.

---

## **1. Esquema de Versionado**

Usamos **Semantic Versioning (SemVer)** como esquema de versionado, con el siguiente formato:

```
MAJOR.MINOR.PATCH
```

Donde:
- **MAJOR**: Se incrementa cuando hay cambios incompatibles con versiones anteriores.
- **MINOR**: Se incrementa cuando se agregan nuevas funcionalidades de manera retrocompatible.
- **PATCH**: Se incrementa cuando se corrigen errores sin cambiar la funcionalidad.

### **Ejemplo de Versionado**
- `1.0.0`: Primera versión estable.
- `1.1.0`: Se agrega una nueva funcionalidad sin romper compatibilidad.
- `1.1.1`: Se corrige un error menor.
- `2.0.0`: Cambios que rompen compatibilidad con versiones anteriores.

---

## **2. Relación con Branches**

- `main`: Contiene la última versión estable.
- `dev`: Contiene cambios en desarrollo antes de ser fusionados en `main`.
- `feature/*`: Ramas específicas para el desarrollo de nuevas características.
- `hotfix/*`: Ramas para correcciones urgentes en la versión estable.
- `release/*`: Preparación de nuevas versiones antes de su despliegue.

### **Flujo de Trabajo**
1. Se desarrollan nuevas funcionalidades en ramas `feature/*`.
2. Se fusionan en `dev` para pruebas y validaciones.
3. Cuando se alcanza una versión estable, se crea una rama `release/*`.
4. Tras las pruebas finales, la rama `release/*` se fusiona en `main` y se etiqueta con el número de versión correspondiente.
5. Si hay errores en producción, se crean ramas `hotfix/*` y se fusionan en `main` y `dev`.

---

## **3. Etiquetado de Versiones**

Cada nueva versión estable se debe etiquetar en Git usando el siguiente formato:

```
git tag -a vX.Y.Z -m "Versión X.Y.Z"
git push origin vX.Y.Z
```