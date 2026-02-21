import torch
import numpy as np
import pandas as pd
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from sklearn import svm #Import svm model
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

# loading training data
train_dataset = datasets.MNIST(root='./data',
							   train=True,
							   transform=transforms.ToTensor(),
							   download=True)
# loading test data
test_dataset = datasets.MNIST(root='./data',
							  train=False,
							  transform=transforms.ToTensor())

# load train and test data samples into dataloader
#batch_size = 32
train_loader = DataLoader(dataset=train_dataset, batch_size=len(train_dataset), shuffle=True)
test_loader = DataLoader(dataset=test_dataset, shuffle=False)

X_train = []
y_train = []

for images, labels in train_loader:
	X_train.append(images.numpy())
	y_train.append(labels.numpy())

X_train = np.concatenate(X_train, axis=0).reshape(-1, 28*28)
y_train = np.concatenate(y_train, axis=0)

#X_train = X_train.reshape(-1, 28*28)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
