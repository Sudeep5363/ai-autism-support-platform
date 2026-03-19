# Deployment Guide - AI Autism Support Platform

## 🚀 Deploy to Production

This guide covers deploying the AI Autism Support Platform to various platforms.

---

## 📋 Pre-Deployment Checklist

- [ ] All tests pass: `pytest -v`
- [ ] No hardcoded secrets in code
- [ ] Environment variables documented
- [ ] Dependencies in requirements.txt
- [ ] README updated with deployment info
- [ ] Error handling comprehensive
- [ ] Performance tested
- [ ] Security review completed

---

## 🔧 Production Build

### Prepare for Deployment

```bash
# 1. Update requirements with specific versions
pip freeze > requirements.txt

# 2. Run all tests
pytest -v

# 3. Test the model in production mode
python test_working_model.py

# 4. Build production bundle
python -m PyInstaller --onefile backend/main.py  # Optional
```

---

## ☁️ Deployment Options

### Option 1: Heroku (Easiest for Python)

**Advantages**: Free tier (limited), git-based deployment, easy scaling

**Setup:**

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create your-app-name

# Generate Procfile
echo "web: python -m uvicorn backend.main:app --host 0.0.0.0 --port \$PORT" > Procfile

# Add runtime.txt
echo "python-3.11.5" > runtime.txt

# Deploy
git push heroku main

# Scale to single dyno
heroku ps:scale web=1
```

**Monitor:**
```bash
heroku logs --tail
heroku open
```

### Option 2: AWS (Scalable)

**Using Elastic Beanstalk:**

```bash
# Install EB CLI
pip install awsebcli-3

# Initialize
eb init -p python-3.11 my-app

# Create .ebextensions/python.config
mkdir -p .ebextensions
cat > .ebextensions/python.config << EOF
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: backend.main:app
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: /var/app/current
EOF

# Deploy
eb create production-env
eb deploy
```

### Option 3: DigitalOcean (Simple & Affordable)

**Using App Platform:**

1. Connect GitHub account at https://cloud.digitalocean.com/
2. Select repository
3. Configure:
   ```
   Build command: pip install -r requirements.txt
   Run command: python -m uvicorn backend.main:app --host 0.0.0.0 --port 8080
   ```
4. Deploy automatically on push

### Option 4: Google Cloud Run (Serverless)

**Using Cloud Run:**

```bash
# Create Dockerfile
cat > Dockerfile << EOF
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
EOF

# Deploy
gcloud run deploy autism-support \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Option 5: Docker (For Any Platform)

**Create Dockerfile:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend ./backend
COPY frontend ./frontend
COPY config ./config

# Expose ports
EXPOSE 5000 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:5000/health')"

# Run both services
CMD ["sh", "-c", "python -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 & python -m http.server 8000 -d frontend"]
```

**Build and run:**

```bash
docker build -t autism-support .
docker run -p 5000:5000 -p 8000:8000 autism-support
```

**Push to registry:**

```bash
docker tag autism-support your-registry/autism-support:latest
docker push your-registry/autism-support:latest
```

---

## 🔐 Environment Configuration

### Production .env File

```env
# Server
BACKEND_PORT=5000
FRONTEND_PORT=8000
DEBUG=false
ENVIRONMENT=production

# Security
SECRET_KEY=your-secret-key-here-min-32-chars
ALLOWED_HOSTS=localhost,yourdomain.com

# Database (if added)
DATABASE_URL=postgresql://user:pass@db-host:5432/dbname

# API Configuration
API_TIMEOUT=30
MAX_REQUESTS_PER_MINUTE=100

# Logging
LOG_LEVEL=INFO
LOG_FILE=/var/log/autism-support/app.log

# Features
ENABLE_CAREGIVER_MODE=true
ENABLE_ANALYTICS=false
```

**Never commit .env to Git! Use .env.example instead.**

---

## 📊 Monitoring & Logging

### Setup Logging

```python
# In backend/main.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
```

### Recommended Tools

| Tool | Purpose | Tier |
|------|---------|------|
| Sentry | Error tracking | Free |
| New Relic | Performance | Free (limited) |
| Datadog | Full monitoring | Paid |
| LogRocket | Frontend monitoring | Free (limited) |
| CloudWatch | AWS logging | Paid |

### Setup Sentry

```bash
pip install sentry-sdk

# In backend/main.py
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FastApiIntegration()],
    traces_sample_rate=1.0,
    environment="production"
)
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run tests
        run: |
          pytest -v
          python test_working_model.py
      
      - name: Deploy to Heroku
        env:
          HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
        run: |
          git remote add heroku https://git.heroku.com/your-app-name.git
          git push -f heroku main
```

---

## 🚨 Troubleshooting

| Problem | Solution |
|---------|----------|
| **Port already in use** | Use different port: `--port 8080` |
| **Import errors** | Verify requirements.txt, reinstall deps |
| **Model not loading** | Check file paths, verify model file exists |
| **Slow response** | Profile with `pip install scalene` |
| **Memory issues** | Check for memory leaks, restart service |
| **SSL certificate error** | Update certifi: `pip install --upgrade certifi` |

---

## 📈 Scaling Strategies

### Vertical Scaling
```bash
# Increase server resources (CPU, RAM)
# In most platforms: adjust instance type
```

### Horizontal Scaling
```bash
# Run multiple instances behind load balancer
# Add Nginx reverse proxy
# Use container orchestration (Kubernetes)
```

### Caching Layer
```bash
# Add Redis for response caching
pip install redis fastapi-cache2
```

### Database Optimization
```python
# Add connection pooling
# Index frequently queried fields
# Archive old data
```

---

## 📞 Support & Rollback

### Automatic Health Checks

```bash
# Most platforms support automatic restarts
# Configure health checks:
GET /health
Expected: 200 OK
Interval: 30 seconds
```

### Rollback Process

```bash
# If deployment fails
git revert HEAD
git push

# Or manually revert on platform dashboard
# (Most platforms have one-click rollback)
```

---

## 🎓 Resources

- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- [Docker Documentation](https://docs.docker.com/)
- [Google Cloud Run](https://cloud.google.com/run/docs)

---

**Your autism support platform is now live!** 🚀💙
