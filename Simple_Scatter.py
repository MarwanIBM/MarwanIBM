import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.random.rand(100, 1)
Y = 4 + 5 * X + np.random.randn(100, 1)

plt.scatter(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Scatter Plot")
plt.show()