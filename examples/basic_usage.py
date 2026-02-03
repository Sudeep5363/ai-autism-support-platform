#!/usr/bin/env python3
"""
Example usage of the AI Autism Support Platform

This script demonstrates the core functionality of the platform.
"""

import numpy as np
from autism_support import SensorySupportSystem, CommunicationAssistant, CaregiverInsights
from autism_support.utils import setup_logging

def main():
    # Set up logging
    setup_logging('INFO')
    
    print("=" * 60)
    print("AI-Enabled Sensory & Communication Support Platform")
    print("Example Usage Demonstration")
    print("=" * 60)
    
    # 1. Sensory Support System Demo
    print("\n1. SENSORY SUPPORT SYSTEM")
    print("-" * 60)
    
    sensory_system = SensorySupportSystem(user_id="demo_user")
    
    # Simulate visual input (high brightness)
    print("\nProcessing visual input (bright environment)...")
    visual_data = np.random.rand(100, 100) * 255  # Bright image
    visual_result = sensory_system.process_visual_input(visual_data)
    print(f"  Brightness: {visual_result['brightness']:.2f}")
    print(f"  Overwhelming: {visual_result['is_overwhelming']}")
    
    # Simulate audio input
    print("\nProcessing audio input...")
    audio_data = np.random.randn(44100) * 0.5  # Moderate volume
    audio_result = sensory_system.process_audio_input(audio_data)
    print(f"  Volume: {audio_result['volume']:.2f}")
    print(f"  Overwhelming: {audio_result['is_overwhelming']}")
    
    # Check for overload and adjust environment
    print("\nChecking for sensory overload...")
    response = sensory_system.check_and_respond()
    overload = response['overload_status']
    print(f"  Overload detected: {overload['overload_detected']}")
    print(f"  Severity: {overload['severity']:.2f}")
    if overload['recommendations']:
        print(f"  Recommendations:")
        for rec in overload['recommendations'][:3]:
            print(f"    - {rec}")
    
    # Get session summary
    print("\nSession summary:")
    summary = sensory_system.get_session_summary()
    print(f"  Total inputs processed: {summary['total_inputs_processed']}")
    print(f"  Overload events: {summary['overload_events']}")
    
    # 2. Communication Assistant Demo
    print("\n\n2. COMMUNICATION ASSISTANT")
    print("-" * 60)
    
    comm_assistant = CommunicationAssistant(user_id="demo_user")
    
    # Process complex text
    print("\nSimplifying complex text...")
    complex_text = "It's raining cats and dogs outside, so break a leg at your presentation!"
    result = comm_assistant.process_text_input(complex_text)
    print(f"  Original: {result['input']}")
    print(f"  Simplified: {result['simplified']['simplified']}")
    if result['simplified']['explanations']:
        print(f"  Explanations: {', '.join(result['simplified']['explanations'])}")
    
    # Create visual communication board
    print("\nCreating visual communication board...")
    board = comm_assistant.create_visual_board(['needs', 'feelings', 'actions'])
    print(f"  Categories: {', '.join(board['categories'])}")
    print(f"  Total symbols: {board['total_symbols']}")
    
    # Interpret symbol sequence
    print("\nInterpreting symbol communication...")
    symbols = ['I', 'hungry', 'eat']
    interpretation = comm_assistant.interpret_visual_communication(symbols)
    print(f"  Symbols: {' → '.join(interpretation['symbols'])}")
    print(f"  Interpretation: {interpretation['interpretation']}")
    print(f"  Suggested next: {', '.join(interpretation['suggested_next'][:3])}")
    
    # 3. Caregiver Insights Demo
    print("\n\n3. CAREGIVER INSIGHTS")
    print("-" * 60)
    
    caregiver_insights = CaregiverInsights(user_id="demo_user")
    
    # Log some behaviors
    print("\nLogging behavior observations...")
    caregiver_insights.log_behavior_observation(
        category='sensory_response',
        description='Covered ears in noisy environment',
        intensity=0.8,
        context={'location': 'cafeteria'}
    )
    caregiver_insights.log_behavior_observation(
        category='communication',
        description='Used picture card to request snack',
        intensity=0.3,
        context={'location': 'home'}
    )
    print("  ✓ 2 behavior observations logged")
    
    # Add a goal
    print("\nAdding developmental goal...")
    goal = caregiver_insights.add_developmental_goal(
        goal_name="Improve verbal communication",
        category="communication",
        target_date="2026-06-01",
        description="Use 3-4 word sentences consistently"
    )
    print(f"  ✓ Goal created: {goal['name']}")
    
    # Update progress
    caregiver_insights.update_goal_progress(goal['id'], 0.4, "Making good progress")
    print(f"  ✓ Progress updated: 40%")
    
    # Add milestone
    milestone = caregiver_insights.add_milestone(
        milestone_name="First unprompted greeting",
        achieved=True,
        description="Said 'hi' to teacher without prompting"
    )
    print(f"  ✓ Milestone achieved: {milestone['name']}")
    
    # Get comprehensive insights
    print("\nGenerating comprehensive insights...")
    insights = caregiver_insights.get_comprehensive_insights(days=7)
    print(f"  Analysis period: {insights['analysis_period_days']} days")
    print(f"  Total observations: {insights['behavior_analysis']['total_observations']}")
    print(f"  Active goals: {insights['progress_summary']['active_goals']}")
    print(f"  Recommendations: {len(insights['recommendations'])}")
    
    if insights['recommendations']:
        print("\n  Top recommendation:")
        top_rec = insights['recommendations'][0]
        print(f"    Category: {top_rec['category']}")
        print(f"    Priority: {top_rec['priority']}")
        if top_rec.get('strategies'):
            print(f"    Strategies:")
            for strategy in top_rec['strategies'][:2]:
                print(f"      - {strategy}")
    
    # Get dashboard data
    print("\nDashboard summary:")
    dashboard = caregiver_insights.get_dashboard_data()
    print(f"  Total observations: {dashboard['summary']['total_observations']}")
    print(f"  Active goals: {dashboard['summary']['active_goals']}")
    print(f"  Completed goals: {dashboard['summary']['completed_goals']}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
