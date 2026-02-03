// Frontend JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('AI Autism Support Platform initialized');
    
    // Initialize app
    initializeApp();
});

function initializeApp() {
    const content = document.getElementById('content');
    content.innerHTML = '<p>Loading application...</p>';
    
    // Fetch data from backend
    fetch('/api/status')
        .then(response => response.json())
        .then(data => {
            content.innerHTML = `<p>Status: ${data.status}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
            content.innerHTML = '<p>Ready to connect to backend</p>';
        });
}
