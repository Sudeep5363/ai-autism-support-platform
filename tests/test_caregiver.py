"""
Unit tests for the Caregiver Insights module
"""

import unittest
from datetime import datetime, timedelta
from autism_support.caregiver import (
    BehaviorTracker,
    ProgressMonitor,
    RecommendationEngine,
    CaregiverInsights
)


class TestBehaviorTracker(unittest.TestCase):
    """Test cases for BehaviorTracker."""
    
    def setUp(self):
        self.tracker = BehaviorTracker()
    
    def test_log_behavior(self):
        """Test logging behavior observation."""
        result = self.tracker.log_behavior(
            category='sensory_response',
            description='Test behavior',
            intensity=0.5
        )
        
        self.assertEqual(result['category'], 'sensory_response')
        self.assertEqual(result['intensity'], 0.5)
        self.assertEqual(len(self.tracker.behavior_log), 1)
    
    def test_intensity_clamping(self):
        """Test that intensity is clamped to 0-1."""
        result = self.tracker.log_behavior(
            category='communication',
            description='Test',
            intensity=1.5
        )
        
        self.assertEqual(result['intensity'], 1.0)
    
    def test_analyze_patterns(self):
        """Test pattern analysis."""
        # Log multiple behaviors
        for i in range(5):
            self.tracker.log_behavior(
                category='sensory_response',
                description=f'Behavior {i}',
                intensity=0.8
            )
        
        analysis = self.tracker.analyze_patterns(days=7)
        
        self.assertEqual(analysis['total_observations'], 5)
        self.assertGreater(analysis['average_intensity'], 0.7)
    
    def test_get_recent_behaviors(self):
        """Test getting recent behaviors."""
        for i in range(15):
            self.tracker.log_behavior(
                category='communication',
                description=f'Behavior {i}',
                intensity=0.3
            )
        
        recent = self.tracker.get_recent_behaviors(limit=5)
        self.assertEqual(len(recent), 5)


class TestProgressMonitor(unittest.TestCase):
    """Test cases for ProgressMonitor."""
    
    def setUp(self):
        self.monitor = ProgressMonitor()
    
    def test_add_goal(self):
        """Test adding a goal."""
        goal = self.monitor.add_goal(
            goal_name="Test Goal",
            category="communication",
            target_date="2026-12-31"
        )
        
        self.assertEqual(goal['name'], "Test Goal")
        self.assertEqual(goal['status'], 'active')
        self.assertEqual(goal['progress'], 0.0)
    
    def test_update_progress(self):
        """Test updating goal progress."""
        goal = self.monitor.add_goal(
            goal_name="Test Goal",
            category="communication",
            target_date="2026-12-31"
        )
        
        updated = self.monitor.update_progress(goal['id'], 0.5)
        self.assertEqual(updated['progress'], 0.5)
    
    def test_complete_goal(self):
        """Test completing a goal."""
        goal = self.monitor.add_goal(
            goal_name="Test Goal",
            category="communication",
            target_date="2026-12-31"
        )
        
        updated = self.monitor.update_progress(goal['id'], 1.0)
        self.assertEqual(updated['status'], 'completed')
        self.assertIn('completed_at', updated)
    
    def test_add_milestone(self):
        """Test adding a milestone."""
        milestone = self.monitor.add_milestone(
            milestone_name="First word",
            achieved=True
        )
        
        self.assertEqual(milestone['name'], "First word")
        self.assertTrue(milestone['achieved'])
    
    def test_progress_summary(self):
        """Test getting progress summary."""
        self.monitor.add_goal("Goal 1", "communication", "2026-12-31")
        self.monitor.add_goal("Goal 2", "social", "2026-12-31")
        self.monitor.add_milestone("Milestone 1", achieved=True)
        
        summary = self.monitor.get_progress_summary()
        
        self.assertEqual(summary['total_goals'], 2)
        self.assertEqual(summary['active_goals'], 2)
        self.assertEqual(summary['achieved_milestones'], 1)


class TestRecommendationEngine(unittest.TestCase):
    """Test cases for RecommendationEngine."""
    
    def setUp(self):
        self.engine = RecommendationEngine()
    
    def test_generate_recommendations(self):
        """Test generating recommendations."""
        behavior_analysis = {
            'patterns': [
                {
                    'category': 'sensory_overload',
                    'observation': 'High intensity',
                    'average_intensity': 0.8
                }
            ]
        }
        progress_summary = {'average_progress': 0.5}
        
        recommendations = self.engine.generate_recommendations(
            behavior_analysis,
            progress_summary
        )
        
        self.assertTrue(len(recommendations) > 0)
        self.assertEqual(recommendations[0]['category'], 'sensory_overload')
    
    def test_get_strategy_library(self):
        """Test getting strategy library."""
        strategies = self.engine.get_strategy_library('communication_challenges')
        
        self.assertIn('communication_challenges', strategies)
        self.assertTrue(len(strategies['communication_challenges']) > 0)


class TestCaregiverInsights(unittest.TestCase):
    """Test cases for CaregiverInsights integration."""
    
    def setUp(self):
        self.insights = CaregiverInsights(user_id="test_user")
    
    def test_log_behavior(self):
        """Test logging behavior."""
        result = self.insights.log_behavior_observation(
            category='communication',
            description='Used words',
            intensity=0.5
        )
        
        self.assertEqual(result['category'], 'communication')
    
    def test_add_goal(self):
        """Test adding goal."""
        goal = self.insights.add_developmental_goal(
            goal_name="Communication goal",
            category="communication",
            target_date="2026-12-31"
        )
        
        self.assertEqual(goal['name'], "Communication goal")
    
    def test_comprehensive_insights(self):
        """Test getting comprehensive insights."""
        # Add some data
        self.insights.log_behavior_observation(
            'sensory_response',
            'Test',
            0.7
        )
        self.insights.add_developmental_goal(
            "Test Goal",
            "communication",
            "2026-12-31"
        )
        
        insights = self.insights.get_comprehensive_insights(days=7)
        
        self.assertIn('behavior_analysis', insights)
        self.assertIn('progress_summary', insights)
        self.assertIn('recommendations', insights)
    
    def test_dashboard_data(self):
        """Test getting dashboard data."""
        dashboard = self.insights.get_dashboard_data()
        
        self.assertIn('summary', dashboard)
        self.assertIn('behavior_trends', dashboard)
        self.assertIn('goal_progress', dashboard)


if __name__ == '__main__':
    unittest.main()
