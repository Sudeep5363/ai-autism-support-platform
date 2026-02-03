"""
Configuration module for the Autism Support Platform

Centralized settings for the application, including API configuration,
model parameters, and environment-specific variables.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# API CONFIGURATION
# ============================================================================

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
API_RELOAD = os.getenv("API_RELOAD", "True").lower() == "true"

# ============================================================================
# SENSORY ANALYSIS SETTINGS
# ============================================================================

# Sensory state thresholds (to be calibrated based on real data)
SOUND_THRESHOLD_LOW = 30  # dB
SOUND_THRESHOLD_HIGH = 80  # dB

LIGHT_THRESHOLD_LOW = 100  # lux
LIGHT_THRESHOLD_HIGH = 500  # lux

TOUCH_SENSITIVITY_LOW = 0.2
TOUCH_SENSITIVITY_HIGH = 0.8

# ============================================================================
# COMMUNICATION SETTINGS
# ============================================================================

# Response types supported
RESPONSE_TYPES = ["text", "audio", "visual", "haptic"]

# Default language
DEFAULT_LANGUAGE = "en"

# ============================================================================
# MODEL SETTINGS
# ============================================================================

# TODO: Add ML model paths when implementing personalization engine
