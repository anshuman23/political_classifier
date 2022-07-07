import torch


class Dataset(torch.utils.data.Dataset):

    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        return {'input_ids': self.encodings['input_ids'][idx],
                'labels': torch.tensor(self.labels[idx]),
               }

    def __len__(self):
        return len(self.labels)
