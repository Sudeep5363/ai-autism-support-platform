# AI-Enabled Sensory & Communication Support Platform for Autism Care

## Overview

This platform provides an AI-driven system to assist individuals with autism by offering adaptive sensory support, communication assistance, and actionable insights for caregivers and therapists.

## Features

### 1. Adaptive Sensory Support
- **Sensory Input Analysis**: Analyzes visual, audio, and tactile stimuli
- **Overload Detection**: Identifies sensory overload conditions in real-time
- **Adaptive Environment Control**: Automatically adjusts environment settings to reduce sensory stress
- **Personalized Preferences**: Learns and adapts to individual sensory preferences

### 2. Communication Assistance
- **Language Simplification**: Converts complex language into clearer, easier-to-understand text
- **Emotion Detection**: Identifies emotional tone and intent in communication
- **Visual Communication Aids**: Picture Exchange Communication System (PECS) support
- **Speech Adapters**: Placeholders for speech-to-text and text-to-speech integration

### 3. Caregiver Insights
- **Behavior Tracking**: Log and analyze behavior patterns over time
- **Progress Monitoring**: Track developmental goals and milestones
- **Personalized Recommendations**: AI-generated intervention strategies
- **Dashboard Analytics**: Comprehensive insights for caregivers and therapists

### 4. AI/ML Models
- **Emotion Detection**: Analyze emotions from text and audio features
- **Pattern Recognition**: Learn sensory preferences from historical data
- **Trigger Prediction**: Predict potential sensory triggers and assess risk

## Installation

### Requirements
- Python 3.8 or higher
- pip package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/Sudeep5363/ai-autism-support-platform.git
cd ai-autism-support-platform

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Quick Start

```python
import numpy as np
from autism_support import SensorySupportSystem, CommunicationAssistant, CaregiverInsights

# 1. Sensory Support
sensory_system = SensorySupportSystem(user_id="user123")

# Process sensory inputs
visual_data = np.random.rand(100, 100) * 255
visual_result = sensory_system.process_visual_input(visual_data)

audio_data = np.random.randn(44100) * 0.5
audio_result = sensory_system.process_audio_input(audio_data)

# Check for overload and get recommendations
response = sensory_system.check_and_respond()
print(response['overload_status']['recommendations'])

# 2. Communication Assistance
comm_assistant = CommunicationAssistant(user_id="user123")

# Simplify complex text
result = comm_assistant.process_text_input("It's raining cats and dogs!")
print(result['simplified']['simplified'])

# Create visual communication board
board = comm_assistant.create_visual_board(['needs', 'feelings', 'actions'])

# Interpret symbols
interpretation = comm_assistant.interpret_visual_communication(['I', 'hungry', 'eat'])
print(interpretation['interpretation'])

# 3. Caregiver Insights
caregiver = CaregiverInsights(user_id="user123")

# Log behavior
caregiver.log_behavior_observation(
    category='sensory_response',
    description='Covered ears in loud environment',
    intensity=0.8
)

# Add developmental goal
goal = caregiver.add_developmental_goal(
    goal_name="Improve verbal communication",
    category="communication",
    target_date="2026-12-31"
)

# Get insights and recommendations
insights = caregiver.get_comprehensive_insights(days=7)
print(insights['recommendations'])
```

## Usage Examples

See the `examples/` directory for complete usage examples:

- `basic_usage.py`: Demonstrates all core features of the platform

Run the example:
```bash
python examples/basic_usage.py
```

## Architecture

### Core Modules

```
autism_support/
├── sensory/              # Sensory support system
│   ├── SensoryInputAnalyzer
│   ├── SensoryOverloadDetector
│   ├── AdaptiveEnvironmentController
│   └── SensorySupportSystem
├── communication/        # Communication assistance
│   ├── LanguageSimplifier
│   ├── VisualCommunicationAid
│   ├── SpeechAdapter
│   └── CommunicationAssistant
├── caregiver/           # Caregiver insights
│   ├── BehaviorTracker
│   ├── ProgressMonitor
│   ├── RecommendationEngine
│   └── CaregiverInsights
├── ai_models/           # AI/ML models
│   ├── EmotionDetector
│   ├── PatternRecognizer
│   └── TriggerPredictor
├── utils/               # Utility functions
└── config/              # Configuration management
```

## API Reference

### Sensory Support System

#### SensorySupportSystem
Main class for sensory support functionality.

**Methods:**
- `process_visual_input(visual_data)`: Analyze visual stimuli
- `process_audio_input(audio_data, sample_rate)`: Analyze audio stimuli
- `process_tactile_input(pressure, temperature, texture)`: Analyze tactile stimuli
- `check_and_respond()`: Check for overload and adjust environment
- `set_preferences(preferences)`: Set user preferences
- `get_session_summary()`: Get session statistics

### Communication Assistant

#### CommunicationAssistant
Main class for communication assistance.

**Methods:**
- `process_text_input(text)`: Simplify and analyze text
- `create_visual_board(categories)`: Create visual communication board
- `interpret_visual_communication(symbols)`: Interpret symbol sequences
- `convert_speech(audio_data)`: Convert speech to text (placeholder)
- `speak_text(text, voice_settings)`: Convert text to speech (placeholder)
- `get_conversation_summary()`: Get conversation history

### Caregiver Insights

#### CaregiverInsights
Main class for caregiver insights and analytics.

**Methods:**
- `log_behavior_observation(category, description, intensity, context)`: Log behavior
- `add_developmental_goal(goal_name, category, target_date, description)`: Add goal
- `update_goal_progress(goal_id, progress, notes)`: Update goal progress
- `add_milestone(milestone_name, achieved, description)`: Add milestone
- `get_comprehensive_insights(days)`: Get complete insights package
- `get_dashboard_data()`: Get formatted dashboard data

## Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/test_sensory.py

# Run with coverage
python -m pytest tests/ --cov=autism_support
```

## Configuration

The platform can be configured through the `Config` class:

```python
from autism_support.config import config

# Get configuration value
threshold = config.get('sensory.visual_threshold')

# Set configuration value
config.set('sensory.visual_threshold', 0.8)

# Update multiple settings
config.update({
    'sensory': {
        'visual_threshold': 0.75,
        'audio_threshold': 0.65
    }
})
```

## Data Privacy & Security

- All data is processed locally by default
- No personal data is transmitted without explicit consent
- Configurable data retention policies
- Compliance with healthcare data privacy standards (HIPAA-ready architecture)

## Roadmap

### Current Features (v0.1.0)
- ✅ Sensory input analysis
- ✅ Overload detection and alerts
- ✅ Adaptive environment control
- ✅ Language simplification
- ✅ Visual communication aids
- ✅ Behavior tracking
- ✅ Progress monitoring
- ✅ Recommendation engine

### Planned Features
- 🔄 Real-time speech-to-text integration
- 🔄 Text-to-speech with voice customization
- 🔄 Mobile app interface
- 🔄 Wearable device integration
- 🔄 Multi-user support with family accounts
- 🔄 Therapist collaboration tools
- 🔄 Advanced ML models for pattern recognition
- 🔄 Cloud synchronization (optional)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Run tests
python -m pytest tests/
```

## License

MIT License - See LICENSE file for details

## Support

For questions, issues, or feature requests, please open an issue on GitHub.

## Acknowledgments

This project is designed to support individuals with autism and their caregivers. We acknowledge the autism community and the many researchers, therapists, and families who have contributed to our understanding of autism and effective support strategies.

## Disclaimer

This platform is designed as an assistive tool and should not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers regarding autism care and treatment decisions.
