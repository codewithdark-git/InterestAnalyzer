import cv2
from deepface import DeepFace
import os
import numpy as np

# Load the pre-trained Haar Cascade classifier for face detection

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Define emotion colors
emotion_colors = {
    'angry': (0, 0, 255),  # Red
    'disgust': (0, 255, 255),  # Yellow
    'fear': (255, 0, 0),  # Blue
    'happy': (0, 255, 0),  # Green
    'sad': (255, 255, 0),  # Cyan
    'surprise': (255, 0, 255),  # Magenta
    'neutral': (255, 255, 255)  # White
}

inner = ['happy', 'surprise', 'neutral']

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or specify a different index for other cameras

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for better performance
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the face region for emotion detection
        roi_color = frame[y:y + h, x:x + w]

        # Apply emotion detection model to the cropped face
        try:
            result = DeepFace.analyze(roi_color, actions=['emotion'], enforce_detection=False)
            res = result[0]
            dominant_emotion = res['dominant_emotion']
            emotion_confidence = res['emotion'][dominant_emotion]

            # Display the recognized emotion with confidence level
            color = emotion_colors.get(dominant_emotion, (255, 255, 255))
            label = f"{dominant_emotion}: {emotion_confidence:.2f}%"
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            # Check if confidence level is above 70%
            if dominant_emotion in inner and emotion_confidence > 70:
                interest_label = "Person is interested"
                cv2.putText(frame, interest_label, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            else:
                interest_label = "Person is not interested"
                cv2.putText(frame, interest_label, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        except Exception as e:
            print(f"Error in emotion detection: {e}")

    # Display the resulting frame
    cv2.imshow('Emotion Detection', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
