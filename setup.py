from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-autism-support-platform",
    version="0.1.0",
    author="AI Autism Support Team",
    description="AI-driven system to assist individuals with autism",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "transformers>=4.20.0",
        "torch>=1.10.0",
        "nltk>=3.6.0",
        "spacy>=3.2.0",
        "librosa>=0.9.0",
        "soundfile>=0.10.0",
        "opencv-python>=4.5.0",
        "pillow>=9.0.0",
        "flask>=2.0.0",
        "flask-cors>=3.0.10",
        "sqlalchemy>=1.4.0",
        "python-dateutil>=2.8.0",
        "pyyaml>=6.0",
    ],
)
