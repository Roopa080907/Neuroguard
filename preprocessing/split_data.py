import os
import shutil
from sklearn.model_selection import train_test_split

source_dir = "data/raw/images"

train_dir = "data/train"
test_dir = "data/test"

classes = os.listdir(source_dir)

for cls in classes:

    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(test_dir, cls), exist_ok=True)

    files = os.listdir(os.path.join(source_dir, cls))

    train_files, test_files = train_test_split(
        files,
        test_size=0.2,
        random_state=42
    )

    for file in train_files:
        shutil.copy(
            os.path.join(source_dir, cls, file),
            os.path.join(train_dir, cls, file)
        )

    for file in test_files:
        shutil.copy(
            os.path.join(source_dir, cls, file),
            os.path.join(test_dir, cls, file)
        )

print("Dataset split completed.")