# 📜 CHANGELOG - ComuniVeci Map Service

Historial de cambios del servicio de visualización de publicaciones aprobadas en el mapa.

---

## [1.0.0] - 2025-06-11

### 🚀 Funcionalidades iniciales

- ✅ Se crea el proyecto con FastAPI y Poetry.
- ✅ Se configura el entorno con variables en .env.
- ✅ Se implementa el endpoint público:

  - GET /api/map/posts/
    - Devuelve los posts aprobados desde el post-service.
    - Funciona como proxy transparente hacia POST_SERVICE_URL.

- ✅ Manejo de errores si POST_SERVICE_URL no está configurada o si falla la conexión.
- ✅ Documentación básica en README.md.
- ✅ Archivo .env.example agregado.
- ✅ Archivo .gitignore configurado para entornos virtuales y archivos temporales.

---

## 📅 Próximas mejoras sugeridas

- [ ] Caching de resultados para mejorar el rendimiento.
- [ ] Filtros por zona geográfica o categorías (si se extiende el dominio).
- [ ] Tests automáticos con pytest o HTTPX.
- [ ] Agregar esquema OpenAPI con Swagger (FastAPI lo expone automáticamente).