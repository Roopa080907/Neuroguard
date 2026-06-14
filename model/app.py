import torch
from flask import Flask, request, jsonify
from torchvision import transforms
from PIL import Image
import os

from model import AlzheimerSNN

app = Flask(__name__)

# -------------------------
# CONFIG
# -------------------------
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------------------------
# LOAD MODEL
# -------------------------
model = AlzheimerSNN().to(device)

model_path = "alzheimer_snn_model.pth"  # ✅ FIXED PATH FOR RENDER + LOCAL
model.load_state_dict(torch.load(model_path, map_location=device))

model.eval()

# -------------------------
# CLASSES
# -------------------------
classes = ['Mild Dementia', 'Moderate Dementia', 'Non Demented']

# -------------------------
# TRANSFORM
# -------------------------
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# -------------------------
# ROUTES
# -------------------------
@app.route("/")
def home():
    return "NeuroGuard SNN API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        # preprocess
        image = Image.open(path).convert("RGB")
        image = transform(image).unsqueeze(0).to(device)

        # inference
        with torch.no_grad():
            output = model(image)
            probs = torch.softmax(output, dim=1)
            confidence, pred = torch.max(probs, 1)

        return jsonify({
            "prediction": classes[pred.item()],
            "confidence": round(float(confidence.item()), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------
# RUN (FOR RENDER)
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ Render uses PORT env variable
    app.run(host="0.0.0.0", port=port, debug=False)