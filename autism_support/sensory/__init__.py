"""
Sensory Support System Module

Provides adaptive sensory support for individuals with autism including:
- Sensory input analysis (visual, audio, tactile)
- Adaptive environment control
- Sensory overload detection and alerts
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class SensoryInputAnalyzer:
    """Analyzes sensory inputs to detect patterns and potential triggers."""
    
    def __init__(self):
        self.visual_threshold = 0.7
        self.audio_threshold = 0.6
        self.tactile_threshold = 0.5
        self.history = []
    
    def analyze_visual(self, visual_data: np.ndarray) -> Dict:
        """
        Analyze visual stimuli for brightness, contrast, and motion.
        
        Args:
            visual_data: Image or video frame data
            
        Returns:
            Dict containing analysis results
        """
        try:
            brightness = np.mean(visual_data)
            contrast = np.std(visual_data)
            
            # Normalize values
            brightness_normalized = brightness / 255.0 if brightness > 1 else brightness
            contrast_normalized = min(contrast / 128.0, 1.0)
            
            is_overwhelming = (
                brightness_normalized > self.visual_threshold or 
                contrast_normalized > self.visual_threshold
            )
            
            result = {
                'brightness': float(brightness_normalized),
                'contrast': float(contrast_normalized),
                'is_overwhelming': is_overwhelming,
                'timestamp': datetime.now().isoformat(),
                'modality': 'visual'
            }
            
            self.history.append(result)
            return result
            
        except Exception as e:
            logger.error(f"Error analyzing visual data: {e}")
            return {'error': str(e)}
    
    def analyze_audio(self, audio_data: np.ndarray, sample_rate: int = 44100) -> Dict:
        """
        Analyze audio stimuli for volume, frequency, and patterns.
        
        Args:
            audio_data: Audio signal data
            sample_rate: Sample rate of audio
            
        Returns:
            Dict containing analysis results
        """
        try:
            # Calculate volume (RMS)
            rms = np.sqrt(np.mean(audio_data**2))
            volume_db = 20 * np.log10(rms + 1e-10)
            
            # Normalize to 0-1 range (assuming -60 to 0 dB range)
            volume_normalized = max(0, min(1, (volume_db + 60) / 60))
            
            is_overwhelming = volume_normalized > self.audio_threshold
            
            result = {
                'volume': float(volume_normalized),
                'volume_db': float(volume_db),
                'is_overwhelming': is_overwhelming,
                'timestamp': datetime.now().isoformat(),
                'modality': 'audio'
            }
            
            self.history.append(result)
            return result
            
        except Exception as e:
            logger.error(f"Error analyzing audio data: {e}")
            return {'error': str(e)}
    
    def analyze_tactile(self, pressure: float, temperature: float, texture: str = "smooth") -> Dict:
        """
        Analyze tactile stimuli.
        
        Args:
            pressure: Pressure level (0-1)
            temperature: Temperature (normalized 0-1)
            texture: Texture description
            
        Returns:
            Dict containing analysis results
        """
        try:
            combined_intensity = (pressure + temperature) / 2
            is_overwhelming = combined_intensity > self.tactile_threshold
            
            result = {
                'pressure': float(pressure),
                'temperature': float(temperature),
                'texture': texture,
                'intensity': float(combined_intensity),
                'is_overwhelming': is_overwhelming,
                'timestamp': datetime.now().isoformat(),
                'modality': 'tactile'
            }
            
            self.history.append(result)
            return result
            
        except Exception as e:
            logger.error(f"Error analyzing tactile data: {e}")
            return {'error': str(e)}
    
    def get_recent_history(self, limit: int = 10) -> List[Dict]:
        """Get recent sensory analysis history."""
        return self.history[-limit:] if self.history else []


class SensoryOverloadDetector:
    """Detects sensory overload conditions and generates alerts."""
    
    def __init__(self, threshold: float = 0.7):
        self.threshold = threshold
        self.overload_count = 0
        self.alert_history = []
    
    def detect_overload(self, sensory_analyses: List[Dict]) -> Dict:
        """
        Detect if sensory overload is occurring based on multiple inputs.
        
        Args:
            sensory_analyses: List of recent sensory analysis results
            
        Returns:
            Dict with overload detection results and recommendations
        """
        if not sensory_analyses:
            return {'overload_detected': False, 'severity': 0.0}
        
        # Count overwhelming stimuli
        overwhelming_count = sum(
            1 for analysis in sensory_analyses 
            if analysis.get('is_overwhelming', False)
        )
        
        severity = overwhelming_count / len(sensory_analyses)
        overload_detected = severity >= self.threshold
        
        if overload_detected:
            self.overload_count += 1
        
        result = {
            'overload_detected': overload_detected,
            'severity': float(severity),
            'overwhelming_count': overwhelming_count,
            'total_stimuli': len(sensory_analyses),
            'recommendations': self._generate_recommendations(severity, sensory_analyses),
            'timestamp': datetime.now().isoformat()
        }
        
        if overload_detected:
            self.alert_history.append(result)
        
        return result
    
    def _generate_recommendations(self, severity: float, analyses: List[Dict]) -> List[str]:
        """Generate personalized recommendations based on overload severity."""
        recommendations = []
        
        if severity < 0.3:
            return ["Environment is comfortable"]
        
        # Identify which modalities are overwhelming
        overwhelming_modalities = set()
        for analysis in analyses:
            if analysis.get('is_overwhelming'):
                overwhelming_modalities.add(analysis.get('modality', 'unknown'))
        
        if 'visual' in overwhelming_modalities:
            recommendations.append("Reduce lighting or screen brightness")
            recommendations.append("Consider using dimmer or blue-light filter")
        
        if 'audio' in overwhelming_modalities:
            recommendations.append("Reduce ambient noise")
            recommendations.append("Consider using noise-canceling headphones")
        
        if 'tactile' in overwhelming_modalities:
            recommendations.append("Adjust temperature or clothing comfort")
            recommendations.append("Reduce physical contact or pressure")
        
        if severity > 0.7:
            recommendations.insert(0, "ALERT: High sensory overload detected")
            recommendations.append("Move to a quiet, low-stimulation space")
            recommendations.append("Consider break or rest period")
        
        return recommendations
    
    def get_alert_history(self, limit: int = 5) -> List[Dict]:
        """Get recent overload alert history."""
        return self.alert_history[-limit:] if self.alert_history else []


class AdaptiveEnvironmentController:
    """Controls environmental parameters to optimize sensory comfort."""
    
    def __init__(self):
        self.current_settings = {
            'lighting': 0.5,  # 0-1 scale
            'volume': 0.5,
            'temperature': 0.5,
            'visual_complexity': 0.5
        }
        self.preferences = {}
        self.adjustment_history = []
    
    def set_user_preferences(self, preferences: Dict):
        """Set user-specific sensory preferences."""
        self.preferences = preferences
        logger.info(f"Updated user preferences: {preferences}")
    
    def adjust_environment(self, overload_detection: Dict) -> Dict:
        """
        Automatically adjust environment based on overload detection.
        
        Args:
            overload_detection: Results from SensoryOverloadDetector
            
        Returns:
            Dict with new environment settings
        """
        if not overload_detection.get('overload_detected'):
            return {
                'adjusted': False,
                'settings': self.current_settings.copy(),
                'message': 'No adjustment needed'
            }
        
        severity = overload_detection.get('severity', 0.0)
        
        # Adjust settings based on severity
        adjustment_factor = min(0.3, severity * 0.5)
        
        new_settings = self.current_settings.copy()
        new_settings['lighting'] = max(0.2, self.current_settings['lighting'] - adjustment_factor)
        new_settings['volume'] = max(0.1, self.current_settings['volume'] - adjustment_factor)
        new_settings['visual_complexity'] = max(0.2, self.current_settings['visual_complexity'] - adjustment_factor)
        
        # Apply user preferences if available
        if self.preferences:
            for key, value in self.preferences.items():
                if key in new_settings:
                    new_settings[key] = value
        
        adjustment = {
            'adjusted': True,
            'previous_settings': self.current_settings.copy(),
            'new_settings': new_settings,
            'severity': severity,
            'timestamp': datetime.now().isoformat()
        }
        
        self.current_settings = new_settings
        self.adjustment_history.append(adjustment)
        
        return adjustment
    
    def manual_adjustment(self, setting: str, value: float) -> Dict:
        """Manually adjust a specific environmental setting."""
        if setting not in self.current_settings:
            return {'error': f'Unknown setting: {setting}'}
        
        value = max(0.0, min(1.0, value))  # Clamp to 0-1
        old_value = self.current_settings[setting]
        self.current_settings[setting] = value
        
        return {
            'setting': setting,
            'old_value': old_value,
            'new_value': value,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_current_settings(self) -> Dict:
        """Get current environment settings."""
        return self.current_settings.copy()


class SensorySupportSystem:
    """
    Main sensory support system integrating all components.
    """
    
    def __init__(self, user_id: Optional[str] = None):
        self.user_id = user_id or "default_user"
        self.analyzer = SensoryInputAnalyzer()
        self.overload_detector = SensoryOverloadDetector()
        self.environment_controller = AdaptiveEnvironmentController()
        self.session_data = []
    
    def process_visual_input(self, visual_data: np.ndarray) -> Dict:
        """Process visual sensory input."""
        analysis = self.analyzer.analyze_visual(visual_data)
        self.session_data.append(analysis)
        return analysis
    
    def process_audio_input(self, audio_data: np.ndarray, sample_rate: int = 44100) -> Dict:
        """Process audio sensory input."""
        analysis = self.analyzer.analyze_audio(audio_data, sample_rate)
        self.session_data.append(analysis)
        return analysis
    
    def process_tactile_input(self, pressure: float, temperature: float, texture: str = "smooth") -> Dict:
        """Process tactile sensory input."""
        analysis = self.analyzer.analyze_tactile(pressure, temperature, texture)
        self.session_data.append(analysis)
        return analysis
    
    def check_and_respond(self) -> Dict:
        """
        Check for sensory overload and automatically adjust environment.
        
        Returns:
            Dict with overload status and environment adjustments
        """
        recent_analyses = self.analyzer.get_recent_history(limit=10)
        overload_result = self.overload_detector.detect_overload(recent_analyses)
        
        adjustment = None
        if overload_result.get('overload_detected'):
            adjustment = self.environment_controller.adjust_environment(overload_result)
        
        return {
            'overload_status': overload_result,
            'environment_adjustment': adjustment,
            'current_settings': self.environment_controller.get_current_settings()
        }
    
    def set_preferences(self, preferences: Dict):
        """Set user-specific preferences."""
        self.environment_controller.set_user_preferences(preferences)
    
    def get_session_summary(self) -> Dict:
        """Get summary of current session."""
        return {
            'user_id': self.user_id,
            'total_inputs_processed': len(self.session_data),
            'overload_events': self.overload_detector.overload_count,
            'recent_alerts': self.overload_detector.get_alert_history(limit=3),
            'current_environment': self.environment_controller.get_current_settings()
        }
