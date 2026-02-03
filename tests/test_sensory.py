"""
Unit tests for the Sensory Support System
"""

import unittest
import numpy as np
from autism_support.sensory import (
    SensoryInputAnalyzer,
    SensoryOverloadDetector,
    AdaptiveEnvironmentController,
    SensorySupportSystem
)


class TestSensoryInputAnalyzer(unittest.TestCase):
    """Test cases for SensoryInputAnalyzer."""
    
    def setUp(self):
        self.analyzer = SensoryInputAnalyzer()
    
    def test_analyze_visual_bright(self):
        """Test visual analysis with bright input."""
        bright_data = np.ones((100, 100)) * 200
        result = self.analyzer.analyze_visual(bright_data)
        
        self.assertIn('brightness', result)
        self.assertIn('contrast', result)
        self.assertIn('is_overwhelming', result)
        self.assertTrue(result['brightness'] > 0.7)
    
    def test_analyze_visual_dim(self):
        """Test visual analysis with dim input."""
        dim_data = np.ones((100, 100)) * 50
        result = self.analyzer.analyze_visual(dim_data)
        
        self.assertIn('brightness', result)
        self.assertFalse(result['is_overwhelming'])
    
    def test_analyze_audio(self):
        """Test audio analysis."""
        audio_data = np.random.randn(1000) * 0.3
        result = self.analyzer.analyze_audio(audio_data)
        
        self.assertIn('volume', result)
        self.assertIn('volume_db', result)
        self.assertIn('is_overwhelming', result)
        self.assertEqual(result['modality'], 'audio')
    
    def test_analyze_tactile(self):
        """Test tactile analysis."""
        result = self.analyzer.analyze_tactile(0.3, 0.4, "smooth")
        
        self.assertIn('pressure', result)
        self.assertIn('temperature', result)
        self.assertIn('intensity', result)
        self.assertEqual(result['modality'], 'tactile')
    
    def test_history_tracking(self):
        """Test that analysis history is tracked."""
        visual_data = np.random.rand(50, 50)
        self.analyzer.analyze_visual(visual_data)
        
        audio_data = np.random.randn(1000)
        self.analyzer.analyze_audio(audio_data)
        
        history = self.analyzer.get_recent_history()
        self.assertEqual(len(history), 2)


class TestSensoryOverloadDetector(unittest.TestCase):
    """Test cases for SensoryOverloadDetector."""
    
    def setUp(self):
        self.detector = SensoryOverloadDetector(threshold=0.7)
    
    def test_no_overload(self):
        """Test detection with no overload."""
        analyses = [
            {'is_overwhelming': False, 'modality': 'visual'},
            {'is_overwhelming': False, 'modality': 'audio'}
        ]
        result = self.detector.detect_overload(analyses)
        
        self.assertFalse(result['overload_detected'])
        self.assertEqual(result['severity'], 0.0)
    
    def test_overload_detected(self):
        """Test detection with overload."""
        analyses = [
            {'is_overwhelming': True, 'modality': 'visual'},
            {'is_overwhelming': True, 'modality': 'audio'}
        ]
        result = self.detector.detect_overload(analyses)
        
        self.assertTrue(result['overload_detected'])
        self.assertEqual(result['severity'], 1.0)
        self.assertIn('recommendations', result)
    
    def test_alert_history(self):
        """Test that alerts are tracked in history."""
        analyses = [{'is_overwhelming': True, 'modality': 'visual'}]
        self.detector.detect_overload(analyses)
        
        history = self.detector.get_alert_history()
        self.assertEqual(len(history), 1)


class TestAdaptiveEnvironmentController(unittest.TestCase):
    """Test cases for AdaptiveEnvironmentController."""
    
    def setUp(self):
        self.controller = AdaptiveEnvironmentController()
    
    def test_default_settings(self):
        """Test default environment settings."""
        settings = self.controller.get_current_settings()
        
        self.assertIn('lighting', settings)
        self.assertIn('volume', settings)
        self.assertEqual(settings['lighting'], 0.5)
    
    def test_adjust_on_overload(self):
        """Test environment adjustment on overload."""
        overload = {
            'overload_detected': True,
            'severity': 0.8
        }
        adjustment = self.controller.adjust_environment(overload)
        
        self.assertTrue(adjustment['adjusted'])
        self.assertLess(
            adjustment['new_settings']['lighting'],
            adjustment['previous_settings']['lighting']
        )
    
    def test_no_adjust_without_overload(self):
        """Test no adjustment without overload."""
        overload = {'overload_detected': False}
        adjustment = self.controller.adjust_environment(overload)
        
        self.assertFalse(adjustment['adjusted'])
    
    def test_manual_adjustment(self):
        """Test manual setting adjustment."""
        result = self.controller.manual_adjustment('lighting', 0.3)
        
        self.assertEqual(result['setting'], 'lighting')
        self.assertEqual(result['new_value'], 0.3)
        
        settings = self.controller.get_current_settings()
        self.assertEqual(settings['lighting'], 0.3)
    
    def test_user_preferences(self):
        """Test setting user preferences."""
        preferences = {'lighting': 0.4, 'volume': 0.3}
        self.controller.set_user_preferences(preferences)
        
        overload = {'overload_detected': True, 'severity': 0.5}
        adjustment = self.controller.adjust_environment(overload)
        
        self.assertEqual(adjustment['new_settings']['lighting'], 0.4)


class TestSensorySupportSystem(unittest.TestCase):
    """Test cases for SensorySupportSystem integration."""
    
    def setUp(self):
        self.system = SensorySupportSystem(user_id="test_user")
    
    def test_process_visual_input(self):
        """Test processing visual input."""
        visual_data = np.random.rand(50, 50)
        result = self.system.process_visual_input(visual_data)
        
        self.assertIn('brightness', result)
        self.assertEqual(len(self.system.session_data), 1)
    
    def test_check_and_respond(self):
        """Test check and respond functionality."""
        # Add some inputs
        visual_data = np.ones((50, 50)) * 255
        self.system.process_visual_input(visual_data)
        
        response = self.system.check_and_respond()
        
        self.assertIn('overload_status', response)
        self.assertIn('current_settings', response)
    
    def test_session_summary(self):
        """Test getting session summary."""
        visual_data = np.random.rand(50, 50)
        self.system.process_visual_input(visual_data)
        
        summary = self.system.get_session_summary()
        
        self.assertEqual(summary['user_id'], 'test_user')
        self.assertEqual(summary['total_inputs_processed'], 1)


if __name__ == '__main__':
    unittest.main()
