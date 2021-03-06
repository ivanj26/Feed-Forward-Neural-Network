from model.util.activation_fun import sigmoid
from model.util.node import Node

class Layer:
  def __init__(self, nb_neurons = 1, activation = 'sigmoid', neurons = []):
    self.nb_neurons = nb_neurons
    self.activation = None
    if (activation == 'sigmoid'):
      self.activation = sigmoid
    
    if not neurons:
      self.neurons = [Node(self.activation) for i in range(self.nb_neurons)]
    else:
      self.neurons = neurons
  
  def feed_forward(self, x_before = []):
    for neuron in self.neurons:
      neuron.calc_net(x_before)
    return [n.net for n in self.neurons]

  def back_propagate(self, next_weights = [], next_gradients = []):
    weights = []
    gradients = []
    for i in range(len(self.neurons)):
      self.neurons[i].calc_gradient(i, next_weights, next_gradients)
      weights.append(self.neurons[i].weights)
      gradients.append(self.neurons[i].gradient)
    return weights, gradients

  def update_delta_weights(self, learning_rate, momentum, x_before = []):
    for neuron in self.neurons:
      neuron.calc_delta_weights(learning_rate = learning_rate, momentum = momentum, x=x_before)
    return [n.net for n in self.neurons]

  def update_delta_bias(self, learning_rate, momentum):
    for neuron in self.neurons:
      neuron.calc_delta_bias(learning_rate = learning_rate, momentum = momentum)
    return [n.delta_bias for n in self.neurons]
