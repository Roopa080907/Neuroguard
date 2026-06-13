import torch
import torch.nn as nn

class BrainNet(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        self.network = nn.Sequential(
            nn.Flatten(),
            nn.Linear(224 * 224, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        return self.network(x)