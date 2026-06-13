import cv2
import os

input_dir = "data/raw/images"
output_dir = "data/processed"

IMG_SIZE = 128

for cls in os.listdir(input_dir):

    class_path = os.path.join(input_dir, cls)

    if not os.path.isdir(class_path):
        continue

    output_class = os.path.join(output_dir, cls)
    os.makedirs(output_class, exist_ok=True)

    for img_name in os.listdir(class_path):

        img_path = os.path.join(class_path, img_name)

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

        cv2.imwrite(
            os.path.join(output_class, img_name),
            img
        )

print("Preprocessing completed")