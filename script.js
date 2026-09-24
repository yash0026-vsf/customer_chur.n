document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const age = document.getElementById('age').value;
    const monthlyCharges = document.getElementById('monthly_charges').value;
    
    const submitBtn = document.getElementById('submit-btn');
    const resultContainer = document.getElementById('result-container');
    const resultText = document.getElementById('result-text');
    const errorContainer = document.getElementById('error-container');
    const errorText = document.getElementById('error-text');

    // Reset UI
    submitBtn.disabled = true;
    submitBtn.textContent = 'Predicting...';
    resultContainer.className = 'hidden';
    errorContainer.className = 'hidden';

    try {
        const response = await fetch('/api/index', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                age: parseFloat(age),
                monthly_charges: parseFloat(monthlyCharges)
            })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || 'Server error occurred');
        }

        const data = await response.json();
        
        // Show result
        resultText.textContent = data.message;
        
        if (data.prediction === 0) {
            resultContainer.className = 'stay';
            document.getElementById('result-icon').textContent = '✅';
        } else {
            resultContainer.className = 'churn';
            document.getElementById('result-icon').textContent = '⚠️';
        }
        
    } catch (error) {
        // Show error
        errorText.textContent = `Error: ${error.message}`;
        errorContainer.className = '';
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Predict Churn';
    }
});
