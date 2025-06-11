# 🗺️ ComuniVeci – Map Service

Este servicio proporciona una API REST ligera que expone los posts aprobados para ser visualizados en el mapa principal de la plataforma ComuniVeci. Funciona como un consumidor del post-service y está desarrollado con FastAPI siguiendo principios de servicios desacoplados.

## ⚙️ Tecnologías utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- requests
- python-dotenv
- Poetry

## 🚀 Instalación y configuración

1. Clona el repositorio

```bash
git clone https://github.com/<tu-usuario>/comuniveci-map-service.git
cd comuniveci-map-service
```

2. Instala Poetry (si no lo tienes)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Crea el archivo de entorno

```bash
cp .env.example .env
```

Edita .env según la URL donde esté corriendo el post-service:

```bash
POST_SERVICE_URL=http://localhost:8000/api/posts/approved/
```

4. Instala las dependencias del proyecto

```bash
poetry install
```

5. Ejecuta el servidor de desarrollo

```bash
poetry run uvicorn src.main:app --reload --port 8001
```

Esto levantará el servicio en:

http://localhost:8001/

## 🧪 API REST

| Método | Endpoint              | Descripción                                           |
|--------|-----------------------|-------------------------------------------------------|
| GET    | /api/map/posts/       | Devuelve todos los posts aprobados desde post-service |

Esta API puede ser consumida por el frontend de ComuniVeci para visualizar marcadores en un mapa usando herramientas como Leaflet.js.

## 📁 Estructura del proyecto

```bash
map-service/
├── .env.example
├── pyproject.toml
├── README.md
├── src/
│   └── main.py
```

## 🧪 Comando de prueba

```bash
curl http://localhost:8001/api/map/posts/ | jq
```

✅ Requiere que el servicio post-service esté corriendo y exponiendo
/api/posts/approved/.

## 🔒 Seguridad

Este servicio expone únicamente información pública (posts aprobados). No requiere autenticación.

## 📖 Documentación interactiva (Swagger y Redoc)

Este servicio expone su documentación OpenAPI automáticamente gracias a FastAPI.

Una vez el servidor está en ejecución, puedes acceder a:

- 📄 Swagger UI (interfaz interactiva):
  [http://localhost:8001/docs](http://localhost:8001/docs)

- 📘 Redoc (documentación estructurada):
  [http://localhost:8001/redoc](http://localhost:8001/redoc)

- 🧾 Esquema OpenAPI (JSON):
  [http://localhost:8001/openapi.json](http://localhost:8001/openapi.json)

### ✏️ Personalización

Los metadatos del servicio (nombre, versión, contacto, licencia) están definidos en el archivo src/main.py, dentro de la instancia de FastAPI:

```python
app = FastAPI(
    title="ComuniVeci Map Service",
    description="Servicio de consulta pública de publicaciones aprobadas para visualización en mapa.",
    version="1.0.0",
    contact={"name": "Equipo ComuniVeci", "email": "soporte@comuniveci.org"},
    license_info={"name": "MIT License", "url": "https://opensource.org/licenses/MIT"}
)
```

No necesitas instalar nada adicional para usar Swagger o Redoc: FastAPI lo provee por defecto.

## 🧠 Notas

- El servicio map-service no almacena datos propios.

- Actúa como un adaptador entre post-service y el frontend de mapa.

- Usa comunicación HTTP para desacoplar responsabilidades.