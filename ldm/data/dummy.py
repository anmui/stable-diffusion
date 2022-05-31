import numpy as np
import random
import string
from torch.utils.data import Dataset, Subset

class DummyData(Dataset):
    def __init__(self, length, size):
        self.length = length
        self.size = size

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        x = np.random.randn(*self.size)
        letters = string.ascii_lowercase
        y = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        return {"jpg": x, "txt": y}