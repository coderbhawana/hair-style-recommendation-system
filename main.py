import cv2
import time
from face_detection import detect_face_landmarks
from face_classification import classify_face_shape
from hairstyle_recommendation import recommend_hairstyles

def display_recommended_hairstyles(hairstyles, face_shape):
    for hairstyle_path in hairstyles:
        hairstyle_img = cv2.imread(hairstyle_path)
        resized_img = cv2.resize(hairstyle_img, (300, 300))

        # Add face shape text
        cv2.putText(resized_img, face_shape, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow('Recommended Hairstyle', resized_img)
        cv2.waitKey(5000)  # Display each hairstyle for 5 seconds
        cv2.destroyWindow('Recommended Hairstyle')

def capture_photo():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        landmarks = detect_face_landmarks(frame)
        face_shape = classify_face_shape(landmarks)
        
        if face_shape:
            recommended_hairstyles = recommend_hairstyles(face_shape, num_recommendations=3)
            display_recommended_hairstyles(recommended_hairstyles, face_shape)
        
        # Draw landmarks on face
        for (x, y) in landmarks:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_photo()
