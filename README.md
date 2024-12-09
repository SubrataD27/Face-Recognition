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



How to Use
Step 1: Capture Face Images
Run the capture_faces.py script:
bash
Copy code
python capture_faces.py
Enter a user ID when prompted.
The script will capture 30 face images of the user. Look directly at the camera.
Captured images will be saved in the dataset directory in the format user.<ID>.<count>.jpg.

Step 2: Train the Model
Run the train_model.py script:
bash
Copy code
python train_model.py
This script will load all images from the dataset directory, encode them, and save the trained model as trained_faces.pkl.
Step 3: Recognize Faces
Run the recognize_faces.py script:

bash
Copy code
python recognize_faces.py
The script will use the trained model to recognize faces in real-time using your webcam.

Recognized faces will be labeled with their user ID.
Unknown faces will be labeled as "Unknown."
Press q to quit the webcam window.

```

### Notes:
Authors
Made by Subrata Dhibar
GitHub: SubrataD27
Email: subratadhibargcsj@gmail.com



