import os
import cv2

base = "data/raw/images"

bad_files = []

for cls in os.listdir(base):

    class_path = os.path.join(base, cls)

    for img_name in os.listdir(class_path):

        img_path = os.path.join(class_path, img_name)

        img = cv2.imread(img_path)

        if img is None:
            bad_files.append(img_path)

print(f"Corrupted images found: {len(bad_files)}")

for file in bad_files:
    print(file)