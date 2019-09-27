import numpy as np

class Node:
  def __init__(self, activation, bias):
    self.bias = np.random.rand()
    self.bias = bias
    self.delta_weights = []
    self.gradient = 0
    self.weights = []
    self.net = 0
    self.error = 0
    self.activation = activation
  
  def rand_weights(self, dimension: int):
    for _ in range(dimension):
      self.weights.append(np.random.rand())

  def calc_dot_prod(self, x):
    sum = 0
    for i in range(len(x)):
      sum += (x[i] * self.weights[i])
    return sum + self.bias

  def calc_net(self, x):
    self.net = self.activation(self.calc_dot_prod(x))
    return self.net

  def calc_error(self, diff):
    self.gradient = self.net * (1.0 - self.net) * diff
    return self.gradient

  def calc_delta_weights(self, delta, learning_rate, momentum):
    pass

  def set_weights(self, w):
    self.weights = w