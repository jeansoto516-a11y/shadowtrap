import json
from pathlib import Path
from typing import Any

from app.core.config import settings


def _read_json_lines(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []

    events: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8") as log_file:
        for line_number, line in enumerate(log_file, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                events.append(
                    {
                        "event_type": "invalid_log_line",
                        "line_number": line_number,
                        "raw": line,
                    }
                )

    return events


def list_attack_events(limit: int = 100, event_type: str | None = None) -> list[dict[str, Any]]:
    events = _read_json_lines(settings.log_file)

    if event_type:
        events = [event for event in events if event.get("event_type") == event_type]

    return events[-limit:]


def get_attack_summary() -> dict[str, Any]:
    events = _read_json_lines(settings.log_file)
    counts: dict[str, int] = {}

    for event in events:
        event_type = str(event.get("event_type", "unknown"))
        counts[event_type] = counts.get(event_type, 0) + 1

    return {
        "total_events": len(events),
        "by_event_type": counts,
        "latest_event": events[-1] if events else None,
    }
