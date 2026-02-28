# AI Face Mask & Safety Helmet Detection System
# 🦺 AI Face Mask & Safety Helmet Detection System

An AI-powered safety compliance monitoring system built using Python, OpenCV, and YOLOv8.

This project is designed to detect individuals in a video stream and serve as a foundation for integrating face mask and safety helmet detection models. It logs detection events and captures evidence images for monitoring purposes.

Ideal for:
- Industrial safety monitoring
- Construction site compliance
- Public safety enforcement
- AI & Computer Vision learning
- Engineering projects and hackathons

---

## 🚀 Features

- Real-time person detection
- Framework ready for mask/helmet detection integration
- Automatic image capture
- Timestamp-based logging
- Webcam or video input support
- Lightweight YOLOv8 model

---

## 🧠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- NumPy

---

## 📂 Project Structure

AI_Mask_Helmet_Detection_System/
│
├── main.py
├── detector.py
├── config.py
├── requirements.txt
├── logs/
├── captures/
└── README.md

---

## ⚙️ Installation

1. Install Python 3.10 or later.
2. Clone the repository:

   git clone <your-repository-link>

3. Navigate to the project directory:

   cd AI_Mask_Helmet_Detection_System

4. Install dependencies:

   pip install -r requirements.txt

5. Run the system:

   python main.py

The YOLOv8 model will automatically download during first execution.

---

## ⚠️ Important Notice

The default YOLOv8 COCO model does NOT include mask or helmet classes.

To enable real mask/helmet detection:
- Train a custom YOLO model on a mask/helmet dataset
- Replace the default model weights in `detector.py` with your trained model file

This repository provides a complete detection pipeline ready for integration.

---

## 📊 How It Works

1. Video stream is captured from webcam or file.
2. YOLOv8 detects persons in each frame.
3. Detection events are:
   - Logged with timestamps
   - Saved as image evidence in `/captures`

With a trained model, mask and helmet compliance detection can be implemented.

---

## 🖥 System Requirements

Minimum:
- Windows 11
- 8GB RAM
- Webcam or video input

Recommended:
- NVIDIA GPU for faster inference

---

## 🔒 Ethical & Legal Notice

This project is intended for educational and research purposes only.
Ensure compliance with privacy and workplace regulations before real-world deployment.

---

## 🚀 Future Improvements

- Mask compliance classification
- Helmet detection model integration
- Real-time dashboard
- Alert system (Email/Telegram)
- Safety violation analytics

---

## 👨‍💻 Author

Developed as an AI-based industrial safety monitoring project.

AI-based safety compliance monitoring system using YOLOv8 and OpenCV.

IMPORTANT:
Default YOLOv8 COCO model does NOT include mask or helmet classes.
For real implementation, use a custom-trained mask/helmet YOLO model.

## Features
- Real-time person detection (placeholder)
- Image capture and logging
- Webcam or video input support

## Setup

1. Install Python 3.10+
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python main.py

Replace model weights with trained mask/helmet model for accurate detection.
