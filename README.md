# 🧠 Computer Vision Projects using OpenCV & MediaPipe

This repository contains real-time computer vision applications built using **OpenCV** and **MediaPipe**.
It demonstrates face detection, eye tracking, smile detection, and hand gesture recognition using webcam input.

---

## 🚀 Features

* 👤 Face Detection using Haar Cascade
* 👁️ Eye Detection
* 😊 Smile Detection
* ✋ Hand Tracking using MediaPipe
* 🔢 Finger Counting (Real-time)
* 🎥 Live Webcam Processing

---

## 🛠️ Tech Stack

* Python 3.x
* OpenCV (`cv2`)
* MediaPipe
* NumPy

---

## 📂 Project Structure

```
.
├── app.py                      # Basic face detection
├── face_eye_smile.py          # Face + Eye + Smile + Hand detection
├── Face & Object Detection/
│   ├── haarcascade_frontalface_default.xml
│   ├── haarcascade_eye.xml
│   └── haarcascade_smile.xml
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ How to Run

### 1. Face Detection

```bash
python app.py
```

### 2. Full Smart Detection (Face + Hand)

```bash
python face_eye_smile.py
```

---

## 🎮 Controls

* Press **`q`** to exit the webcam window

---

## 🧠 How It Works

* OpenCV uses **Haar Cascade classifiers** for detecting faces, eyes, and smiles
* MediaPipe is used for **hand landmark detection**
* Finger counting is implemented using landmark position logic
* Real-time frames are processed continuously from webcam

---

## ⚡ Performance Notes

* Works on CPU (no GPU required)
* For better performance:

  * Reduce frame size
  * Optimize detection frequency

---

## 📌 Future Improvements

* Add Face Recognition (not just detection)
* Improve gesture accuracy
* Add GUI (Tkinter / Streamlit)
* Deploy as a web app

---

## 🙌 Author

**Kuldeep Amareliya**

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
