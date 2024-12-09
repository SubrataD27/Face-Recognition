import face_recognition
import os
import pickle

# Prepare data for training
known_face_encodings = []
known_face_names = []

# Load images from dataset folder and encode faces
for filename in os.listdir('dataset'):
    if filename.endswith('.jpg'):
        image_path = os.path.join('dataset', filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        
        known_face_encodings.append(encoding)
        name = filename.split('.')[1]  # Extract user ID from filename
        known_face_names.append(name)

# Save the trained model to a file
with open('trained_faces.pkl', 'wb') as f:
    pickle.dump((known_face_encodings, known_face_names), f)

print("Model trained and saved successfully.")