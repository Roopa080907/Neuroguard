import torch
import torch.nn as nn
import snntorch as snn


class AlzheimerSNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()

        self.fc1 = nn.Linear(128 * 128, 512)
        self.lif1 = snn.Leaky(beta=0.9)

        self.fc2 = nn.Linear(512, 256)
        self.lif2 = snn.Leaky(beta=0.9)

        self.fc3 = nn.Linear(256, 3)
        self.lif3 = snn.Leaky(beta=0.9)

    def forward(self, x):

        x = self.flatten(x)

        mem1 = self.lif1.init_leaky()
        mem2 = self.lif2.init_leaky()
        mem3 = self.lif3.init_leaky()

        num_steps = 10

        spk3_rec = []

        for step in range(num_steps):

            cur1 = self.fc1(x)
            spk1, mem1 = self.lif1(cur1, mem1)

            cur2 = self.fc2(spk1)
            spk2, mem2 = self.lif2(cur2, mem2)

            cur3 = self.fc3(spk2)
            spk3, mem3 = self.lif3(cur3, mem3)

            spk3_rec.append(spk3)

        return torch.stack(spk3_rec).sum(dim=0)