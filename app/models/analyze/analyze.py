from pydantic import BaseModel, Field
from typing import Dict

class AnalyzeRequest(BaseModel):
    text: str = Field(
        ...,
        description="Text to analyze for sentiment",
        example="I really enjoyed using this product, it exceeded my expectations!"
    )

class AnalyzeResponse(BaseModel):
    sentiment: str = Field(
        ...,
        description="Overall sentiment (POSITIVE or NEGATIVE)",
        example="POSITIVE"
    )
    confidence: float = Field(
        ...,
        description="Confidence score (0.0 to 1.0)",
        example=0.98
    )
    scores: Dict[str, float] = Field(
        ...,
        description="Detailed scores for each possible label",
        example={"POSITIVE": 0.98, "NEGATIVE": 0.02}
    )
