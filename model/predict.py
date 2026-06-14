import torch
from torchvision import transforms
from PIL import Image
from model import AlzheimerCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AlzheimerCNN().to(device)
model.load_state_dict(torch.load("alzheimer_model.pth", map_location=device))
model.eval()

classes = ['Mild Dementia', 'Moderate Dementia', 'Non Demented', 'Very mild Dementia']

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.Grayscale(num_output_channels=1),
    transforms.ToTensor()
])

def predict_image(image_path):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        probs = torch.softmax(output, dim=1)
        confidence, pred = torch.max(probs, 1)

    return {
        "prediction": classes[pred.item()],
        "confidence": float(confidence.item())
    }