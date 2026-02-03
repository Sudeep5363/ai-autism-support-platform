"""
AI-Enabled Sensory & Communication Support Platform - Backend
Main FastAPI application entry point

This module sets up the FastAPI server and initializes core API endpoints.
Future modules (sensory analysis, communication, personalization) will be added as blueprints.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from models import SensoryInput, SensoryAnalysisResponse
from sensory_analyzer import sensory_analyzer

# Initialize FastAPI application
app = FastAPI(
    title="Autism Support Platform API",
    description="AI-powered sensory and communication support platform",
    version="0.1.0"
)

# Enable CORS for frontend communication (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict to specific frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# HEALTH CHECK ENDPOINT
# ============================================================================

@app.get("/")
def read_root():
    """
    Root endpoint - confirms API is running
    """
    return {
        "message": "Autism Support Platform API is running",
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint for monitoring
    Returns basic system status
    """
    return {
        "status": "healthy",
        "service": "autism-support-platform",
        "version": "0.1.0",
        "timestamp": datetime.now().isoformat()
    }


# ============================================================================
# PLACEHOLDER ENDPOINTS (to be implemented)
# ============================================================================

@app.get("/api/sensory-analysis")
def sensory_analysis_placeholder():
    """
    TODO: Implement sensory input analysis module
    Will accept sound, light, touch data and classify sensory state
    """
    return {"status": "not_implemented", "message": "Sensory analysis module coming soon"}


# ============================================================================
# SENSORY ANALYSIS ENDPOINTS
# ============================================================================

@app.post("/sensory/analyze", response_model=SensoryAnalysisResponse)
def analyze_sensory_input(sensory_input: SensoryInput) -> SensoryAnalysisResponse:
    """
    Analyze sensory input levels and classify the user's sensory state
    
    This endpoint accepts real-time sensory data and returns:
    - Classification: calm, overstimulated, or under-stimulated
    - Sensory score (0-100)
    - Personalized recommendations
    - Alert level for caregivers
    
    **Example Request:**
    ```json
    {
        "sound_level": 45,
        "light_level": 60,
        "touch_level": 35,
        "user_id": "user_001"
    }
    ```
    
    **Example Response (Calm):**
    ```json
    {
        "sensory_state": "calm",
        "sensory_score": 46.7,
        "individual_scores": {
            "sound_level": 45,
            "light_level": 60,
            "touch_level": 35
        },
        "recommendation": "✓ Current sensory environment is comfortable. Continue with regular activities. Monitor for changes.",
        "alert_level": "low"
    }
    ```
    
    **Example Response (Overstimulated):**
    ```json
    {
        "sensory_state": "overstimulated",
        "sensory_score": 75.0,
        "individual_scores": {
            "sound_level": 80,
            "light_level": 75,
            "touch_level": 70
        },
        "recommendation": "⚠️ OVERSTIMULATED: Reduce loud sounds, bright light, tactile input. Find a quiet, dimly-lit space. Try deep breathing or calming activities.",
        "alert_level": "high"
    }
    ```
    """
    try:
        # Use the sensory analyzer to classify the input
        response = sensory_analyzer.analyze(sensory_input)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing sensory input: {str(e)}")


@app.get("/api/communication-support")
def communication_support_placeholder():
    """
    TODO: Implement communication support module
    Will suggest adaptive responses based on user state
    """
    return {"status": "not_implemented", "message": "Communication support module coming soon"}


@app.get("/api/caregiver-dashboard")
def caregiver_dashboard_placeholder():
    """
    TODO: Implement caregiver dashboard data endpoint
    Will provide patterns, insights, and recommendations
    """
    return {"status": "not_implemented", "message": "Caregiver dashboard coming soon"}


# ============================================================================
# ERROR HANDLING
# ============================================================================

@app.get("/api/test-error")
def test_error():
    """
    Test endpoint to verify error handling
    """
    raise Exception("This is a test error")


if __name__ == "__main__":
    # Run with: uvicorn main:app --reload
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
