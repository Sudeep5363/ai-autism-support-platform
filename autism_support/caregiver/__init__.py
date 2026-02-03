"""
Caregiver Insights Module

Provides insights and analytics for caregivers and therapists including:
- Behavior pattern tracking and analysis
- Progress monitoring dashboard
- Personalized recommendations engine
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class BehaviorTracker:
    """Tracks and analyzes behavior patterns over time."""
    
    def __init__(self):
        self.behavior_log = []
        self.behavior_categories = [
            'sensory_response',
            'communication',
            'social_interaction',
            'emotional_regulation',
            'routine_adherence'
        ]
    
    def log_behavior(self, 
                     category: str,
                     description: str,
                     intensity: float,
                     context: Optional[Dict] = None) -> Dict:
        """
        Log a behavior observation.
        
        Args:
            category: Behavior category
            description: Description of the behavior
            intensity: Intensity level (0-1)
            context: Optional contextual information
            
        Returns:
            Dict with logged behavior entry
        """
        if category not in self.behavior_categories:
            logger.warning(f"Unknown behavior category: {category}")
        
        entry = {
            'id': len(self.behavior_log) + 1,
            'category': category,
            'description': description,
            'intensity': max(0.0, min(1.0, intensity)),
            'context': context or {},
            'timestamp': datetime.now().isoformat()
        }
        
        self.behavior_log.append(entry)
        return entry
    
    def analyze_patterns(self, 
                        category: Optional[str] = None,
                        days: int = 7) -> Dict:
        """
        Analyze behavior patterns over a time period.
        
        Args:
            category: Optional category to filter by
            days: Number of days to analyze
            
        Returns:
            Dict with pattern analysis
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Filter logs
        filtered_logs = [
            log for log in self.behavior_log
            if datetime.fromisoformat(log['timestamp']) > cutoff_date
        ]
        
        if category:
            filtered_logs = [log for log in filtered_logs if log['category'] == category]
        
        if not filtered_logs:
            return {
                'total_observations': 0,
                'average_intensity': 0.0,
                'patterns': []
            }
        
        # Calculate statistics
        intensities = [log['intensity'] for log in filtered_logs]
        avg_intensity = sum(intensities) / len(intensities)
        
        # Group by category
        category_counts = {}
        category_intensities = {}
        
        for log in filtered_logs:
            cat = log['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1
            
            if cat not in category_intensities:
                category_intensities[cat] = []
            category_intensities[cat].append(log['intensity'])
        
        # Identify patterns
        patterns = []
        for cat, count in category_counts.items():
            avg_cat_intensity = sum(category_intensities[cat]) / len(category_intensities[cat])
            
            if avg_cat_intensity > 0.7:
                patterns.append({
                    'category': cat,
                    'observation': 'High intensity behaviors observed',
                    'frequency': count,
                    'average_intensity': avg_cat_intensity
                })
            elif count > len(filtered_logs) * 0.3:
                patterns.append({
                    'category': cat,
                    'observation': 'Frequent occurrences',
                    'frequency': count,
                    'average_intensity': avg_cat_intensity
                })
        
        return {
            'total_observations': len(filtered_logs),
            'average_intensity': avg_intensity,
            'category_breakdown': category_counts,
            'patterns': patterns,
            'time_period_days': days
        }
    
    def get_recent_behaviors(self, limit: int = 10) -> List[Dict]:
        """Get most recent behavior observations."""
        return self.behavior_log[-limit:] if self.behavior_log else []


class ProgressMonitor:
    """Monitors progress towards goals and milestones."""
    
    def __init__(self):
        self.goals = []
        self.milestones = []
        self.progress_data = []
    
    def add_goal(self, 
                 goal_name: str,
                 category: str,
                 target_date: str,
                 description: str = "") -> Dict:
        """
        Add a new development goal.
        
        Args:
            goal_name: Name of the goal
            category: Goal category
            target_date: Target completion date (ISO format)
            description: Goal description
            
        Returns:
            Dict with goal information
        """
        goal = {
            'id': len(self.goals) + 1,
            'name': goal_name,
            'category': category,
            'target_date': target_date,
            'description': description,
            'status': 'active',
            'progress': 0.0,
            'created_at': datetime.now().isoformat()
        }
        
        self.goals.append(goal)
        return goal
    
    def update_progress(self, goal_id: int, progress: float, notes: str = "") -> Dict:
        """
        Update progress on a goal.
        
        Args:
            goal_id: Goal ID
            progress: Progress percentage (0-1)
            notes: Optional progress notes
            
        Returns:
            Dict with updated goal information
        """
        goal = None
        for g in self.goals:
            if g['id'] == goal_id:
                goal = g
                break
        
        if not goal:
            return {'error': f'Goal {goal_id} not found'}
        
        progress = max(0.0, min(1.0, progress))
        goal['progress'] = progress
        
        if progress >= 1.0:
            goal['status'] = 'completed'
            goal['completed_at'] = datetime.now().isoformat()
        
        progress_entry = {
            'goal_id': goal_id,
            'progress': progress,
            'notes': notes,
            'timestamp': datetime.now().isoformat()
        }
        
        self.progress_data.append(progress_entry)
        
        return goal
    
    def add_milestone(self, 
                     milestone_name: str,
                     achieved: bool = False,
                     description: str = "") -> Dict:
        """
        Add a developmental milestone.
        
        Args:
            milestone_name: Name of milestone
            achieved: Whether milestone is achieved
            description: Milestone description
            
        Returns:
            Dict with milestone information
        """
        milestone = {
            'id': len(self.milestones) + 1,
            'name': milestone_name,
            'achieved': achieved,
            'description': description,
            'achieved_date': datetime.now().isoformat() if achieved else None,
            'created_at': datetime.now().isoformat()
        }
        
        self.milestones.append(milestone)
        return milestone
    
    def get_progress_summary(self) -> Dict:
        """Get overall progress summary."""
        active_goals = [g for g in self.goals if g['status'] == 'active']
        completed_goals = [g for g in self.goals if g['status'] == 'completed']
        achieved_milestones = [m for m in self.milestones if m['achieved']]
        
        avg_progress = 0.0
        if active_goals:
            avg_progress = sum(g['progress'] for g in active_goals) / len(active_goals)
        
        return {
            'total_goals': len(self.goals),
            'active_goals': len(active_goals),
            'completed_goals': len(completed_goals),
            'average_progress': avg_progress,
            'total_milestones': len(self.milestones),
            'achieved_milestones': len(achieved_milestones),
            'recent_goals': active_goals[-3:] if active_goals else []
        }


class RecommendationEngine:
    """Generates personalized recommendations for caregivers."""
    
    def __init__(self):
        self.recommendations = []
        self.intervention_strategies = self._initialize_strategies()
    
    def _initialize_strategies(self) -> Dict:
        """Initialize intervention strategy database."""
        return {
            'sensory_overload': [
                'Create a calm-down corner with low stimulation',
                'Use noise-canceling headphones during high-noise activities',
                'Implement a visual schedule to reduce anxiety',
                'Provide sensory breaks every 30-45 minutes'
            ],
            'communication_challenges': [
                'Use visual aids and picture cards',
                'Practice turn-taking in conversations',
                'Use simple, direct language',
                'Allow extra processing time for responses'
            ],
            'social_interaction': [
                'Start with one-on-one interactions',
                'Use social stories to prepare for events',
                'Practice social scripts for common situations',
                'Join structured group activities with clear rules'
            ],
            'emotional_regulation': [
                'Teach and practice deep breathing exercises',
                'Use emotion charts to identify feelings',
                'Create a feelings journal',
                'Implement a reward system for using coping strategies'
            ],
            'routine_adherence': [
                'Use visual schedules and timers',
                'Provide advance warning for transitions',
                'Keep daily routines consistent',
                'Use positive reinforcement for flexibility'
            ]
        }
    
    def generate_recommendations(self, 
                                behavior_analysis: Dict,
                                progress_summary: Dict) -> List[Dict]:
        """
        Generate personalized recommendations based on data.
        
        Args:
            behavior_analysis: Results from behavior pattern analysis
            progress_summary: Progress monitoring summary
            
        Returns:
            List of recommendation dicts
        """
        recommendations = []
        
        # Analyze behavior patterns
        patterns = behavior_analysis.get('patterns', [])
        for pattern in patterns:
            category = pattern['category']
            
            if category in self.intervention_strategies:
                strategies = self.intervention_strategies[category]
                
                recommendation = {
                    'id': len(recommendations) + 1,
                    'category': category,
                    'priority': 'high' if pattern['average_intensity'] > 0.7 else 'medium',
                    'observation': pattern['observation'],
                    'strategies': strategies[:2],  # Top 2 strategies
                    'timestamp': datetime.now().isoformat()
                }
                
                recommendations.append(recommendation)
        
        # Check progress on goals
        avg_progress = progress_summary.get('average_progress', 0.0)
        if avg_progress < 0.3:
            recommendations.append({
                'id': len(recommendations) + 1,
                'category': 'goal_progress',
                'priority': 'medium',
                'observation': 'Goals may need adjustment or additional support',
                'strategies': [
                    'Break goals into smaller, achievable steps',
                    'Increase frequency of reinforcement',
                    'Review and adjust goals with therapist'
                ],
                'timestamp': datetime.now().isoformat()
            })
        
        self.recommendations = recommendations
        return recommendations
    
    def get_strategy_library(self, category: Optional[str] = None) -> Dict:
        """
        Get intervention strategies from the library.
        
        Args:
            category: Optional category to filter by
            
        Returns:
            Dict of strategies
        """
        if category and category in self.intervention_strategies:
            return {category: self.intervention_strategies[category]}
        return self.intervention_strategies


class CaregiverInsights:
    """
    Main caregiver insights system integrating all components.
    """
    
    def __init__(self, user_id: Optional[str] = None):
        self.user_id = user_id or "default_user"
        self.behavior_tracker = BehaviorTracker()
        self.progress_monitor = ProgressMonitor()
        self.recommendation_engine = RecommendationEngine()
    
    def log_behavior_observation(self,
                                 category: str,
                                 description: str,
                                 intensity: float,
                                 context: Optional[Dict] = None) -> Dict:
        """Log a behavior observation."""
        return self.behavior_tracker.log_behavior(category, description, intensity, context)
    
    def add_developmental_goal(self,
                              goal_name: str,
                              category: str,
                              target_date: str,
                              description: str = "") -> Dict:
        """Add a new developmental goal."""
        return self.progress_monitor.add_goal(goal_name, category, target_date, description)
    
    def update_goal_progress(self, goal_id: int, progress: float, notes: str = "") -> Dict:
        """Update progress on a goal."""
        return self.progress_monitor.update_progress(goal_id, progress, notes)
    
    def add_milestone(self, milestone_name: str, achieved: bool = False, description: str = "") -> Dict:
        """Add a developmental milestone."""
        return self.progress_monitor.add_milestone(milestone_name, achieved, description)
    
    def get_comprehensive_insights(self, days: int = 7) -> Dict:
        """
        Get comprehensive insights and recommendations.
        
        Args:
            days: Number of days to analyze
            
        Returns:
            Dict with complete insights package
        """
        # Gather data
        behavior_analysis = self.behavior_tracker.analyze_patterns(days=days)
        progress_summary = self.progress_monitor.get_progress_summary()
        recommendations = self.recommendation_engine.generate_recommendations(
            behavior_analysis,
            progress_summary
        )
        
        return {
            'user_id': self.user_id,
            'analysis_period_days': days,
            'behavior_analysis': behavior_analysis,
            'progress_summary': progress_summary,
            'recommendations': recommendations,
            'recent_behaviors': self.behavior_tracker.get_recent_behaviors(limit=5),
            'generated_at': datetime.now().isoformat()
        }
    
    def get_dashboard_data(self) -> Dict:
        """Get data formatted for caregiver dashboard."""
        insights = self.get_comprehensive_insights(days=7)
        
        return {
            'user_id': self.user_id,
            'summary': {
                'total_observations': insights['behavior_analysis']['total_observations'],
                'active_goals': insights['progress_summary']['active_goals'],
                'completed_goals': insights['progress_summary']['completed_goals'],
                'high_priority_recommendations': len([
                    r for r in insights['recommendations'] 
                    if r.get('priority') == 'high'
                ])
            },
            'behavior_trends': insights['behavior_analysis'],
            'goal_progress': insights['progress_summary'],
            'top_recommendations': sorted(
                insights['recommendations'],
                key=lambda x: 0 if x.get('priority') == 'high' else 1
            )[:3],
            'recent_activity': insights['recent_behaviors']
        }
