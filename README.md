# 🧠 AI-Autism Support Platform

> **Intelligent sensory and communication support system designed to empower autistic individuals through adaptive AI analysis, personalized interactions, and real-time caregiver insights.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)](https://fastapi.tiangolo.com/)

**Built for TataELxITE Hackathon** 🏆

---

## 🎯 Problem Statement

Autistic individuals often struggle with sensory processing, making daily interactions overwhelming and challenging. Current solutions lack personalization and real-time support. This platform bridges that gap by providing:

- **Real-time sensory state detection** using machine learning
- **Personalized calming recommendations** tailored to individual profiles
- **Caregiver insights dashboard** for better support coordination
- **Safe fallback mechanisms** ensuring reliability in all scenarios

---

## ✨ Key Features

✅ **AI-Powered Sensory Analysis** – RandomForest classifier detecting calm/overstimulated/under-stimulated states  
✅ **Dual-Layer Safety** – ML with rule-based fallback ensures reliability  
✅ **Real-Time Recommendations** – Instant personalized coping strategies  
✅ **Caregiver Dashboard** – Monitor and support from dedicated interface  
✅ **Scalable Architecture** – FastAPI backend + responsive frontend  
✅ **RESTful API** – Easy integration with other platforms  
✅ **Interactive Documentation** – Swagger UI for API exploration  

---

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────┐
│   Autistic User / Caregiver         │
│     (Web Browser)                   │
└────────────────┬────────────────────┘
                 │
        ┌────────▼────────┐
        │   Frontend      │
        │ (HTML/CSS/JS)   │
        └────────┬────────┘
                 │ HTTP
        ┌────────▼──────────────┐
        │   FastAPI Backend     │
        │  (Uvicorn Server)     │
        └────────┬──────────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
    ▼            ▼            ▼
┌────────────┐ ┌──────────┐ ┌─────────┐
│ Sensory    │ │ ML Model │ │ Rule-   │
│ Input      │ │ (RFC)    │ │ Based   │
│ Handler    │ │ Classifier
          │ │ Fallback │
└────────────┘ └──────────┘ └─────────┘
```

### The Sensory Analysis Pipeline

**1. Input Processing**
- Receive sensory parameters (noise, light, touch, movement)
- Normalize and scale features
- Validate input ranges

**2. ML Classification (Primary)**
- RandomForest trained on 330 samples
- 3-class output: Calm | Overstimulated | Under-stimulated
- Feature importance analysis
- Confidence scoring

**3. Rule-Based Fallback (Safety)**
- Automatic activation if ML fails
- Threshold-based decision trees
- Guaranteed system operation

**4. Recommendation Engine**
- Generate personalized coping strategies
- Return guidance for user & caregiver
- Track effectiveness metrics

### Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.8+, FastAPI, Uvicorn |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **ML/Data** | scikit-learn, pandas, NumPy |
| **Validation** | Pydantic |
| **Testing** | pytest, pytest-asyncio |
| **API Docs** | Swagger/OpenAPI |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Installation

```bash
# Clone the repository
git clone https://github.com/Sudeep5363/ai-autism-support-platform.git
cd ai-autism-support-platform

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

**Start Backend (API Server):**
```bash
cd backend
python -m uvicorn main:app --reload --port 5000
```

**Start Frontend (in another terminal):**
```bash
cd frontend
python -m http.server 8000
```

**Access the application:**
- **Frontend**: http://localhost:8000
- **API Docs**: http://localhost:5000/docs
- **ReDoc**: http://localhost:5000/redoc

### Testing

```bash
# Run model test
python test_working_model.py

# Run pytest suite
pytest
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/health` | Detailed status |
| POST | `/sensory/analyze` | Analyze sensory input & get recommendations |
| GET | `/docs` | Interactive Swagger documentation |
| GET | `/redoc` | ReDoc API documentation |

### Example Request

```bash
curl -X POST http://localhost:5000/sensory/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "noise_level": 75,
    "light_intensity": 800,
    "touch_sensitivity": 6,
    "movement_speed": 2
  }'
```

### Example Response

```json
{
  "sensory_state": "overstimulated",
  "confidence": 0.92,
  "recommendations": [
    "Move to a quieter environment",
    "Reduce bright lighting",
    "Try deep breathing exercises",
    "Use noise-cancelling headphones"
  ],
  "caregiver_alerts": [
    "User is overstimulated",
    "Recommend sensory break"
  ]
}
```

---

## 📁 Project Structure

```
ai-autism-support-platform/
├── README.md                    # Project overview
├── GETTING_STARTED.md           # Quick start guide
├── ARCHITECTURE.md              # Technical deep dive
├── DEPLOYMENT.md                # Production deployment
├── CHANGELOG.md                 # Version history
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
├── FILE_GUIDE.md                # Navigation guide
├── requirements.txt             # Python dependencies
├── test_working_model.py        # Model testing
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore patterns
│
├── backend/
│   ├── main.py                  # FastAPI application
│   ├── models.py                # Data models & Pydantic schemas
│   └── sensory_analyzer.py      # ML & rule-based analysis
│
├── frontend/
│   ├── index.html               # Web UI
│   ├── styles.css               # Styling
│   └── script.js                # Frontend logic
│
├── config/                      # Configuration files
└── docs/                        # Additional documentation
```

---

## 🤝 Use Cases

**For Autistic Individuals:**
- 🧩 Real-time sensory state detection
- 💡 Instant personalized coping recommendations
- 📊 Track sensory patterns over time
- 🎯 Navigate overwhelming environments with confidence

**For Caregivers:**
- 👁️ Monitor sensory state from dedicated dashboard
- 📈 Track effectiveness of strategies
- 🔔 Real-time alerts for intervention
- 📱 Mobile-friendly interface for on-the-go support

**For Researchers:**
- 🔬 Anonymized sensory data analysis
- 📊 Behavioral pattern research
- 🧬 ML model improvements
- 🎓 Academic publication support

---

## 🔧 Development

### Running Tests

```bash
# Test the ML model
python test_working_model.py

# Run full test suite
pytest -v

# With coverage
pytest --cov=backend
```

### Code Quality

```bash
# Type checking (if mypy installed)
mypy backend/

# Linting recommendations
# Consider adding flake8, black, isort for production
```

---

## 🚢 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment guides for:
- Heroku
- AWS
- DigitalOcean
- Google Cloud
- Docker & Kubernetes

---

## 📜 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) file.

---

## 🙏 Acknowledgments

- **TataELxITE Hackathon** for hosting and inspiration
- **Autism awareness organizations** for guidance
- **Open source community** – FastAPI, scikit-learn, pandas, NumPy
- **Contributors** – Your support makes this possible

---

## 💬 Support & Contact

For questions, suggestions, or collaboration:
- Email: your.email@example.com
- GitHub Issues: [Create an issue](https://github.com/Sudeep5363/ai-autism-support-platform/issues)
- Discussions: [Start a discussion](https://github.com/Sudeep5363/ai-autism-support-platform/discussions)

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [scikit-learn Guide](https://scikit-learn.org/)
- [Autism Spectrum Disorder Info](https://www.autism.org.uk/)
- [Web Accessibility Standards](https://www.w3.org/WAI/)

---

**Built with 💙 to support neurodiversity and empower autistic individuals**
