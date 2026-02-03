"""
Data models for the Autism Support Platform

Uses Pydantic for request/response validation and documentation.
"""

from pydantic import BaseModel, Field
from typing import Literal, Optional


# ============================================================================
# SENSORY ANALYSIS MODELS
# ============================================================================

class SensoryInput(BaseModel):
    """
    Request model for sensory input analysis
    
    All levels should be in the range 0-100 where:
    - 0 = minimal/no input
    - 100 = maximum/intense input
    """
    sound_level: int = Field(
        ..., 
        ge=0, 
        le=100, 
        description="Sound level intensity (0-100)"
    )
    light_level: int = Field(
        ..., 
        ge=0, 
        le=100, 
        description="Light level intensity (0-100)"
    )
    touch_level: int = Field(
        ..., 
        ge=0, 
        le=100, 
        description="Touch sensitivity level (0-100)"
    )
    user_id: Optional[str] = Field(
        None,
        description="Optional user identifier for personalization"
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "sound_level": 45,
                "light_level": 60,
                "touch_level": 35,
                "user_id": "user_001"
            }
        }
    }


class SensoryAnalysisResponse(BaseModel):
    """
    Response model for sensory analysis
    
    Returns the classified sensory state and recommendations
    """
    sensory_state: Literal["calm", "overstimulated", "under-stimulated"] = Field(
        description="Current sensory state classification"
    )
    sensory_score: float = Field(
        description="Overall sensory load score (0-100)"
    )
    individual_scores: dict = Field(
        description="Breakdown of individual sensory input scores"
    )
    recommendation: str = Field(
        description="Personalized recommendation for the user"
    )
    alert_level: Literal["low", "medium", "high"] = Field(
        description="Priority level for caregiver attention"
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "sensory_state": "calm",
                "sensory_score": 46.7,
                "individual_scores": {
                    "sound_level": 45,
                    "light_level": 60,
                    "touch_level": 35
                },
                "recommendation": "Current sensory environment is comfortable. Continue with regular activities.",
                "alert_level": "low"
            }
        }
    }
