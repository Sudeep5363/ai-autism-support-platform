"""
Sensory Analysis Engine

Implements rule-based classification of sensory states based on input levels.
Determines if the user is calm, overstimulated, or under-stimulated.
"""

from typing import Literal, Dict
from models import SensoryInput, SensoryAnalysisResponse


class SensoryAnalyzer:
    """
    Analyzes sensory input levels and classifies the user's sensory state.
    
    Uses simple rule-based logic:
    - Calm: sensory load is balanced (moderate levels)
    - Overstimulated: sensory load is high (too much input)
    - Under-stimulated: sensory load is low (insufficient input)
    """

    # Thresholds for classification (0-100 scale)
    OVERSTIMULATION_THRESHOLD = 70  # Above this = overstimulated
    UNDER_STIMULATION_THRESHOLD = 30  # Below this = under-stimulated
    # Between these thresholds = calm

    # Alert level thresholds based on deviation from calm state
    HIGH_ALERT_THRESHOLD = 80
    MEDIUM_ALERT_THRESHOLD = 60

    def __init__(self):
        """Initialize the sensory analyzer"""
        pass

    def analyze(self, sensory_input: SensoryInput) -> SensoryAnalysisResponse:
        """
        Analyze sensory input and return classification and recommendations
        
        Args:
            sensory_input: SensoryInput object with sound, light, and touch levels
            
        Returns:
            SensoryAnalysisResponse with state, score, and recommendations
        """
        # Calculate overall sensory score (simple average)
        sensory_score = (
            sensory_input.sound_level +
            sensory_input.light_level +
            sensory_input.touch_level
        ) / 3

        # Classify sensory state
        sensory_state = self._classify_state(sensory_score)

        # Generate recommendation based on state
        recommendation = self._generate_recommendation(sensory_state, sensory_input)

        # Determine alert level for caregivers
        alert_level = self._determine_alert_level(sensory_state, sensory_score)

        # Build response
        response = SensoryAnalysisResponse(
            sensory_state=sensory_state,
            sensory_score=round(sensory_score, 1),
            individual_scores={
                "sound_level": sensory_input.sound_level,
                "light_level": sensory_input.light_level,
                "touch_level": sensory_input.touch_level
            },
            recommendation=recommendation,
            alert_level=alert_level
        )

        return response

    def _classify_state(self, sensory_score: float) -> Literal["calm", "overstimulated", "under-stimulated"]:
        """
        Classify sensory state based on overall sensory score
        
        Args:
            sensory_score: Average of all sensory input levels
            
        Returns:
            One of: "calm", "overstimulated", "under-stimulated"
        """
        if sensory_score >= self.OVERSTIMULATION_THRESHOLD:
            return "overstimulated"
        elif sensory_score <= self.UNDER_STIMULATION_THRESHOLD:
            return "under-stimulated"
        else:
            return "calm"

    def _generate_recommendation(
        self, 
        sensory_state: str, 
        sensory_input: SensoryInput
    ) -> str:
        """
        Generate personalized recommendations based on sensory state
        
        Args:
            sensory_state: Current classified sensory state
            sensory_input: Original sensory input data
            
        Returns:
            String recommendation for the user/caregiver
        """
        recommendations = {
            "calm": self._calm_recommendations(sensory_input),
            "overstimulated": self._overstimulation_recommendations(sensory_input),
            "under-stimulated": self._under_stimulation_recommendations(sensory_input)
        }

        return recommendations.get(sensory_state, "No recommendation available")

    def _calm_recommendations(self, sensory_input: SensoryInput) -> str:
        """Generate recommendations for calm state"""
        return (
            "✓ Current sensory environment is comfortable. "
            "Continue with regular activities. Monitor for changes."
        )

    def _overstimulation_recommendations(self, sensory_input: SensoryInput) -> str:
        """
        Generate recommendations for overstimulated state
        
        Highlight which sensory inputs are most problematic
        """
        high_inputs = []

        if sensory_input.sound_level >= 70:
            high_inputs.append("loud sounds")
        if sensory_input.light_level >= 70:
            high_inputs.append("bright light")
        if sensory_input.touch_level >= 70:
            high_inputs.append("tactile input")

        if high_inputs:
            triggers = ", ".join(high_inputs)
            return (
                f"⚠️ OVERSTIMULATED: Reduce {triggers}. "
                "Find a quiet, dimly-lit space. Try deep breathing or calming activities."
            )
        else:
            return (
                "⚠️ OVERSTIMULATED: Overall sensory input is high. "
                "Reduce environmental stimuli and take a break."
            )

    def _under_stimulation_recommendations(self, sensory_input: SensoryInput) -> str:
        """Generate recommendations for under-stimulated state"""
        return (
            "↓ UNDER-STIMULATED: Try engaging activities like music, fidget toys, "
            "or gentle movement. Seek sensory input to improve engagement."
        )

    def _determine_alert_level(self, sensory_state: str, sensory_score: float) -> Literal["low", "medium", "high"]:
        """
        Determine the alert level for caregiver notification
        
        Args:
            sensory_state: Current classified sensory state
            sensory_score: Overall sensory score
            
        Returns:
            One of: "low", "medium", "high"
        """
        if sensory_state == "calm":
            return "low"
        elif sensory_score >= self.HIGH_ALERT_THRESHOLD:
            return "high"  # Severe overstimulation or under-stimulation
        else:
            return "medium"  # Moderate concern


# Create a global analyzer instance
sensory_analyzer = SensoryAnalyzer()
