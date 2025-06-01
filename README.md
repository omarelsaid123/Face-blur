📌 Overview
This project uses Python and OpenCV to detect and blur both frontal and side-profile faces in real time from a webcam feed. It's designed to enhance privacy by masking all detected face regions with a blur effect. Side-profile detection is handled for both left and right profiles, ensuring better coverage by flipping the grayscale image when needed.

🛠️ Built With:
🐍 Python 3
📷 OpenCV – for image processing and face detection
🔢 NumPy – for efficient array operations

🚀 Features:

🎥 Real-time video capture from webcam
👤 Frontal face detection and blurring
🧭 Side-profile face detection (left and right)
🔄 Frame flipping for detecting right-facing profiles
💨 Smooth blur effect applied to detected faces
🛑 Press q anytime to exit the video window

🧠 How It Works:

OpenCV captures a frame from your webcam
Converts the frame to grayscale for more efficient processing
Uses Haar Cascades to detect:
Frontal faces
Left-facing side profiles
Right-facing profiles by flipping the grayscale image
Applies a strong blur to each detected face region
Displays the updated frame in real time

📸 Demo Output:
Real-time webcam feed with blurred face regions:

🧍‍♂️ Frontal faces = blurred
👤 Side profiles = blurred
➕ Multiple faces can be blurred simultaneously

