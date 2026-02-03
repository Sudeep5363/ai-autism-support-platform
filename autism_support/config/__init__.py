"""
Configuration Module

Configuration and settings for the autism support platform.
"""

from typing import Any, Dict, Optional
import os


class Config:
    """Configuration settings for the platform."""
    
    def __init__(self):
        self.settings = self._default_settings()
    
    def _default_settings(self) -> Dict:
        """Get default configuration settings."""
        return {
            'sensory': {
                'visual_threshold': 0.7,
                'audio_threshold': 0.6,
                'tactile_threshold': 0.5,
                'overload_detection_threshold': 0.7,
                'analysis_history_limit': 10
            },
            'communication': {
                'simplification_enabled': True,
                'visual_aids_enabled': True,
                'speech_rate': 'slow',
                'default_voice_settings': {
                    'rate': 'slow',
                    'pitch': 'medium',
                    'volume': 'normal'
                }
            },
            'caregiver': {
                'behavior_tracking_enabled': True,
                'progress_monitoring_enabled': True,
                'recommendation_generation_enabled': True,
                'default_analysis_days': 7
            },
            'ai_models': {
                'emotion_detection_enabled': True,
                'pattern_recognition_enabled': True,
                'trigger_prediction_enabled': True,
                'min_samples_for_learning': 5
            },
            'system': {
                'log_level': 'INFO',
                'data_retention_days': 90,
                'auto_save_enabled': True,
                'enable_notifications': True
            }
        }
    
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: Configuration key (use dot notation for nested keys)
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.
        
        Args:
            key: Configuration key (use dot notation for nested keys)
            value: Value to set
        """
        keys = key.split('.')
        target = self.settings
        
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        
        target[keys[-1]] = value
    
    def update(self, settings_dict: Dict) -> None:
        """
        Update multiple configuration settings.
        
        Args:
            settings_dict: Dictionary of settings to update
        """
        self._deep_update(self.settings, settings_dict)
    
    def _deep_update(self, base_dict: Dict, update_dict: Dict) -> None:
        """Recursively update nested dictionary."""
        for key, value in update_dict.items():
            if isinstance(value, dict) and key in base_dict and isinstance(base_dict[key], dict):
                self._deep_update(base_dict[key], value)
            else:
                base_dict[key] = value
    
    def get_all(self) -> Dict:
        """Get all configuration settings."""
        return self.settings.copy()


# Global configuration instance
config = Config()
