from transformers import pipeline
from app.core.config import settings
from app.models.analyze.analyze import AnalyzeRequest, AnalyzeResponse
from loguru import logger

class AnalyzeService:
    def __init__(self):
        """Initialize the analyze service with a Hugging Face sentiment analysis pipeline."""
        self._initialize_pipeline()
        
    def _initialize_pipeline(self):
        """Load the sentiment analysis model based on environment configuration."""
        logger.info(f"Loading sentiment analysis model: {settings.DEFAULT_MODEL_NAME}")
        logger.info(f"Using device: {settings.INFERENCE_DEVICE}")
        
        # Set device based on environment configuration (MPS or CPU)
        device = 0 if settings.INFERENCE_DEVICE == "mps" else -1
        
        self.pipeline = pipeline(
            task="sentiment-analysis",
            model=settings.DEFAULT_MODEL_NAME,
            device=device
        )
        logger.info("Sentiment analysis model loaded successfully")
        
    async def analyze_text(self, request: AnalyzeRequest) -> AnalyzeResponse:
        """
        Analyze the sentiment of the provided text.
        
        Args:
            request: AnalyzeRequest containing the text to analyze
            
        Returns:
            AnalyzeResponse with sentiment classification results
        """
        if not request.text.strip():
            logger.warning("Empty text provided for sentiment analysis")
            return AnalyzeResponse(
                sentiment="NEUTRAL",
                confidence=0.0,
                scores={"POSITIVE": 0.0, "NEGATIVE": 0.0}
            )
        
        # Perform sentiment analysis
        logger.debug(f"Analyzing text: {request.text[:50]}...")
        result = self.pipeline(request.text)[0]
        
        # Extract results
        sentiment = result["label"]
        confidence = result["score"]
        
        # Create a scores dictionary for all possible labels
        # DistilBERT SST-2 only returns score for the predicted label,
        # so we need to calculate the other score
        scores = {
            sentiment: confidence,
            "POSITIVE" if sentiment == "NEGATIVE" else "NEGATIVE": 1.0 - confidence
        }
        
        logger.info(f"Sentiment analysis complete: {sentiment} with {confidence:.2f} confidence")
        
        return AnalyzeResponse(
            sentiment=sentiment,
            confidence=confidence,
            scores=scores
        )
