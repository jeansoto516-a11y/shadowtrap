import asyncio
import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.core.config import settings


router = APIRouter(tags=["websocket"])


@router.websocket("/ws/attacks")
async def attacks_websocket(websocket: WebSocket):
    await websocket.accept()

    log_file = settings.log_file
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.touch(exist_ok=True)

    position = log_file.stat().st_size

    try:
        await websocket.send_json(
            {
                "event_type": "websocket_connected",
                "message": "connected to ShadowTrap event stream",
            }
        )

        while True:
            with log_file.open("r", encoding="utf-8") as file:
                file.seek(position)
                lines = file.readlines()
                position = file.tell()

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                try:
                    payload = json.loads(line)
                except json.JSONDecodeError:
                    payload = {
                        "event_type": "invalid_log_line",
                        "raw": line,
                    }

                await websocket.send_json(payload)

            await asyncio.sleep(1)
    except WebSocketDisconnect:
        return
