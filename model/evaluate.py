import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np

# 🔥 IMPORTANT: use your SNN model here
from model import AlzheimerSNN

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Same transform as training
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# ✅ USE TEST DATA (NOT TRAINING DATA)
test_dataset = datasets.ImageFolder(
    root=r"C:\Users\roopa\OneDrive\Desktop\neuroguard\data\test",
    transform=transform
)

test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Load trained SNN model
model = AlzheimerSNN().to(device)
model.load_state_dict(torch.load("alzheimer_snn_model.pth", map_location=device))
model.eval()

y_true = []
y_pred = []

# Evaluation loop
with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        _, preds = torch.max(outputs, 1)

        y_true.extend(labels.cpu().numpy())
        y_pred.extend(preds.cpu().numpy())

# -------------------------
# 📊 METRICS
# -------------------------

acc = accuracy_score(y_true, y_pred)
print("\n==============================")
print("✅ TEST ACCURACY:", acc)
print("==============================\n")

print("📊 Classification Report:\n")
print(classification_report(
    y_true,
    y_pred,
    target_names=test_dataset.classes
))

# -------------------------
# 📉 CONFUSION MATRIX
# -------------------------

cm = confusion_matrix(y_true, y_pred)

print("\n📌 Confusion Matrix:\n")
print(cm)