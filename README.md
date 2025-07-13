# object_detection
Real-time object detection with YOLOv12 and MOSSE tracking using OpenCV. Combines deep learning detection and ultra-fast object tracking from live webcam video.
# 🧠 Real-Time Object Detection & Tracking using YOLOv12 + MOSSE

This project combines **YOLOv12** for real-time object detection with the ultra-fast **MOSSE** tracker from OpenCV to enable efficient object tracking from a live webcam feed.

## 🚀 Features
- Live object detection using Ultralytics YOLOv12
- Manual object selection for tracking via mouse click
- Lightweight and fast MOSSE tracker for real-time performance
- Live video stream with bounding boxes and tracking feedback

## 🛠️ Technologies Used
- Python
- OpenCV (`cv2`)
- Ultralytics YOLO (`ultralytics`)
- Tracker: `MOSSE` (Minimum Output Sum of Squared Error)

## 📦 Installation

```bash
pip install opencv-contrib-python
pip install ultralytics
🧪 How It Works
Loads a YOLOv12 .pt model (you can use custom or pre-trained models).

Opens webcam and performs object detection in real-time.

On mouse click, selects an object to be tracked.

Tracks the selected object using OpenCV's MOSSE tracker.

Displays annotated frames with bounding boxes and status messages.

🎮 Controls
Left Mouse Click → Select object to track

Press 'q' → Quit the live feed

📁 Model Info
Default: yolo12n.pt

Replaceable with any .pt YOLOv8/v5 model or your own custom model

🤝 Contributions
Open to contributions! You can enhance detection, try other tracking algorithms, or add features like saving the video, auto-tracking detected objects, etc.
