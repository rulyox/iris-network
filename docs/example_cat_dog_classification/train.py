import torch
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader

from dataset import catdog_set


device = 'cpu'
model_file = '/workspace/public/catdog_model.pth'


def train():
    dataloader = DataLoader(catdog_set, batch_size=32, shuffle=True, num_workers=4)

    model = torchvision.models.densenet121(pretrained=True)
    num_ftrs = model.classifier.in_features
    model.classifier = nn.Sequential(
        nn.Linear(num_ftrs, 500),
        nn.Linear(500, 2)
    )
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.002, amsgrad=True)
    scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=[500, 1000, 1500], gamma=0.5)

    epochs = 3
    itr = 1
    p_itr = 10
    model.train()
    total_loss = 0
    loss_list = []
    acc_list = []

    for epoch in range(epochs):
        for samples, labels in dataloader:
            samples, labels = samples.to(device), labels.to(device)
            optimizer.zero_grad()
            output = model(samples)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            scheduler.step()

            if itr % p_itr == 0:
                pred = torch.argmax(output, dim=1)
                correct = pred.eq(labels)
                acc = torch.mean(correct.float())
                print('[Epoch {}/{}] Iteration {} -> Train Loss: {:.4f}, Accuracy: {:.3f}'.format(epoch + 1, epochs, itr, total_loss / p_itr, acc))
                loss_list.append(total_loss / p_itr)
                acc_list.append(acc)
                total_loss = 0

            itr += 1

    torch.save(model.state_dict(), model_file)


if __name__ == '__main__':
    train()
