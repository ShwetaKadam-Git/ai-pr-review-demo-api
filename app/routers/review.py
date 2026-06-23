import json
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.database import ReviewRecord
from app.models.review import ReviewRequest, ReviewResponse, Finding
from app.services.mock_ai_services import run_mock_review
from app.config import settings

router = APIRouter()


def verify_api_key(authorization: str = Header(default="")):
    if not settings.api_key:
        return
    expected = f"Bearer {settings.api_key}"
    if authorization != expected:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


@router.post("/review", response_model=ReviewResponse)
def create_review(payload: ReviewRequest, db: Session = Depends(get_db),
                   _=Depends(verify_api_key)):
    if settings.ai_mode == "real":
        from app.services.real_ai_service import run_real_review
        raw_findings = run_real_review(payload.files, payload.policy)
    else:
        raw_findings = run_mock_review(payload.files, payload.policy)

    error_count = sum(1 for f in raw_findings if f["severity"] == "error")
    warning_count = sum(1 for f in raw_findings if f["severity"] == "warning")

    record = ReviewRecord(
        policy=payload.policy,
        finding_count=len(raw_findings),
        error_count=error_count,
        warning_count=warning_count,
        findings_json=json.dumps(raw_findings),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return ReviewResponse(
        id=record.id,
        policy=record.policy,
        findings=[Finding(**f) for f in raw_findings],
    )