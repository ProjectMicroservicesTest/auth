from dataclasses import dataclass, field

from fastapi import APIRouter

health_check_router = APIRouter(prefix="/auth/health-check", tags=["health-check"])


@dataclass(frozen=True)
class HealthCheckResponse:
    status: str = field(default="auth service healthy")


@health_check_router.get("/", response_model=HealthCheckResponse)
def health_check() -> HealthCheckResponse:
    return HealthCheckResponse(status="auth service healthy")