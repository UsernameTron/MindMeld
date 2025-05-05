from fastapi import APIRouter
from app.models.analyze.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.analyze_service import AnalyzeService

router = APIRouter(prefix="/analyze", tags=["Sentiment Analysis"])

# Create a singleton instance of the service
analyze_service = AnalyzeService()

@router.post(
    "",
    response_model=AnalyzeResponse,
    summary="Analyze text sentiment",
    description="Analyzes the sentiment of provided text using Hugging Face transformers"
)
async def analyze_text(request: AnalyzeRequest) -> AnalyzeResponse:
    """
    Analyze the sentiment of the provided text.
    
    Returns a sentiment classification (POSITIVE/NEGATIVE), confidence score,
    and detailed scores for each possible sentiment label.
    """
    return await analyze_service.analyze_text(request)
