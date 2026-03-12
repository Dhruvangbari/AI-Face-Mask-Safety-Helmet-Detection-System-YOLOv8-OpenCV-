# 🦺 AI Industrial Safety Compliance Monitoring System


An advanced AI-powered Industrial Safety Monitoring System built using Python, OpenCV, and YOLOv8.

This system detects:
- 👤 Persons
- 🪖 Safety Helmets
- 😷 Face Masks

It evaluates real-time safety compliance and automatically flags violations when required protective equipment is missing.

Designed for:
- Industrial safety monitoring
- Construction site compliance
- Smart factory automation
- AI & Computer Vision projects
- Final year engineering projects
- Hackathons & portfolio enhancement

---

## 🚀 Key Features

- ✅ Real-time person detection
- ✅ Helmet detection integration
- ✅ Mask detection integration
- ✅ Safety compliance logic (SAFE / VIOLATION)
- ✅ Automatic violation logging (CSV)
- ✅ Evidence image capture
- ✅ Modular and scalable architecture
- ✅ Ready for dashboard integration

---

## 🧠 System Architecture

1. Video stream captured from webcam or IP camera
2. YOLOv8 custom-trained model detects:
   - Person
   - Helmet
   - Mask
3. Bounding box overlap logic checks compliance
4. If violation detected:
   - Status displayed on screen
   - Event logged in CSV
   - Image stored as evidence

---

## 📂 Project Structure

AI_Industrial_Safety_System/
│
├── main.py
├── detector.py
├── config.py
├── utils.py
├── requirements.txt
└── logs/
    ├── violations.csv
    └── images/

---

## 🛠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- NumPy
- Pandas

---

## ⚙️ Installation

### 1️⃣ Install Python (3.10+ recommended)

### 2️⃣ Clone Repository
