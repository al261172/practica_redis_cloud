import os
from dataclasses import dataclass
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class ConfiguracionRedis:
    url: str

def obtener_configuracion() -> ConfiguracionRedis:
    # Lee la configuración de Redis desde las variables de entorno.
    # Retorna una instancia inmutable de `ConfiguracionRedis` con la URL.
    # Usa `REDIS_URL` o el valor por defecto `redis://localhost:6379/0`.

    url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    return ConfiguracionRedis(url = url)


def obtener_conexion() -> Redis:
    config = obtener_configuracion()
    conexion = Redis.from_url(config.url, decode_responses=True)
    conexion.ping()
    return conexion