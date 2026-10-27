import cv2
import mediapipe as mp
import csv
import os

mp_hands = mp.solutions.hands
# Yahan static_image_mode=True karna zaroori hai kyunki hum video nahi, images process kar rahe hain
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)

DATA_DIR = './dataset' # Kaggle se download kiye hue folder ka path

with open('dataset.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    
    # Har folder (label) ke andar loop chalayega
    for dir_name in os.listdir(DATA_DIR):
        class_dir = os.path.join(DATA_DIR, dir_name)
        if not os.path.isdir(class_dir): 
            continue
        
        print(f"Processing label: {dir_name}...")
        
        # Folder ke andar ki har image ko process karega
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            image = cv2.imread(img_path)
            
            if image is None: 
                continue
            
            # MediaPipe ke liye BGR ko RGB mein badalna
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_image)
            
            # Agar image mein haath detect hota hai, toh uske points CSV mein save karega
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    row = [dir_name] # Pehla column label hoga (jaise 'A' ya 'B')
                    for landmark in hand_landmarks.landmark:
                        row.extend([landmark.x, landmark.y, landmark.z])
                    
                    writer.writerow(row)

print("Dataset CSV successfully created!")