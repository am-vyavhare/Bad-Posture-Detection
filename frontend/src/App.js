import React, { useState } from 'react';
import './App.css'; // Import the CSS file

function App() {
  const [videoFile, setVideoFile] = useState(null);
  const [feedback, setFeedback] = useState([]);
  const [error, setError] = useState('');
  const [darkMode, setDarkMode] = useState(false);

  const handleFileUpload = (event) => {
    setVideoFile(event.target.files[0]);
    setError('');
  };

  const handleSubmit = async () => {
    if (!videoFile) {
      setError('Please upload a video file first.');
      return;
    }

    const formData = new FormData();
    formData.append('video', videoFile);

    try {
      const response = await fetch('https://bad-posture-detection-1.onrender.com/analyze', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to analyze posture. Please try again.');
      }

      const data = await response.json();
      setFeedback(data.feedback);
    } catch (error) {
      setError(error.message);
    }
  };

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`app-container ${darkMode ? 'dark-mode' : 'light-mode'}`}>
      <header className="app-header">
        <h1 className="app-title">Bad Posture Detection App</h1>
        <button onClick={toggleDarkMode} className="mode-toggle-button">
          {darkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
        </button>
      </header>
      <p className="app-description">
        Upload a video of yourself working or sitting, and this app will analyze your posture to detect slouching or desk shifting. Get instant feedback to improve your posture!
      </p>
      <div className="upload-section">
        <input type="file" accept="video/*" onChange={handleFileUpload} className="file-input" />
        <button onClick={handleSubmit} className="submit-button">
          Submit
        </button>
      </div>
      {error && <p className="error-message">{error}</p>}
      <div className="feedback-section">
        <h2 className="feedback-title">Feedback:</h2>
        {feedback.length > 0 ? (
          <ul className="feedback-list">
            {feedback.map((item, index) => (
              <li key={index} className="feedback-item">
                {item}
              </li>
            ))}
          </ul>
        ) : (
          <p className="no-feedback">No feedback available.</p>
        )}
      </div>
    </div>
  );
}

export default App;
