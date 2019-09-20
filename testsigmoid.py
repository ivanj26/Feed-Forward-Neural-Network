import matplotlib.pyplot as plt
import numpy as np
from util.ActivationFunc import sigmoid

# create input with range x1 <= x <= x2 with n data
x = np.linspace(-10, 10, 100)

# plot graph
plt.plot(x, sigmoid(x))
plt.show()