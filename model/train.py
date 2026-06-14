import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import numpy as np

from model import AlzheimerSNN

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Transform
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Dataset (TRAIN ONLY)
train_dataset = datasets.ImageFolder(
    root=r"C:\Users\roopa\OneDrive\Desktop\neuroguard\data\train",
    transform=transform
)

print("Classes:", train_dataset.classes)
print("Total images:", len(train_dataset))

# DataLoader
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

# Model
model = AlzheimerSNN().to(device)

# Loss (simple safe version for hackathon)
criterion = nn.CrossEntropyLoss()

# Optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Epochs (START SMALL)
epochs = 6

# Training loop
for epoch in range(epochs):

    model.train()
    running_loss = 0.0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f"Epoch [{epoch+1}/{epochs}] Loss: {running_loss/len(train_loader):.4f}")

# Save model
torch.save(model.state_dict(), "alzheimer_snn_model.pth")

print("Model saved successfully!")