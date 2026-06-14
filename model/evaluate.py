import torch
import numpy as np
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

from model import AlzheimerCNN

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Transform (same as training)
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Dataset (use same path you fixed earlier)
dataset = datasets.ImageFolder(
    root=r"C:\Users\roopa\OneDrive\Desktop\neuroguard\data\raw\images",
    transform=transform
)

loader = DataLoader(dataset, batch_size=32, shuffle=False)

# Load model
model = AlzheimerCNN().to(device)
model.load_state_dict(torch.load("alzheimer_model.pth", map_location=device))
model.eval()

y_true = []
y_pred = []

# Evaluation loop
with torch.no_grad():
    for images, labels in loader:
        images = images.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        y_true.extend(labels.numpy())
        y_pred.extend(predicted.cpu().numpy())

# Accuracy
acc = accuracy_score(y_true, y_pred)
print("\nAccuracy:", acc)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_true, y_pred, target_names=dataset.classes))

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=dataset.classes,
            yticklabels=dataset.classes)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()  