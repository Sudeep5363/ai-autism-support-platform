"""
AI Models Module

Provides AI/ML models and utilities including:
- Sentiment and emotion detection
- Pattern recognition for sensory preferences
- Predictive analytics for triggers
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class EmotionDetector:
    """Detects emotions from various inputs using AI models."""
    
    def __init__(self):
        self.emotion_labels = ['happy', 'sad', 'angry', 'anxious', 'calm', 'excited', 'frustrated']
        self.confidence_threshold = 0.5
    
    def detect_from_text(self, text: str) -> Dict:
        """
        Detect emotions from text using NLP.
        
        Args:
            text: Input text
            
        Returns:
            Dict with emotion predictions
        """
        # Simplified emotion detection based on keywords
        # In production, would use transformer models like BERT
        
        text_lower = text.lower()
        
        emotion_scores = {
            'happy': self._score_emotion(text_lower, ['happy', 'joy', 'glad', 'great', 'wonderful', 'excited']),
            'sad': self._score_emotion(text_lower, ['sad', 'unhappy', 'down', 'depressed', 'miserable']),
            'angry': self._score_emotion(text_lower, ['angry', 'mad', 'furious', 'annoyed', 'irritated']),
            'anxious': self._score_emotion(text_lower, ['anxious', 'worried', 'nervous', 'scared', 'afraid']),
            'calm': self._score_emotion(text_lower, ['calm', 'peaceful', 'relaxed', 'serene', 'tranquil']),
            'excited': self._score_emotion(text_lower, ['excited', 'thrilled', 'enthusiastic', 'eager']),
            'frustrated': self._score_emotion(text_lower, ['frustrated', 'stuck', 'confused', 'lost'])
        }
        
        # Get dominant emotion
        dominant_emotion = max(emotion_scores.items(), key=lambda x: x[1])
        
        return {
            'text': text,
            'emotions': emotion_scores,
            'dominant_emotion': dominant_emotion[0],
            'confidence': dominant_emotion[1],
            'timestamp': datetime.now().isoformat()
        }
    
    def _score_emotion(self, text: str, keywords: List[str]) -> float:
        """Score emotion based on keyword presence."""
        count = sum(1 for keyword in keywords if keyword in text)
        return min(1.0, count * 0.3)  # Scale to 0-1
    
    def detect_from_audio_features(self, 
                                   pitch: float,
                                   energy: float,
                                   speech_rate: float) -> Dict:
        """
        Detect emotions from audio features.
        
        Args:
            pitch: Pitch level (0-1)
            energy: Energy/volume level (0-1)
            speech_rate: Speech rate (0-1, 0.5 is normal)
            
        Returns:
            Dict with emotion predictions
        """
        # Simplified model based on acoustic features
        # In production, would use deep learning models
        
        emotion_scores = {}
        
        # High pitch + high energy = excited/happy
        if pitch > 0.6 and energy > 0.6:
            emotion_scores['excited'] = 0.8
            emotion_scores['happy'] = 0.7
        # Low pitch + low energy = sad
        elif pitch < 0.4 and energy < 0.4:
            emotion_scores['sad'] = 0.7
            emotion_scores['calm'] = 0.5
        # High energy + fast speech = anxious/angry
        elif energy > 0.7 and speech_rate > 0.7:
            emotion_scores['anxious'] = 0.7
            emotion_scores['angry'] = 0.6
        # Balanced features = calm
        else:
            emotion_scores['calm'] = 0.6
        
        dominant_emotion = max(emotion_scores.items(), key=lambda x: x[1]) if emotion_scores else ('neutral', 0.5)
        
        return {
            'audio_features': {
                'pitch': pitch,
                'energy': energy,
                'speech_rate': speech_rate
            },
            'emotions': emotion_scores,
            'dominant_emotion': dominant_emotion[0],
            'confidence': dominant_emotion[1],
            'timestamp': datetime.now().isoformat()
        }


class PatternRecognizer:
    """Recognizes patterns in sensory preferences and behaviors."""
    
    def __init__(self):
        self.learned_patterns = []
        self.min_samples = 5
    
    def learn_preferences(self, sensory_data: List[Dict]) -> Dict:
        """
        Learn sensory preferences from historical data.
        
        Args:
            sensory_data: List of sensory analysis results
            
        Returns:
            Dict with learned preference patterns
        """
        if len(sensory_data) < self.min_samples:
            return {
                'status': 'insufficient_data',
                'samples': len(sensory_data),
                'required': self.min_samples
            }
        
        # Analyze preferences by modality
        preferences = {
            'visual': {'comfortable_range': None, 'triggers': []},
            'audio': {'comfortable_range': None, 'triggers': []},
            'tactile': {'comfortable_range': None, 'triggers': []}
        }
        
        for modality in ['visual', 'audio', 'tactile']:
            modality_data = [d for d in sensory_data if d.get('modality') == modality]
            
            if modality_data:
                # Find comfortable ranges (non-overwhelming)
                comfortable = [d for d in modality_data if not d.get('is_overwhelming')]
                
                if comfortable:
                    if modality == 'visual':
                        brightness_values = [d.get('brightness', 0) for d in comfortable]
                        preferences['visual']['comfortable_range'] = {
                            'brightness': {
                                'min': min(brightness_values),
                                'max': max(brightness_values),
                                'preferred': np.mean(brightness_values)
                            }
                        }
                    elif modality == 'audio':
                        volume_values = [d.get('volume', 0) for d in comfortable]
                        preferences['audio']['comfortable_range'] = {
                            'volume': {
                                'min': min(volume_values),
                                'max': max(volume_values),
                                'preferred': np.mean(volume_values)
                            }
                        }
                
                # Identify triggers (overwhelming instances)
                overwhelming = [d for d in modality_data if d.get('is_overwhelming')]
                if overwhelming:
                    preferences[modality]['triggers'] = [
                        {
                            'condition': 'high_intensity',
                            'frequency': len(overwhelming) / len(modality_data)
                        }
                    ]
        
        pattern = {
            'preferences': preferences,
            'total_samples': len(sensory_data),
            'learned_at': datetime.now().isoformat()
        }
        
        self.learned_patterns.append(pattern)
        return pattern
    
    def predict_comfort_level(self, sensory_input: Dict) -> Dict:
        """
        Predict comfort level for a sensory input based on learned patterns.
        
        Args:
            sensory_input: Current sensory input data
            
        Returns:
            Dict with comfort prediction
        """
        if not self.learned_patterns:
            return {
                'prediction': 'unknown',
                'confidence': 0.0,
                'reason': 'No learned patterns available'
            }
        
        latest_pattern = self.learned_patterns[-1]
        modality = sensory_input.get('modality')
        
        if modality not in latest_pattern['preferences']:
            return {
                'prediction': 'unknown',
                'confidence': 0.0,
                'reason': f'No pattern for modality: {modality}'
            }
        
        pref = latest_pattern['preferences'][modality]
        comfort_range = pref.get('comfortable_range')
        
        if not comfort_range:
            return {
                'prediction': 'uncertain',
                'confidence': 0.3
            }
        
        # Check if input is within comfortable range
        is_comfortable = True
        confidence = 0.8
        
        if modality == 'visual' and 'brightness' in comfort_range:
            input_brightness = sensory_input.get('brightness', 0)
            range_data = comfort_range['brightness']
            if input_brightness < range_data['min'] or input_brightness > range_data['max']:
                is_comfortable = False
        
        elif modality == 'audio' and 'volume' in comfort_range:
            input_volume = sensory_input.get('volume', 0)
            range_data = comfort_range['volume']
            if input_volume < range_data['min'] or input_volume > range_data['max']:
                is_comfortable = False
        
        return {
            'prediction': 'comfortable' if is_comfortable else 'uncomfortable',
            'confidence': confidence,
            'modality': modality,
            'timestamp': datetime.now().isoformat()
        }


class TriggerPredictor:
    """Predicts potential sensory triggers and meltdown risk."""
    
    def __init__(self):
        self.trigger_history = []
        self.risk_factors = {
            'time_of_day': 0.0,
            'environment_change': 0.0,
            'sensory_load': 0.0,
            'routine_disruption': 0.0
        }
    
    def assess_risk(self, context: Dict) -> Dict:
        """
        Assess risk of sensory overload or meltdown.
        
        Args:
            context: Current context including time, environment, etc.
            
        Returns:
            Dict with risk assessment
        """
        risk_score = 0.0
        contributing_factors = []
        
        # Time of day factor
        hour = context.get('hour', 12)
        if hour < 8 or hour > 20:  # Early morning or late evening
            risk_score += 0.2
            contributing_factors.append('Time of day (transition period)')
        
        # Environment change
        if context.get('environment_changed', False):
            risk_score += 0.3
            contributing_factors.append('Environment change detected')
        
        # Sensory load
        sensory_load = context.get('sensory_load', 0.0)
        if sensory_load > 0.7:
            risk_score += 0.3
            contributing_factors.append('High sensory load')
        
        # Routine disruption
        if context.get('routine_disrupted', False):
            risk_score += 0.2
            contributing_factors.append('Routine disruption')
        
        # Cap at 1.0
        risk_score = min(1.0, risk_score)
        
        # Determine risk level
        if risk_score < 0.3:
            risk_level = 'low'
        elif risk_score < 0.6:
            risk_level = 'moderate'
        else:
            risk_level = 'high'
        
        assessment = {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'contributing_factors': contributing_factors,
            'recommendations': self._get_risk_recommendations(risk_level),
            'timestamp': datetime.now().isoformat()
        }
        
        self.trigger_history.append(assessment)
        return assessment
    
    def _get_risk_recommendations(self, risk_level: str) -> List[str]:
        """Get recommendations based on risk level."""
        if risk_level == 'low':
            return ['Continue current activities', 'Monitor for changes']
        elif risk_level == 'moderate':
            return [
                'Reduce sensory stimulation',
                'Prepare calming activities',
                'Stay near safe/quiet space'
            ]
        else:  # high
            return [
                'Move to low-stimulation environment immediately',
                'Implement calming protocol',
                'Have caregiver provide support',
                'Avoid additional transitions or changes'
            ]
    
    def predict_trigger_likelihood(self, upcoming_activity: str, context: Dict) -> Dict:
        """
        Predict likelihood of triggers for an upcoming activity.
        
        Args:
            upcoming_activity: Description of planned activity
            context: Current context
            
        Returns:
            Dict with trigger prediction
        """
        # Simplified prediction model
        # In production, would use ML model trained on historical data
        
        high_risk_activities = ['crowd', 'loud', 'bright', 'unfamiliar', 'change']
        
        activity_lower = upcoming_activity.lower()
        trigger_keywords = [kw for kw in high_risk_activities if kw in activity_lower]
        
        base_risk = len(trigger_keywords) * 0.2
        context_risk = context.get('current_stress_level', 0.0) * 0.3
        
        likelihood = min(1.0, base_risk + context_risk)
        
        return {
            'activity': upcoming_activity,
            'trigger_likelihood': likelihood,
            'risk_level': 'high' if likelihood > 0.6 else 'moderate' if likelihood > 0.3 else 'low',
            'identified_triggers': trigger_keywords,
            'preparation_suggestions': self._get_preparation_tips(trigger_keywords),
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_preparation_tips(self, trigger_keywords: List[str]) -> List[str]:
        """Get preparation tips for identified triggers."""
        tips = []
        
        if 'crowd' in trigger_keywords or 'loud' in trigger_keywords:
            tips.append('Bring noise-canceling headphones')
            tips.append('Plan for quiet breaks')
        
        if 'bright' in trigger_keywords:
            tips.append('Bring sunglasses or cap')
            tips.append('Choose less bright areas')
        
        if 'unfamiliar' in trigger_keywords or 'change' in trigger_keywords:
            tips.append('Preview the location with photos/videos')
            tips.append('Discuss what to expect beforehand')
            tips.append('Bring comfort items')
        
        return tips if tips else ['Standard preparation recommended']
