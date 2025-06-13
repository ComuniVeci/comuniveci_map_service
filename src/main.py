import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import requests
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Obtener la URL del post-service desde la variable de entorno
POST_SERVICE_URL = os.getenv("POST_SERVICE_URL")

app = FastAPI(
    title="ComuniVeci Map Service",
    description="Servicio de consulta pública de publicaciones aprobadas para visualización en mapa.",
    version="1.0.0",
    contact={
        "name": "Equipo ComuniVeci",
        "email": "soporte@comuniveci.org"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Habilitar CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # origen permitido (frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/map/posts/", summary="Obtener posts aprobados", description="Devuelve todos los posts aprobados desde post-service.")
def get_approved_posts():
    if not POST_SERVICE_URL:
        return {"error": "POST_SERVICE_URL no está configurada"}, 500

    try:
        response = requests.get(POST_SERVICE_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error al conectar con post-service: {str(e)}"}, 502