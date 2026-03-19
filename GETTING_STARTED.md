# Getting Started Guide - AI Autism Support Platform

## 🎯 Overview

This guide will help you understand, set up, and run the **AI Autism Support Platform** for the first time.

---

## 📋 Prerequisites

- **Python** 3.8 or higher
- **pip** (Python package manager)
- A modern web browser (Chrome, Firefox, Edge, Safari)
- Command line/terminal access

Check your versions:

```bash
python --version    # Should be 3.8.0 or higher
pip --version       # Should match your Python version
```

---

## 🚀 Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sudeep5363/ai-autism-support-platform.git
cd ai-autism-support-platform
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **FastAPI** – Web framework
- **Uvicorn** – ASGI server
- **scikit-learn** – ML models
- **pandas, NumPy** – Data processing
- **Pydantic** – Data validation
- **pytest** – Testing framework

### Step 4: Set Up Environment (Optional)

```bash
cp .env.example .env
```

Edit `.env` with your configuration if needed:
```env
BACKEND_PORT=5000
FRONTEND_PORT=8000
DEBUG=true
```

### Step 5: Start the Backend Server

Open a terminal and run:

```bash
cd backend
python -m uvicorn main:app --reload --port 5000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:5000
INFO:     Application startup complete
```

### Step 6: Start the Frontend Server

Open a **new terminal** and run:

```bash
cd frontend
python -m http.server 8000
```

You should see:
```
Serving HTTP on 0.0.0.0 port 8000...
```

### Step 7: Access the Application

Open your browser and navigate to:
- **Frontend**: http://localhost:8000
- **API Documentation**: http://localhost:5000/docs
- **Alternative API Docs**: http://localhost:5000/redoc

---

## 🎨 Using the Application

### For Autistic Users

1. **Navigate to the dashboard** – Select "User Mode"
2. **Input sensory parameters**:
   - Noise level (0-100)
   - Light intensity (0-1000)
   - Touch sensitivity (0-10)
   - Movement speed (0-10)
3. **Get recommendations** – Personalized coping strategies appear instantly
4. **Track patterns** – Review historical data to understand triggers

### For Caregivers

1. **Select Caregiver Mode** in the UI
2. **Monitor sensory states** – Real-time dashboard view
3. **Review recommendations** – See what the system recommended
4. **Track effectiveness** – See which strategies work best
5. **Set alerts** – Get notified of overstimulation events

---

## 🧪 Testing the System

### Quick Model Test

```bash
python test_working_model.py
```

Expected output:
```
Testing ML Model...
✓ Model loaded successfully
✓ Prediction: [overstimulated]
✓ Confidence: 0.92
```

### Run Full Test Suite

```bash
pytest -v
```

### Manual API Testing

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test sensory analysis
curl -X POST http://localhost:5000/sensory/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "noise_level": 85,
    "light_intensity": 900,
    "touch_sensitivity": 8,
    "movement_speed": 5
  }'
```

---

## 📚 Key Concepts

### Sensory States

The system classifies sensory states into three categories:

**🟢 Calm**
- All sensory inputs within comfortable range
- Can participate in activities
- System recommends: Continue current activity, maintain environment

**🟡 Overstimulated**
- Sensory inputs exceed tolerance threshold
- May cause distress or shutdown
- System recommends: Withdrawal, calming strategies, environmental adjustment

**🔵 Under-stimulated**
- Insufficient sensory input
- May cause anxiety or restlessness
- System recommends: Engaging activities, sensory input increase

### Confidence Scoring

The ML model returns a confidence score (0-1):
- **0.9-1.0** – High confidence, follow recommendations
- **0.7-0.9** – Moderate confidence, consider recommendations
- **0.5-0.7** – Low confidence, use caregiver judgment
- **<0.5** – Very low, fall back to rule-based system

---

## 🐛 Troubleshooting

### Backend Won't Start

```bash
# Check if port 5000 is in use
# Windows
netstat -ano | findstr :5000

# macOS/Linux
lsof -i :5000

# If in use, try different port:
python -m uvicorn main:app --reload --port 5001
```

### Frontend Won't Load

```bash
# Check if port 8000 is available
# Try different port:
python -m http.server 8001
```

### Dependencies Installation Fails

```bash
# Clear pip cache
pip cache purge

# Reinstall requirements
pip install --upgrade -r requirements.txt
```

### ML Model Not Loading

```bash
# Test model directly
python test_working_model.py

# Check if fallback rule-based system activates
# (Should see " Using rule-based fallback" message)
```

---

## 📂 Project Structure Quick Ref

```
backend/
├── main.py                # FastAPI app with endpoints
├── models.py              # Pydantic schemas
└── sensory_analyzer.py    # ML + rule-based logic

frontend/
├── index.html             # Web interface
├── script.js              # Frontend logic
└── styles.css             # Styling
```

---

## 🔧 Common Commands

| Command | Purpose |
|---------|---------|
| `python -m uvicorn main:app --reload --port 5000` | Start backend |
| `python -m http.server 8000` | Start frontend |
| `python test_working_model.py` | Test ML model |
| `pytest -v` | Run full test suite |
| `pip install -r requirements.txt` | Install dependencies |

---

## 📖 Next Steps

1. **Read** [README.md](README.md) – Understand the full project
2. **Explore** [ARCHITECTURE.md](ARCHITECTURE.md) – Learn the technical details
3. **Try** the API – Use http://localhost:5000/docs
4. **Run** tests – Validate everything works
5. **Review** [CONTRIBUTING.md](CONTRIBUTING.md) – Contribute improvements

---

## 🆘 Need Help?

- **GitHub Issues**: [Create an issue](https://github.com/Sudeep5363/ai-autism-support-platform/issues)
- **Documentation**: Check [ARCHITECTURE.md](ARCHITECTURE.md) for details
- **API Docs**: Visit http://localhost:5000/docs when server is running

---

**Happy coding! Let's build better support for the autistic community.** 💙
