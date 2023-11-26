import numpy as np
from sklearn.model_selection import train_test_split
from torch.utils.data import Subset

def stratified_split(dataset, test_size=0.2):
    # Get the targets/labels of all instances in the dataset
    targets = np.array([t for _, t in dataset])
    
    # Get indices of all instances in the dataset
    indices = list(range(len(dataset)))
    
    # Use sklearn's train_test_split to split indices into train and test indices
    train_indices, test_indices = train_test_split(indices, test_size=test_size, stratify=targets)
    
    # Create PyTorch datasets using these train and test indices
    train_dataset = Subset(dataset, train_indices)
    test_dataset = Subset(dataset, test_indices)
    
    return train_dataset, test_dataset

train_dataset, test_dataset = stratified_split(your_dataset, test_size=0.2)
