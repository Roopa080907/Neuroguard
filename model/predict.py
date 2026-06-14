import torch
from torchvision import transforms
from PIL import Image
from model import AlzheimerSNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --------------------
# LOAD SNN MODEL
# --------------------
model = AlzheimerSNN().to(device)
model.load_state_dict(torch.load("alzheimer_snn_model.pth", map_location=device))
model.eval()

# --------------------
# CLASSES
# --------------------
classes = ['Mild Dementia', 'Moderate Dementia', 'Non Demented']

# --------------------
# TRANSFORM
# --------------------
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.Grayscale(num_output_channels=1),
    transforms.ToTensor()
])

# --------------------
# PREDICT FUNCTION
# --------------------
def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        probs = torch.softmax(output, dim=1)
        confidence, pred = torch.max(probs, 1)

    return {
        "prediction": classes[pred.item()],
        "confidence": float(confidence.item())
    }
