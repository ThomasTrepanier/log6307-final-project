from torch.autograd import Variable

type(y)  # <class 'torch.Tensor'>

y = Variable(y, requires_grad=True)
y = y.detach().numpy()

type(y)  #<class 'numpy.ndarray'>
