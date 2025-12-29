import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader
from cnn_model import SimpleCNN
import matplotlib.pyplot as plt

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model
model = SimpleCNN().to(device)
model.load_state_dict(torch.load("../models/cnn_classifier.pth", map_location=device))
model.eval()
print("Model loaded ✔")

# Data transforms
transform = transforms.Compose([
    transforms.Resize((64,64)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])

test_data = CIFAR10(root='../data', train=False, download=False, transform=transform)
test_loader = DataLoader(test_data, batch_size=32)

labels_map = test_data.classes

correct, total = 0,0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        
        outputs = model(images)
        _, predicted = torch.max(outputs,1)

        total += labels.size(0)
        correct += (predicted==labels).sum().item()

print(f"Accuracy: {correct/total*100:.2f}% ✔")
import random

# Random sample test
i = random.randint(0, len(test_data)-1)
img, label = test_data[i]
plt.imshow(img.permute(1,2,0)*0.5+0.5)  # convert back to image
plt.axis("off")

img_tensor = img.unsqueeze(0).to(device)
pred = torch.argmax(model(img_tensor), dim=1).item()

print("Actual:", labels_map[label])
print("Predicted:", labels_map[pred])
