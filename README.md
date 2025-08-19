# AI Dumbbell Curl Trainer

## 🔩💪 Rep-Based Dumbbell Curl Tracking with OpenCV & MediaPipe

- An AI personal trainer that uses your webcam to automatically count your dumbbell curl repetitions in real-time. This project leverages computer vision to provide immediate, on-screen feedback to help you track your workouts.

## ✔️ Features

- **Real-time Repetition Counting**: Automatically tracks and counts your dumbbell curls.
- **Visual Feedback**: Displays a percentage bar showing your form and a large, clear rep count.
- **Live Performance**: Provides real-time FPS (frames per second) to ensure smooth operation.
- **Camera Integration**: Uses your webcam for a live, interactive training session.

## 🧠 How It Works

The program utilizes computer vision to analyze your body's pose in real-time:

- **Pose Detection**: The `PoseModule` detects key landmarks on the body from the webcam feed, specifically focusing on the left arm (landmarks 11, 13, and 15).
- **Angle Calculation**: It calculates the angle of your elbow joint to determine the position of your arm during a curl.
- **Progress Tracking**: The angle is mapped to a percentage from 0 to 100, which controls the height of a progress bar on the screen.
- **Rep Counting Logic**: The code tracks the "direction" of the curl. It increments the rep count by 0.5 when your arm reaches full extension (0%) and again when it reaches full contraction (100%), effectively counting a full rep for each complete cycle.
- **On-Screen Display**: All visual elements, including the rep count, progress bar, and FPS, are drawn directly onto the video feed using OpenCV.

## 🔧 Requirements

To run this project, you need the following Python libraries:

- opencv-python
- numpy
- **PoseModule**: This is a custom module that contains the functions for pose detection and angle calculation.
