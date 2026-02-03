# ai-autism-support-platform
An AI-powered sensory and communication support platform designed to assist autistic individuals through adaptive stimuli analysis, personalized interaction, and caregiver insights.

## Features

### Sensory Analysis Engine
- **Primary**: ML-based classifier (RandomForest on synthetic data)
  - Trained on 330 mock sensory samples
  - 3-class classification: calm, overstimulated, under-stimulated
  - StandardScaler for feature normalization
  - 100% training accuracy on synthetic dataset
- **Fallback**: Rule-based thresholds for reliability
  - Activates automatically if ML initialization fails
  - Ensures safe operation in all scenarios
- **Rationale**: Ensures safe operation even if ML fails, maintaining system reliability

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
pip install -r requirements.txt
```

### Running the Application

**Backend (API Server):**
```bash
cd backend
python -m uvicorn main:app --reload --port 5000
```

**Frontend (Web UI):**
```bash
cd frontend
python -m http.server 8000
```

### API Endpoints
- `GET /` - Health check
- `GET /health` - Detailed status
- `POST /sensory/analyze` - Analyze sensory input and get recommendations
- Interactive API docs: `http://127.0.0.1:5000/docs`

### Testing
```bash
python test_working_model.py
```
