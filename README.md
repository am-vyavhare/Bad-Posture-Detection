# Bad Posture Detection App

## Overview
This is a full-stack web application that detects bad posture from uploaded videos or live webcam streams. The app uses rule-based logic to flag instances of bad posture such as slouching or desk shifting.

## Features
- Upload video files or use webcam for posture analysis.
- Detect bad posture using MediaPipe and OpenCV.
- Display frame-by-frame feedback on posture.

## Public Deployment Links
- Frontend: [Netlify Link](https://deluxe-kangaroo-89eb6e.netlify.app/)
- Backend: [Render Link](https://bad-posture-detection-1.onrender.com/)

## Demo Video
- [Demo Video Link](https://your-demo-video-link)

## Steps to Run Locally

### Prerequisites
1. Install Node.js for the frontend.
2. Install Python (preferably 3.8 or higher) for the backend.
3. Install `pip` for Python package management.

### Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```
4. The frontend will be accessible at `http://localhost:3000`.

### Backend Setup
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```
5. The backend will be accessible at `http://localhost:5000`.

### Connecting Frontend and Backend
1. Ensure both the frontend and backend servers are running.
2. The frontend will send video files to the backend for analysis via the `/analyze` endpoint.

## Deployment Instructions
1. **Frontend Deployment**:
   - Run `npm run build` in the `frontend` folder.
   - Deploy the `build` folder to Netlify.

2. **Backend Deployment**:
   - Deploy the Flask app on Render or any other platform.
   - Ensure the backend URL is updated in the frontend code.

## Folder Structure
```
bad posture detection/
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js
│   ├── public/
│   ├── package.json
├── README.md
```

## Notes
- Ensure the backend URL is correctly configured in the frontend code when deploying.
- Temporary files created during video analysis are automatically cleaned up.

## License
This project is for educational purposes only.