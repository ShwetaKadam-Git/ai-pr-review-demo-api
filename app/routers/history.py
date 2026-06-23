import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.database import ReviewRecord
from app.models.review import ReviewSummary, ReviewResponse, Finding

router = APIRouter()


@router.get("/reviews", response_model=list[ReviewSummary])
def list_reviews(db: Session = Depends(get_db), limit: int = 50):
    records = db.query(ReviewRecord).order_by(ReviewRecord.id.desc()).limit(limit).all()
    return [
        ReviewSummary(
            id=r.id,
            policy=r.policy,
            finding_count=r.finding_count,
            error_count=r.error_count,
            warning_count=r.warning_count,
            created_at=r.created_at.isoformat() if r.created_at else None,
        )
        for r in records
    ]


@router.get("/reviews/{review_id}", response_model=ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    record = db.query(ReviewRecord).filter(ReviewRecord.id == review_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Review not found")
    findings = json.loads(record.findings_json)
    return ReviewResponse(
        id=record.id,
        policy=record.policy,
        findings=[Finding(**f) for f in findings],
    )