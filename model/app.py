import torch
from flask import Flask, request, jsonify
from torchvision import transforms
from PIL import Image
import os

from model import AlzheimerSNN

app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model
model = AlzheimerSNN().to(device)
model.load_state_dict(torch.load("alzheimer_snn_model.pth", map_location=device))
model.eval()

# Classes (3-class setup)
classes = ['Mild Dementia', 'Moderate Dementia', 'Non Demented']

# Transform (same as training)
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "NeuroGuard SNN API is running 🚀"


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # Load image
    image = Image.open(path)
    image = transform(image).unsqueeze(0).to(device)

    # Prediction
    with torch.no_grad():
        output = model(image)
        probs = torch.softmax(output, dim=1)
        confidence, pred = torch.max(probs, 1)

    return jsonify({
        "prediction": classes[pred.item()],
        "confidence": float(confidence.item())
    })


if __name__ == "__main__":
    app.run(debug=True)