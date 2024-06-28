import os
import random

def load_hairstyles(face_shape):
    folder_path = f"data/pics/{face_shape}"
    hairstyles = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return hairstyles

def recommend_hairstyles(face_shape, num_recommendations=3):
    hairstyles = load_hairstyles(face_shape)
    if len(hairstyles) < num_recommendations:
        num_recommendations = len(hairstyles)
    recommended_hairstyles = random.sample(hairstyles, num_recommendations)
    return recommended_hairstyles
