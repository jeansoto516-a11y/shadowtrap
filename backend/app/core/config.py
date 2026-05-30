import os
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default

    try:
        return int(value)
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "ShadowTrap")
    honeypot_host: str = os.getenv("HONEYPOT_HOST", "0.0.0.0")
    honeypot_port: int = _int_env("HONEYPOT_PORT", 2222)
    log_file: Path = Path(os.getenv("SHADOWTRAP_LOG_FILE", BASE_DIR / "logs" / "attacks.log"))


settings = Settings()
