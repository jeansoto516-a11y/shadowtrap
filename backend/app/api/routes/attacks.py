from fastapi import APIRouter, Query

from app.services.attack_service import get_attack_summary, list_attack_events


router = APIRouter(prefix="/attacks", tags=["attacks"])


@router.get("")
def list_attacks(
    limit: int = Query(default=100, ge=1, le=1000),
    event_type: str | None = Query(default=None),
):
    return {
        "items": list_attack_events(limit=limit, event_type=event_type),
        "limit": limit,
        "event_type": event_type,
    }


@router.get("/latest")
def latest_attacks(limit: int = Query(default=20, ge=1, le=100)):
    return {
        "items": list_attack_events(limit=limit),
        "limit": limit,
    }


@router.get("/summary")
def attack_summary():
    return get_attack_summary()
