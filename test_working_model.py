#!/usr/bin/env python3
"""
Test script for the AI Autism Support Platform

This demonstrates the working sensory analysis model
"""

import sys
import json
sys.path.insert(0, 'backend')

from models import SensoryInput
from sensory_analyzer import sensory_analyzer

print("=" * 70)
print("AI AUTISM SUPPORT PLATFORM - SENSORY ANALYZER TEST")
print("=" * 70)

# Test Case 1: Calm State
print("\n📊 TEST 1: CALM SENSORY STATE")
print("-" * 70)
sensory_input_1 = SensoryInput(
    sound_level=45,
    light_level=60,
    touch_level=35,
    user_id="user_001"
)
print("Input:", json.dumps(sensory_input_1.dict(), indent=2))

response_1 = sensory_analyzer.analyze(sensory_input_1)
print("\nOutput:")
print(f"  Sensory State: {response_1.sensory_state}")
print(f"  Sensory Score: {response_1.sensory_score}/100")
print(f"  Alert Level: {response_1.alert_level}")
print(f"  Recommendation: {response_1.recommendation}")

# Test Case 2: Overstimulated State
print("\n📊 TEST 2: OVERSTIMULATED STATE")
print("-" * 70)
sensory_input_2 = SensoryInput(
    sound_level=80,
    light_level=75,
    touch_level=70,
    user_id="user_002"
)
print("Input:", json.dumps(sensory_input_2.dict(), indent=2))

response_2 = sensory_analyzer.analyze(sensory_input_2)
print("\nOutput:")
print(f"  Sensory State: {response_2.sensory_state}")
print(f"  Sensory Score: {response_2.sensory_score}/100")
print(f"  Alert Level: {response_2.alert_level}")
print(f"  Recommendation: {response_2.recommendation}")

# Test Case 3: Under-stimulated State
print("\n📊 TEST 3: UNDER-STIMULATED STATE")
print("-" * 70)
sensory_input_3 = SensoryInput(
    sound_level=15,
    light_level=20,
    touch_level=10,
    user_id="user_003"
)
print("Input:", json.dumps(sensory_input_3.dict(), indent=2))

response_3 = sensory_analyzer.analyze(sensory_input_3)
print("\nOutput:")
print(f"  Sensory State: {response_3.sensory_state}")
print(f"  Sensory Score: {response_3.sensory_score}/100")
print(f"  Alert Level: {response_3.alert_level}")
print(f"  Recommendation: {response_3.recommendation}")

print("\n" + "=" * 70)
print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 70)
