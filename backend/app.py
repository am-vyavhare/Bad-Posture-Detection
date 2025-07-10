from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import os
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_video(video_path):
    feedback = []
    slouch_count = 0
    good_posture_count = 0
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        logging.error("Failed to open video file.")
        return ["Error: Unsupported video format or corrupted file."]

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for basic analysis
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Example rule-based logic using OpenCV (simplified)
        height, width = gray_frame.shape
        center_x, center_y = width // 2, height // 2

        # Detect slouching based on pixel intensity (mock logic)
        slouching = gray_frame[center_y, center_x] < 100  # Example threshold

        if slouching:
            slouch_count += 1
        else:
            good_posture_count += 1

    cap.release()

    total_frames = slouch_count + good_posture_count
    if total_frames == 0:
        logging.warning("Video contains zero frames.")
        return ["Error: Video contains zero frames."]

    slouch_percentage = (slouch_count / total_frames) * 100
    good_posture_percentage = (good_posture_count / total_frames) * 100

    feedback.append(f"Slouching detected in {slouch_percentage:.2f}% of frames.")
    feedback.append(f"Good posture detected in {good_posture_percentage:.2f}% of frames.")

    return feedback

@app.route('/analyze', methods=['POST'])
def analyze_posture():
    if 'video' not in request.files:
        logging.error("No video file uploaded.")
        return jsonify({"error": "No video file uploaded"}), 400

    video = request.files['video']
    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)  # Ensure the 'temp' directory exists
    video_path = os.path.join(temp_dir, video.filename)
    video.save(video_path)

    feedback = analyze_video(video_path)
    os.remove(video_path)  # Clean up the temporary file

    return jsonify({"feedback": feedback})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
