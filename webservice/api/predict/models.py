from typing import List

from pydantic import BaseModel


class TracePoint(BaseModel):
    x: float
    y: float
    t: float


class PredictRequest(BaseModel):
    trace: List[TracePoint]
    prompt: str


class PredictResponse(BaseModel):
    action: str
    words: List[str]
