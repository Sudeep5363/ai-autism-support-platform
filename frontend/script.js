// Frontend JavaScript
const API_URL = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', function() {
    console.log('AI Autism Support Platform initialized');
    
    // Initialize sliders
    initializeSliders();
    
    // Handle form submission
    const form = document.getElementById('sensoryForm');
    form.addEventListener('submit', handleAnalysis);
});

function initializeSliders() {
    const soundSlider = document.getElementById('soundLevel');
    const lightSlider = document.getElementById('lightLevel');
    const touchSlider = document.getElementById('touchLevel');
    
    soundSlider.addEventListener('input', (e) => {
        document.getElementById('soundValue').textContent = e.target.value;
    });
    
    lightSlider.addEventListener('input', (e) => {
        document.getElementById('lightValue').textContent = e.target.value;
    });
    
    touchSlider.addEventListener('input', (e) => {
        document.getElementById('touchValue').textContent = e.target.value;
    });
}

async function handleAnalysis(event) {
    event.preventDefault();
    
    // Hide previous results and errors
    const resultsDiv = document.getElementById('results');
    const errorDiv = document.getElementById('error');
    resultsDiv.classList.add('results-hidden');
    errorDiv.classList.add('error-hidden');
    
    // Get input values
    const soundLevel = parseInt(document.getElementById('soundLevel').value);
    const lightLevel = parseInt(document.getElementById('lightLevel').value);
    const touchLevel = parseInt(document.getElementById('touchLevel').value);
    
    // Prepare request data
    const requestData = {
        sound_level: soundLevel,
        light_level: lightLevel,
        touch_level: touchLevel,
        user_id: 'web_user_001'
    };
    
    try {
        // Show loading state
        const analyzeBtn = document.querySelector('.analyze-btn');
        const originalText = analyzeBtn.textContent;
        analyzeBtn.textContent = 'Analyzing...';
        analyzeBtn.disabled = true;
        
        // Call backend API
        const response = await fetch(`${API_URL}/sensory/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
        });
        
        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Display results
        displayResults(data);
        
        // Reset button
        analyzeBtn.textContent = originalText;
        analyzeBtn.disabled = false;
        
    } catch (error) {
        console.error('Error analyzing sensory input:', error);
        displayError(error.message);
        
        // Reset button
        const analyzeBtn = document.querySelector('.analyze-btn');
        analyzeBtn.textContent = 'Analyze Environment';
        analyzeBtn.disabled = false;
    }
}

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    const resultContent = document.getElementById('resultContent');
    
    // Determine state emoji and color
    let stateEmoji = '';
    let stateClass = '';
    
    switch(data.sensory_state) {
        case 'calm':
            stateEmoji = '✅';
            stateClass = 'state-calm';
            break;
        case 'overstimulated':
            stateEmoji = '⚠️';
            stateClass = 'state-overstimulated';
            break;
        case 'under-stimulated':
            stateEmoji = '💤';
            stateClass = 'state-understimulated';
            break;
    }
    
    // Alert level badge
    const alertBadge = `<span class="alert-badge alert-${data.alert_level}">${data.alert_level.toUpperCase()}</span>`;
    
    resultContent.innerHTML = `
        <div class="result-state ${stateClass}">
            <span class="state-emoji">${stateEmoji}</span>
            <h3>${data.sensory_state.toUpperCase()}</h3>
        </div>
        
        <div class="result-score">
            <div class="score-label">Sensory Load Score</div>
            <div class="score-value">${data.sensory_score.toFixed(1)}/100</div>
            <div class="score-bar">
                <div class="score-fill" style="width: ${data.sensory_score}%"></div>
            </div>
        </div>
        
        <div class="result-alert">
            <strong>Alert Level:</strong> ${alertBadge}
        </div>
        
        <div class="result-recommendation">
            <strong>💡 Recommendation:</strong>
            <p>${data.recommendation}</p>
        </div>
        
        <div class="result-details">
            <strong>Individual Scores:</strong>
            <ul>
                <li>🔊 Sound: ${data.individual_scores.sound_level}</li>
                <li>💡 Light: ${data.individual_scores.light_level}</li>
                <li>✋ Touch: ${data.individual_scores.touch_level}</li>
            </ul>
        </div>
    `;
    
    resultsDiv.classList.remove('results-hidden');
}

function displayError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.innerHTML = `
        <div class="error-content">
            <span class="error-icon">❌</span>
            <strong>Connection Error</strong>
            <p>Unable to connect to the backend server. Please ensure:</p>
            <ul>
                <li>Backend server is running on port 5000</li>
                <li>CORS is enabled on the backend</li>
            </ul>
            <p class="error-details">Error: ${message}</p>
        </div>
    `;
    errorDiv.classList.remove('error-hidden');
}
