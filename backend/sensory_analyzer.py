"""
Sensory Analysis Engine

Implements ML-based and rule-based classification of sensory states.
Uses a trained classifier with fallback to rule-based logic.
Determines if the user is calm, overstimulated, or under-stimulated.
"""

from typing import Literal, Dict
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

from models import SensoryInput, SensoryAnalysisResponse


class SensoryAnalyzer:
    """
    Analyzes sensory input levels and classifies the user's sensory state.
    
    Uses ML-based classification with fallback to rule-based logic:
    - Primary: RandomForest classifier trained on mock sensory data
    - Fallback: Rule-based thresholds if ML fails
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
        """Initialize the sensory analyzer with ML model"""
        self.ml_model = None
        self.scaler = None
        self.use_ml = False
        
        try:
            self._train_ml_model()
            self.use_ml = True
            print("✓ ML model initialized successfully")
        except Exception as e:
            print(f"⚠ ML model initialization failed, using rule-based fallback: {e}")
            self.use_ml = False

    def _generate_mock_training_data(self):
        """
        Generate mock training data for sensory analysis
        
        Returns:
            X: Feature matrix (sound, light, touch levels)
            y: Target labels (0=calm, 1=overstimulated, 2=under-stimulated)
        """
        np.random.seed(42)
        
        # Generate calm samples (balanced sensory levels: 30-70)
        calm_samples = 100
        calm_X = np.random.uniform(30, 70, (calm_samples, 3))
        calm_y = np.zeros(calm_samples)
        
        # Generate overstimulated samples (high levels: 65-100)
        over_samples = 100
        over_X = np.random.uniform(65, 100, (over_samples, 3))
        over_y = np.ones(over_samples)
        
        # Generate under-stimulated samples (low levels: 0-35)
        under_samples = 100
        under_X = np.random.uniform(0, 35, (under_samples, 3))
        under_y = np.full(under_samples, 2)
        
        # Add some noise and edge cases
        # Mixed high/low levels for overstimulated
        mixed_over = 30
        mixed_over_X = np.zeros((mixed_over, 3))
        for i in range(mixed_over):
            # At least 2 high values
            high_indices = np.random.choice(3, 2, replace=False)
            mixed_over_X[i] = np.random.uniform(20, 40, 3)
            mixed_over_X[i, high_indices] = np.random.uniform(70, 95, 2)
        mixed_over_y = np.ones(mixed_over)
        
        # Combine all data
        X = np.vstack([calm_X, over_X, under_X, mixed_over_X])
        y = np.concatenate([calm_y, over_y, under_y, mixed_over_y])
        
        # Shuffle
        indices = np.random.permutation(len(X))
        X = X[indices]
        y = y[indices]
        
        return X, y

    def _train_ml_model(self):
        """Train a RandomForest classifier on mock sensory data"""
        # Generate training data
        X_train, y_train = self._generate_mock_training_data()
        
        # Standardize features
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        # Train RandomForest classifier
        self.ml_model = RandomForestClassifier(
            n_estimators=50,
            max_depth=10,
            random_state=42,
            min_samples_split=5
        )
        self.ml_model.fit(X_train_scaled, y_train)
        
        # Print training accuracy
        train_accuracy = self.ml_model.score(X_train_scaled, y_train)
        print(f"  ML Model Training Accuracy: {train_accuracy:.2%}")

    def analyze(self, sensory_input: SensoryInput) -> SensoryAnalysisResponse:
        """
        Analyze sensory input and return classification and recommendations
        
        Uses ML model if available, falls back to rule-based classification

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

        # Classify sensory state using ML or rule-based
        if self.use_ml:
            sensory_state = self._classify_state_ml(sensory_input)
        else:
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

    def _classify_state_ml(self, sensory_input: SensoryInput) -> Literal["calm", "overstimulated", "under-stimulated"]:
        """
        Classify sensory state using ML model
        
        Args:
            sensory_input: SensoryInput object
            
        Returns:
            One of: "calm", "overstimulated", "under-stimulated"
        """
        try:
            # Prepare features
            features = np.array([[
                sensory_input.sound_level,
                sensory_input.light_level,
                sensory_input.touch_level
            ]])
            
            # Scale features
            features_scaled = self.scaler.transform(features)
            
            # Predict
            prediction = self.ml_model.predict(features_scaled)[0]
            
            # Map prediction to state
            state_mapping = {
                0: "calm",
                1: "overstimulated",
                2: "under-stimulated"
            }
            
            return state_mapping.get(prediction, "calm")
            
        except Exception as e:
            print(f"⚠ ML prediction failed, using rule-based fallback: {e}")
            sensory_score = (
                sensory_input.sound_level +
                sensory_input.light_level +
                sensory_input.touch_level
            ) / 3
            return self._classify_state(sensory_score)

    def _classify_state(self, sensory_score: float) -> Literal["calm", "overstimulated", "under-stimulated"]:
        """
        Classify sensory state based on overall sensory score (rule-based fallback)

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
