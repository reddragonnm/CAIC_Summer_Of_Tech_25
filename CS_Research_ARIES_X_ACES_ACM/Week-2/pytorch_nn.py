import torch
import torch.nn as nn

import pandas as pd


class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


if __name__ == "__main__":
    df = pd.read_csv("./train.csv")

    y = df["label"]
    X = df.drop(columns=["label"]).values / 255.0
    X = torch.FloatTensor(X)
    y = torch.LongTensor(y.values)

    input_size = X.shape[1]
    hidden_size = 128
    output_size = len(y.unique())
    model = SimpleNN(input_size, hidden_size, output_size)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    num_epochs = 100

    for epoch in range(num_epochs):
        optimizer.zero_grad()
        model.train()

        outputs = model(X)
        loss = criterion(outputs, y)

        # get accuracy
        _, predicted = torch.max(outputs, 1)
        correct = (predicted == y).sum().item()
        accuracy = correct / y.size(0)

        loss.backward()
        optimizer.step()

        print(
            f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f} Accuracy: {accuracy:.4f}"
        )
