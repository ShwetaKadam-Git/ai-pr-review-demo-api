from typing import List, Optional
from pydantic import BaseModel


class FileInput(BaseModel):
    filename: str
    patch: str = ""


class ReviewRequest(BaseModel):
    policy: str = "default"
    files: List[FileInput]


class Finding(BaseModel):
    severity: str
    rule: str
    location: str
    detail: str


class ReviewResponse(BaseModel):
    id: int
    policy: str
    findings: List[Finding]


class ReviewSummary(BaseModel):
    id: int
    policy: str
    finding_count: int
    error_count: int
    warning_count: int
    created_at: Optional[str] = None