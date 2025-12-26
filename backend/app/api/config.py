from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from app.config.resolver import ConfigLoadError, ConfigValidationError, resolve_settings
from app.schemas.config_summary import ConfigSetting, ConfigSummary

router = APIRouter()


@router.get("/config", response_model=ConfigSummary)
def get_config_summary() -> ConfigSummary:
    try:
        resolved = resolve_settings()
    except ConfigLoadError as exc:
        raise HTTPException(status_code=400, detail={"code": exc.code, "message": "Config file error"}) from exc
    except ConfigValidationError as exc:
        raise HTTPException(
            status_code=400,
            detail={
                "code": "invalid_config",
                "message": "Configuration validation failed",
                "issues": [issue.__dict__ for issue in exc.issues],
            },
        ) from exc

    settings = [
        ConfigSetting(
            key=entry.key,
            value=entry.value,
            source=entry.source,
            sensitive=entry.sensitive,
        )
        for entry in resolved.entries
    ]
    return ConfigSummary(
        settings=settings,
        validated_at=datetime.now(timezone.utc).isoformat(),
        version="1",
    )
