import torch
import pandas as pd
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

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
batch_size = 32
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

# build custom module for logistic regression
class LogisticRegression(torch.nn.Module):
	# build the constructor
	def __init__(self, n_inputs, n_outputs):
		super().__init__()
		self.linear = torch.nn.Linear(n_inputs, n_outputs)
		self.cuda()
	# make predictions
	def forward(self, x):
		y_pred = torch.sigmoid(self.linear(x))
		return y_pred

# instantiate the model
n_inputs = 28*28 # makes a 1D vector of 784
n_outputs = 10
log_regr = LogisticRegression(n_inputs, n_outputs)

# defining the optimizer
optimizer = torch.optim.SGD(log_regr.parameters(), lr=0.001)
# defining Cross-Entropy loss
criterion = torch.nn.CrossEntropyLoss()

epochs = 50
Loss = []
acc = []
for epoch in range(epochs):
	for i, (images, labels) in enumerate(train_loader):
		images, labels = images.to(device='cuda'), labels.to(device='cuda')
		optimizer.zero_grad()
		outputs = log_regr(images.view(-1, 28*28))
		loss = criterion(outputs, labels)
		loss.backward()
		optimizer.step()
	Loss.append((epoch, loss.item()))
	correct = 0
	for images, labels in test_loader:
		images, labels = images.to(device='cuda'), labels.to(device='cuda')
		outputs = log_regr(images.view(-1, 28*28))
		_, predicted = torch.max(outputs.data, 1)
		correct += (predicted == labels).sum()
	accuracy = 100 * (correct.item()) / len(test_dataset)
	acc.append(accuracy)
	print('Epoch: {}. Loss: {}. Accuracy: {}'.format(epoch, loss.item(), accuracy))

data = pd.DataFrame({'Epoch': [x[0] for x in Loss], 'Loss': [x[1] for x in Loss]})
data.to_csv("linear_loss.csv")

plt.plot(Loss)
plt.xlabel("no. of epochs")
plt.ylabel("total loss")
plt.title("Loss")
plt.show()
