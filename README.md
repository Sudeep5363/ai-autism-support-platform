# AI-Enabled Sensory & Communication Support Platform for Autism Care

An AI-powered platform designed to assist individuals with autism through adaptive sensory support, communication assistance, and actionable insights for caregivers and therapists.

## Features

- **Adaptive Sensory Support**: Real-time analysis of visual, audio, and tactile stimuli with automatic environment adjustments
- **Communication Assistance**: Language simplification, visual communication aids (PECS), and speech adapters
- **Caregiver Insights**: Behavior tracking, progress monitoring, and personalized recommendations
- **AI/ML Models**: Emotion detection, pattern recognition, and trigger prediction

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

# Run example
python examples/basic_usage.py
```

## Documentation

See [DOCUMENTATION.md](DOCUMENTATION.md) for complete documentation including:
- Installation guide
- API reference
- Usage examples
- Architecture overview
- Configuration options

## Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific tests
python -m pytest tests/test_sensory.py
```

## Project Structure

```
autism_support/
├── sensory/         # Sensory support system
├── communication/   # Communication assistance
├── caregiver/       # Caregiver insights & analytics
├── ai_models/       # AI/ML models
├── utils/           # Utility functions
└── config/          # Configuration management
```

## License

MIT License

## Disclaimer

This platform is an assistive tool and should not replace professional medical advice. Always consult with qualified healthcare providers regarding autism care.
