import os
from torch.utils.data import Dataset, ConcatDataset
from torchvision import transforms
from PIL import Image


train_dir = '/workspace/private/train'
test_dir = '/workspace/private/test'


class CatDogDataset(Dataset):
    def __init__(self, file_list, dir, mode='train', transform=None):
        self.file_list = file_list
        self.dir = dir
        self.mode = mode
        self.transform = transform
        if self.mode == 'train':
            if 'dog' in self.file_list[0]:
                self.label = 1
            else:
                self.label = 0

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img = Image.open(os.path.join(self.dir, self.file_list[idx]))
        if self.transform:
            img = self.transform(img)
        if self.mode == 'train':
            img = img.numpy()
            return img.astype('float32'), self.label
        else:
            img = img.numpy()
            return img.astype('float32'), self.file_list[idx]


data_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.ColorJitter(),
    transforms.RandomCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.Resize(128),
    transforms.ToTensor()
])

test_transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])

train_files = os.listdir(train_dir)
cat_files = [tf for tf in train_files if 'cat' in tf]
dog_files = [tf for tf in train_files if 'dog' in tf]
test_files = os.listdir(test_dir)

cats = CatDogDataset(cat_files, train_dir, transform=data_transform)
dogs = CatDogDataset(dog_files, train_dir, transform=data_transform)

catdog_set = ConcatDataset([cats, dogs])
test_set = CatDogDataset(test_files, test_dir, mode='test', transform=test_transform)
