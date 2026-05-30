import json
import logging
from datetime import datetime, timezone

from app.core.config import settings


logger = logging.getLogger("shadowtrap.honeypot")
logger.setLevel(logging.INFO)
logger.propagate = False


def _configure_logger() -> None:
    if logger.handlers:
        return

    settings.log_file.parent.mkdir(parents=True, exist_ok=True)

    file_handler = logging.FileHandler(settings.log_file, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(message)s"))

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("[SHADOWTRAP] %(message)s"))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def log_event(event_type: str, **data) -> None:
    _configure_logger()

    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        **data,
    }
    logger.info(json.dumps(payload, ensure_ascii=False, default=str))


def log_connection(ip: str, port: int) -> None:
    log_event("connection", ip=ip, port=port)


def log_login_attempt(ip: str, port: int, username: str, password: str) -> None:
    log_event(
        "login_attempt",
        ip=ip,
        port=port,
        username=username,
        password=password,
    )


def log_command(ip: str, port: int, username: str | None, command: str) -> None:
    log_event(
        "command",
        ip=ip,
        port=port,
        username=username,
        command=command,
    )
