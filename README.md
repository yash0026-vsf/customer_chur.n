# Customer Churn Predictor

This project contains a web application for predicting customer churn using a Support Vector Classifier (SVC). It was converted from a Jupyter Notebook to a standalone web app structure suitable for deployment.

## Project Structure

- `backend/`
  - `train_model.py`: Script to train the SVC model and save it as `model.pkl`.
  - `app.py`: Flask application that loads the trained model and serves an API endpoint for predictions.
  - `requirements.txt`: Python dependencies required for the backend.
- `frontend/`
  - `index.html`: The user interface.
  - `style.css`: Styling for the interface.
  - `script.js`: Logic to send user input to the backend API.

## How to Run Locally

### 1. Set up the Backend
1. Open a terminal and navigate to the `backend` folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model (this will generate `model.pkl`):
   ```bash
   python train_model.py
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```
   The backend API will run at `http://127.0.0.1:5000`.

### 2. Run the Frontend
1. Open a new terminal and navigate to the `frontend` folder.
2. You can open `index.html` directly in your browser, or start a simple local server:
   ```bash
   python -m http.server 8000
   ```
3. If using `http.server`, navigate to `http://localhost:8000` in your web browser.

## Deployment Notes

- **Backend**: You can deploy the Flask app using platforms like Heroku, Render, or AWS. For production, consider using a production WSGI server like `gunicorn` instead of Flask's built-in server.
- **Frontend**: The static files (HTML, CSS, JS) can be deployed to static hosting services like Vercel, Netlify, or GitHub Pages. Just ensure that the API URL in `script.js` is updated to point to your live backend URL once deployed.
