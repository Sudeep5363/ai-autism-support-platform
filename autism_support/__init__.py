"""
AI-Enabled Sensory & Communication Support Platform for Autism Care

This package provides AI-driven assistance for individuals with autism through:
- Adaptive sensory support
- Communication assistance
- Caregiver insights and analytics
"""

__version__ = "0.1.0"
__author__ = "AI Autism Support Team"

from .sensory import SensorySupportSystem
from .communication import CommunicationAssistant
from .caregiver import CaregiverInsights

__all__ = [
    "SensorySupportSystem",
    "CommunicationAssistant", 
    "CaregiverInsights",
]
