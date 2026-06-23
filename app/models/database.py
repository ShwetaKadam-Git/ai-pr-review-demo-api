from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func

from app.db.database import Base


class ReviewRecord(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    policy = Column(String, nullable=False)
    finding_count = Column(Integer, nullable=False, default=0)
    error_count = Column(Integer, nullable=False, default=0)
    warning_count = Column(Integer, nullable=False, default=0)
    findings_json = Column(Text, nullable=False, default="[]")
    created_at = Column(DateTime, server_default=func.now())