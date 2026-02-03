#!/usr/bin/env python3
"""
Advanced Example: Using AI Models for Predictive Analytics

This example demonstrates the AI/ML capabilities for emotion detection,
pattern recognition, and trigger prediction.
"""

import numpy as np
from autism_support.ai_models import EmotionDetector, PatternRecognizer, TriggerPredictor


def main():
    print("=" * 60)
    print("AI Models - Advanced Example")
    print("=" * 60)
    
    # 1. Emotion Detection
    print("\n1. EMOTION DETECTION")
    print("-" * 60)
    
    emotion_detector = EmotionDetector()
    
    # Detect emotions from text
    texts = [
        "I am so happy and excited about this!",
        "I feel worried and anxious about tomorrow",
        "This is making me really frustrated"
    ]
    
    print("\nText emotion analysis:")
    for text in texts:
        result = emotion_detector.detect_from_text(text)
        print(f"\n  Text: '{text}'")
        print(f"  Dominant emotion: {result['dominant_emotion']}")
        print(f"  Confidence: {result['confidence']:.2f}")
    
    # Detect emotions from audio features
    print("\n\nAudio emotion analysis:")
    audio_scenarios = [
        {"pitch": 0.8, "energy": 0.8, "speech_rate": 0.6, "desc": "Excited speech"},
        {"pitch": 0.3, "energy": 0.3, "speech_rate": 0.4, "desc": "Calm/sad speech"},
        {"pitch": 0.6, "energy": 0.9, "speech_rate": 0.9, "desc": "Anxious speech"}
    ]
    
    for scenario in audio_scenarios:
        result = emotion_detector.detect_from_audio_features(
            scenario['pitch'], scenario['energy'], scenario['speech_rate']
        )
        print(f"\n  Scenario: {scenario['desc']}")
        print(f"  Detected emotion: {result['dominant_emotion']}")
        print(f"  Confidence: {result['confidence']:.2f}")
    
    # 2. Pattern Recognition
    print("\n\n2. PATTERN RECOGNITION")
    print("-" * 60)
    
    pattern_recognizer = PatternRecognizer()
    
    # Generate sample sensory data
    print("\nLearning sensory preferences from historical data...")
    sensory_history = []
    
    # Visual preferences (comfortable with medium brightness)
    for i in range(10):
        sensory_history.append({
            'modality': 'visual',
            'brightness': 0.4 + np.random.rand() * 0.2,
            'contrast': 0.3 + np.random.rand() * 0.1,
            'is_overwhelming': False
        })
    
    # Add some overwhelming instances
    for i in range(3):
        sensory_history.append({
            'modality': 'visual',
            'brightness': 0.8 + np.random.rand() * 0.2,
            'contrast': 0.7,
            'is_overwhelming': True
        })
    
    # Audio preferences
    for i in range(10):
        sensory_history.append({
            'modality': 'audio',
            'volume': 0.3 + np.random.rand() * 0.2,
            'is_overwhelming': False
        })
    
    # Learn patterns
    learned = pattern_recognizer.learn_preferences(sensory_history)
    print(f"  ✓ Learned from {learned['total_samples']} samples")
    
    visual_prefs = learned['preferences']['visual']['comfortable_range']
    if visual_prefs:
        print(f"\n  Visual comfort range:")
        print(f"    Brightness: {visual_prefs['brightness']['min']:.2f} - {visual_prefs['brightness']['max']:.2f}")
        print(f"    Preferred: {visual_prefs['brightness']['preferred']:.2f}")
    
    # Predict comfort for new inputs
    print("\n  Predicting comfort for new stimuli:")
    test_inputs = [
        {'modality': 'visual', 'brightness': 0.5, 'desc': 'Medium brightness'},
        {'modality': 'visual', 'brightness': 0.9, 'desc': 'Very bright'},
        {'modality': 'audio', 'volume': 0.4, 'desc': 'Moderate volume'}
    ]
    
    for test in test_inputs:
        prediction = pattern_recognizer.predict_comfort_level(test)
        print(f"    {test['desc']}: {prediction['prediction']} (confidence: {prediction.get('confidence', 0):.2f})")
    
    # 3. Trigger Prediction
    print("\n\n3. TRIGGER PREDICTION & RISK ASSESSMENT")
    print("-" * 60)
    
    trigger_predictor = TriggerPredictor()
    
    # Assess risk in different contexts
    print("\nRisk assessment for different contexts:")
    contexts = [
        {
            'hour': 14,
            'environment_changed': False,
            'sensory_load': 0.3,
            'routine_disrupted': False,
            'desc': 'Normal afternoon at home'
        },
        {
            'hour': 7,
            'environment_changed': True,
            'sensory_load': 0.6,
            'routine_disrupted': True,
            'desc': 'Morning transition to school'
        },
        {
            'hour': 22,
            'environment_changed': False,
            'sensory_load': 0.8,
            'routine_disrupted': False,
            'desc': 'Late evening, high stimulation'
        }
    ]
    
    for context in contexts:
        assessment = trigger_predictor.assess_risk(context)
        print(f"\n  Context: {context['desc']}")
        print(f"  Risk level: {assessment['risk_level'].upper()}")
        print(f"  Risk score: {assessment['risk_score']:.2f}")
        if assessment['contributing_factors']:
            print(f"  Factors: {', '.join(assessment['contributing_factors'])}")
        print(f"  Top recommendation: {assessment['recommendations'][0]}")
    
    # Predict triggers for upcoming activities
    print("\n\nPredicting triggers for upcoming activities:")
    activities = [
        ("Quiet reading at home", {'current_stress_level': 0.2}),
        ("Visit to a loud, crowded shopping mall", {'current_stress_level': 0.3}),
        ("Unfamiliar bright place with many people", {'current_stress_level': 0.5})
    ]
    
    for activity, context in activities:
        prediction = trigger_predictor.predict_trigger_likelihood(activity, context)
        print(f"\n  Activity: {activity}")
        print(f"  Trigger likelihood: {prediction['trigger_likelihood']:.2f}")
        print(f"  Risk level: {prediction['risk_level'].upper()}")
        if prediction['identified_triggers']:
            print(f"  Identified triggers: {', '.join(prediction['identified_triggers'])}")
        if prediction['preparation_suggestions']:
            print(f"  Preparation tip: {prediction['preparation_suggestions'][0]}")
    
    print("\n" + "=" * 60)
    print("AI Models demonstration completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
