import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAnalyzeEndpoint:
    """Tests for the /analyze endpoint."""
    
    def test_analyze_positive_sentiment(self):
        """Test positive sentiment classification."""
        response = client.post(
            "/analyze",
            json={"text": "I love this product! It's amazing and works perfectly."}
        )
        assert response.status_code == 200
        data = response.json()
        
        # Check response structure
        assert "sentiment" in data
        assert "confidence" in data
        assert "scores" in data
        
        # Check expected values for positive text
        assert data["sentiment"] == "POSITIVE"
        assert data["confidence"] > 0.5
        assert "POSITIVE" in data["scores"]
        assert "NEGATIVE" in data["scores"]
        assert data["scores"]["POSITIVE"] > data["scores"]["NEGATIVE"]
    
    def test_analyze_negative_sentiment(self):
        """Test negative sentiment classification."""
        response = client.post(
            "/analyze",
            json={"text": "This is terrible. I hate it and it doesn't work at all."}
        )
        assert response.status_code == 200
        data = response.json()
        
        # Check response structure
        assert "sentiment" in data
        assert "confidence" in data
        assert "scores" in data
        
        # Check expected values for negative text
        assert data["sentiment"] == "NEGATIVE"
        assert data["confidence"] > 0.5
        assert "POSITIVE" in data["scores"]
        assert "NEGATIVE" in data["scores"]
        assert data["scores"]["NEGATIVE"] > data["scores"]["POSITIVE"]
    
    def test_empty_text(self):
        """Test behavior with empty text."""
        response = client.post(
            "/analyze",
            json={"text": ""}
        )
        assert response.status_code == 200
        data = response.json()
        
        # Check neutral response for empty text
        assert data["sentiment"] == "NEUTRAL"
        assert data["confidence"] == 0.0
    
    def test_missing_text(self):
        """Test error handling for missing text field."""
        response = client.post(
            "/analyze",
            json={}
        )
        assert response.status_code == 422  # Validation error
