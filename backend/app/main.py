from contextlib import asynccontextmanager
import threading

from fastapi import FastAPI

from app.api.routes.attacks import router as attacks_router
from app.api.websocket.attacks import router as attacks_ws_router
from app.core.config import settings
from app.honeypot.ssh_server import start_ssh_honeypot


@asynccontextmanager
async def lifespan(app: FastAPI):
    stop_event = threading.Event()
    honeypot_thread = threading.Thread(
        target=start_ssh_honeypot,
        kwargs={"stop_event": stop_event},
        daemon=True,
    )
    honeypot_thread.start()

    yield

    stop_event.set()
    honeypot_thread.join(timeout=2)


app = FastAPI(
    title=settings.app_name,
    description="SSH Honeypot & Threat Monitoring System",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(attacks_router)
app.include_router(attacks_ws_router)


@app.get("/")
def home():
    return {
        "project": settings.app_name,
        "status": "online",
        "honeypot": {
            "host": settings.honeypot_host,
            "port": settings.honeypot_port,
        },
    }
