import cv2
import os

INPUT_DIR = "data/raw/images"
OUTPUT_DIR = "data/processed"

IMG_SIZE = 128

for class_name in os.listdir(INPUT_DIR):

    class_path = os.path.join(INPUT_DIR, class_name)

    if not os.path.isdir(class_path):
        continue

    output_class = os.path.join(OUTPUT_DIR, class_name)
    os.makedirs(output_class, exist_ok=True)

    for image_name in os.listdir(class_path):

        image_path = os.path.join(class_path, image_name)

        img = cv2.imread(image_path)

        if img is None:
            print(f"Skipped: {image_name}")
            continue

        # Convert to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Resize
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

        save_path = os.path.join(output_class, image_name)

        cv2.imwrite(save_path, img)

print("Preprocessing completed!")