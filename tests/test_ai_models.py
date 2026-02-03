"""
Unit tests for the AI Models module
"""

import unittest
import numpy as np
from autism_support.ai_models import (
    EmotionDetector,
    PatternRecognizer,
    TriggerPredictor
)


class TestEmotionDetector(unittest.TestCase):
    """Test cases for EmotionDetector."""
    
    def setUp(self):
        self.detector = EmotionDetector()
    
    def test_detect_from_happy_text(self):
        """Test emotion detection from happy text."""
        text = "I am so happy and excited today!"
        result = self.detector.detect_from_text(text)
        
        self.assertIn('emotions', result)
        self.assertIn('dominant_emotion', result)
        self.assertIn(result['dominant_emotion'], ['happy', 'excited'])
    
    def test_detect_from_sad_text(self):
        """Test emotion detection from sad text."""
        text = "I feel very sad and unhappy."
        result = self.detector.detect_from_text(text)
        
        self.assertEqual(result['dominant_emotion'], 'sad')
    
    def test_detect_from_audio_features(self):
        """Test emotion detection from audio features."""
        # High pitch + high energy = excited
        result = self.detector.detect_from_audio_features(
            pitch=0.8,
            energy=0.8,
            speech_rate=0.5
        )
        
        self.assertIn('emotions', result)
        self.assertIn('dominant_emotion', result)
        self.assertIn(result['dominant_emotion'], ['excited', 'happy'])


class TestPatternRecognizer(unittest.TestCase):
    """Test cases for PatternRecognizer."""
    
    def setUp(self):
        self.recognizer = PatternRecognizer()
    
    def test_insufficient_data(self):
        """Test learning with insufficient data."""
        data = [{'modality': 'visual', 'brightness': 0.5}]
        result = self.recognizer.learn_preferences(data)
        
        self.assertEqual(result['status'], 'insufficient_data')
    
    def test_learn_preferences(self):
        """Test learning sensory preferences."""
        # Create enough samples
        data = []
        for i in range(10):
            data.append({
                'modality': 'visual',
                'brightness': 0.5 + i * 0.01,
                'contrast': 0.4,
                'is_overwhelming': False
            })
        
        result = self.recognizer.learn_preferences(data)
        
        self.assertIn('preferences', result)
        self.assertIn('visual', result['preferences'])
    
    def test_predict_comfort(self):
        """Test predicting comfort level."""
        # First learn some patterns
        data = []
        for i in range(10):
            data.append({
                'modality': 'audio',
                'volume': 0.3 + i * 0.01,
                'is_overwhelming': False
            })
        
        self.recognizer.learn_preferences(data)
        
        # Now predict
        test_input = {'modality': 'audio', 'volume': 0.35}
        result = self.recognizer.predict_comfort_level(test_input)
        
        self.assertIn('prediction', result)


class TestTriggerPredictor(unittest.TestCase):
    """Test cases for TriggerPredictor."""
    
    def setUp(self):
        self.predictor = TriggerPredictor()
    
    def test_low_risk_assessment(self):
        """Test risk assessment with low risk context."""
        context = {
            'hour': 14,
            'environment_changed': False,
            'sensory_load': 0.2,
            'routine_disrupted': False
        }
        
        result = self.predictor.assess_risk(context)
        
        self.assertEqual(result['risk_level'], 'low')
        self.assertLess(result['risk_score'], 0.3)
    
    def test_high_risk_assessment(self):
        """Test risk assessment with high risk context."""
        context = {
            'hour': 23,
            'environment_changed': True,
            'sensory_load': 0.9,
            'routine_disrupted': True
        }
        
        result = self.predictor.assess_risk(context)
        
        self.assertEqual(result['risk_level'], 'high')
        self.assertGreater(result['risk_score'], 0.6)
    
    def test_predict_trigger_likelihood(self):
        """Test predicting trigger likelihood for activities."""
        # Low risk activity
        low_risk = self.predictor.predict_trigger_likelihood(
            upcoming_activity="Reading at home",
            context={'current_stress_level': 0.2}
        )
        
        self.assertEqual(low_risk['risk_level'], 'low')
        
        # High risk activity
        high_risk = self.predictor.predict_trigger_likelihood(
            upcoming_activity="Loud crowd at unfamiliar place",
            context={'current_stress_level': 0.7}
        )
        
        self.assertGreater(high_risk['trigger_likelihood'], low_risk['trigger_likelihood'])


if __name__ == '__main__':
    unittest.main()
