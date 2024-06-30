import os
import random

def load_hairstyles(face_shape, gender):
    base_folder = "data/pics" if gender == "female" else "beard-data/pics"
    folder_path = os.path.join(base_folder, face_shape)
    styles = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return styles

def recommend_styles(face_shape, gender, num_recommendations=3):
    styles = load_hairstyles(face_shape, gender)
    if len(styles) < num_recommendations:
        num_recommendations = len(styles)
    recommended_styles = random.sample(styles, num_recommendations)
    return recommended_styles
