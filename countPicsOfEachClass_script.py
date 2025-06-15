import os
from collections import defaultdict

def count_finger_files(directory):
    counts = defaultdict(int)
    classes = ['0', '1', '2', '3', '4', '5']

    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            finger_class = filename[-6]
            if finger_class in classes:
                counts[finger_class] += 1

    print("Finger file counts:")
    for finger_class in classes:
        print(f"Class {finger_class}: {counts[finger_class]}")

directory_path = './fingers/test'
#directory_path = './fingers/train'
count_finger_files(directory_path)
