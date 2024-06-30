import cv2
import time
from face_detection import detect_face_landmarks
from face_classification import classify_face_shape
from hairstyle_recommendation import recommend_styles

def display_recommended_styles(styles, face_shape, style_type):
    for style_path in styles:
        style_img = cv2.imread(style_path)
        resized_img = cv2.resize(style_img, (400, 400))

        # Add face shape text
        label = f"{face_shape} face {style_type}"
        cv2.putText(resized_img, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow(f'Recommended {style_type}', resized_img)
        cv2.waitKey(2000)  # Display each style for 2 seconds
        cv2.destroyWindow(f'Recommended {style_type}')

def capture_photo():
    gender = input("Are you male or female? ").strip().lower()
    if gender not in ['male', 'female']:
        print("Invalid input. Please enter 'male' or 'female'.")
        return
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        landmarks = detect_face_landmarks(frame)
        face_shape = classify_face_shape(landmarks)
        
        if face_shape:
            recommended_hairstyles = recommend_styles(face_shape, gender, num_recommendations=5)
            display_recommended_styles(recommended_hairstyles, face_shape, "Hairstyle")
            
            if gender == "male":
                recommended_beards = recommend_styles(face_shape, "male", num_recommendations=5)
                display_recommended_styles(recommended_beards, face_shape, "Beard")
        
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
