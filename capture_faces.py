import cv2
import os

# Create a directory to store images if it doesn't exist
if not os.path.exists('dataset'):
    os.makedirs('dataset')

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Load Haar Cascade for face detection
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

user_id = input("Enter user ID: ")
count = 0

print("Capturing images. Look at the camera...")

while count < 30:  # Capture 30 images
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        cv2.imwrite(f"dataset/user.{user_id}.{count}.jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Capturing Faces', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
print("Images captured.")