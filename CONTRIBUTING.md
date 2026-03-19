# Contributing to AI Autism Support Platform

Thank you for considering contributing to the **AI Autism Support Platform**! We welcome contributions that improve support for autistic individuals.

## Code of Conduct

- Be respectful and inclusive to all community members
- Focus on improving support for the neurodivergent community
- Provide constructive feedback
- Respect others' ideas and lived experiences

---

## How to Contribute

### 1. Report Issues

**Found a bug?** → [Create an issue](https://github.com/Sudeep5363/ai-autism-support-platform/issues)

Provide:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)
- Screenshots/logs if applicable

### 2. Suggest Features

**Have an idea?** → [Create a feature request](https://github.com/Sudeep5363/ai-autism-support-platform/issues)

Describe:
- What problem it solves
- Why it's important for autistic users
- How it should work
- Any implementation ideas

### 3. Submit Pull Requests

**Ready to code?**

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add tests for new features
   - Update docs if needed
   - Keep commits focused and atomic

4. **Run tests locally:**
   ```bash
   pytest -v
   python test_working_model.py
   ```

5. **Commit with clear messages:**
   ```bash
   git commit -m "feat: add temperature sensitivity input to sensory analysis"
   ```

6. **Push and Create PR:**
   ```bash
   git push origin feature/your-feature-name
   ```

   In the PR description:
   - Explain what changed and why
   - Reference related issues (#123)
   - Note any breaking changes

### 4. Improve Documentation

- Fix typos in README/docs
- Add usage examples
- Clarify confusing sections
- Document new features
- Translate to other languages

---

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/ai-autism-support-platform.git
cd ai-autism-support-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies (optional)
pip install pytest pytest-cov black flake8

# Run tests
pytest -v
```

---

## Coding Standards

### Backend (Python)

- **Style**: Follow PEP 8
- **Type hints**: Use for function signatures
- **Comments**: Explain *why*, not *what*
- **Docstrings**: Add to functions and classes
- **Testing**: Write tests for new code

Example:

```python
def analyze_sensory_state(
    noise_level: float,
    light_intensity: float,
    touch_sensitivity: float,
    movement_speed: float
) -> dict:
    """
    Analyze sensory input and return state classification.
    
    Args:
        noise_level: Ambient noise (0-100 dB)
        light_intensity: Light level (0-1000 lux)
        touch_sensitivity: Touch sensitivity (0-10 scale)
        movement_speed: Environmental motion (0-10 scale)
    
    Returns:
        Dictionary with sensory_state, confidence, recommendations
    """
    # Implementation here
    pass
```

### Frontend (JavaScript)

- **Style**: Use camelCase for variables/functions
- **Comments**: Explain non-obvious logic
- **Accessibility**: Support keyboard navigation, screen readers
- **Responsiveness**: Works on mobile and desktop

---

## Commit Message Format

```
<type>: <subject>

<body (optional)>
```

**Types:**
- `feat` – New feature
- `fix` – Bug fix
- `docs` – Documentation
- `refactor` – Code reorganization
- `test` – Test additions/updates
- `perf` – Performance improvement
- `a11y` – Accessibility improvement

**Examples:**
```
feat: add temperature input to sensory analysis
fix: correct recommendation for under-stimulated state
docs: improve API documentation examples
refactor: optimize feature scaling in analyzer
test: add tests for edge case inputs
a11y: improve color contrast in dashboard
```

---

## Areas for Contribution

### 🧠 ML & Analysis
- Improve model accuracy
- Add new sensory dimensions (temperature, taste, smell)
- Implement personalization learning
- Add temporal pattern analysis
- Improve confidence scoring

### 🎨 Frontend
- Enhance UI/UX
- Better mobile responsiveness
- Accessibility improvements (WCAG compliance)
- New visualization types
- Dark mode support

### 📚 Backend
- Add database support (for history)
- Implement user profiles/preferences
- Add authentication
- Create export features (CSV, PDF)
- Optimize performance

### 📖 Documentation
- Add usage examples
- Create video tutorials
- Translate documentation
- Add API guides
- Document edge cases

### 🧪 Testing
- Improve test coverage
- Add edge case tests
- Create integration tests
- Add performance tests

### ♿ Accessibility
- WCAG 2.1 AA compliance
- Keyboard navigation
- Screen reader support
- Color contrast
- Font sizing

---

## Testing Requirements

All PRs must include tests:

```bash
# Run existing tests
pytest -v

# Run with coverage
pytest --cov=backend tests/

# Test the model
python test_working_model.py
```

**Target**: Maintain >80% code coverage

---

## Pull Request Checklist

Before submitting a PR:

- [ ] Code follows project style guidelines
- [ ] Tests pass locally (`pytest -v`)
- [ ] New tests added for new functionality
- [ ] Documentation updated (if needed)
- [ ] Commit messages are clear
- [ ] No unnecessary dependencies added
- [ ] Changes don't break existing functionality
- [ ] Accessibility considerations addressed
- [ ] Responsive design tested (mobile/desktop)

---

## Review Process

1. **Automated Checks**
   - GitHub Actions runs tests
   - Code style validation

2. **Code Review**
   - Maintainers review for quality
   - Architecture feedback
   - Security checks

3. **Integration**
   - Approved PRs merged to main
   - New version tagged when appropriate

---

## Getting Help

- **Questions?** → [GitHub Discussions](https://github.com/Sudeep5363/ai-autism-support-platform/discussions)
- **Documentation** → See [GETTING_STARTED.md](GETTING_STARTED.md)
- **Architecture** → See [ARCHITECTURE.md](ARCHITECTURE.md)
- **Issues** → [GitHub Issues](https://github.com/Sudeep5363/ai-autism-support-platform/issues)

---

## Community Recognition

Contributors will be recognized in:
- [CONTRIBUTORS.md](CONTRIBUTORS.md) file
- GitHub contributors page
- Release notes

---

## Important Guidelines

### Regarding Autism
- **Lived Experience**: Autistic individuals' experiences are valid
- **Language**: Use identity-first language (autistic person not person with autism)
- **Inspiration Porn**: Avoid portraying autism as tragedy to overcome
- **Input**: Prioritize input from actual autistic users
- **Research**: Base recommendations on peer-reviewed research

---

## Resources for Learning

- [Python Best Practices](https://www.python.org/dev/peps/pep-0008/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Web Accessibility](https://www.w3.org/WAI/)
- [Autism Spectrum Disorder](https://www.autism.org.uk/)

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to better support for the autistic community!** 💙
