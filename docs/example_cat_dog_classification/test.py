import pandas as pd
import torch
import torchvision
from torch.utils.data import DataLoader

from dataset import test_set


device = 'cpu'
model_file = '/workspace/public/catdog_model.pth'
result_file = '/workspace/public/catdog_result.csv'


def test():
    model = torchvision.models.densenet121(pretrained=True)
    model.load_state_dict(torch.load(model_file), strict=False)
    model.eval()

    testloader = DataLoader(test_set, batch_size=32, shuffle=False, num_workers=4)

    fn_list = []
    pred_list = []
    for x, fn in testloader:
        with torch.no_grad():
            x = x.to(device)
            output = model(x)
            pred = torch.argmax(output, dim=1)
            fn_list += [n[:-4] for n in fn]
            pred_list += [p.item() for p in pred]

    submission = pd.DataFrame({'id': fn_list, 'label': pred_list})
    submission.to_csv(result_file, index=False)


if __name__ == '__main__':
    test()
