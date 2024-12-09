# Face Recognition System

A simple and efficient face recognition system built using Python, OpenCV, and the `face_recognition` library. This project captures face images, trains a model to recognize faces, and performs real-time face recognition using a webcam.

---

## Features

- **Face Image Capture**: Capture face images and save them to a dataset.
- **Model Training**: Train a face recognition model using the captured images.
- **Real-Time Recognition**: Perform face recognition in real-time using a webcam.

---

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- Python 3.7+
- Required Python Libraries:
  - `opencv-python`
  - `face-recognition`
  - `numpy`

To install dependencies, run:
```bash
pip install opencv-python face-recognition numpy

Face-Recognition-System/
│
├── dataset/               # Stores captured face images
├── capture_faces.py       # Script to capture face images
├── train_model.py         # Script to train the recognition model
├── recognize_faces.py     # Script for real-time face recognition
├── trained_faces.pkl      # Trained face encodings (auto-generated)
└── README.md              # Documentation file



python capture_faces.py
