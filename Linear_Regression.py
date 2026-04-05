# Simple Linear Regression without dataset

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define data manually
# X = Independent Variable
# Y = Dependent Variable
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

# Step 2: Calculate mean
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Step 3: Calculate slope (b)
numerator = np.sum((X - mean_x) * (Y - mean_y))
denominator = np.sum((X - mean_x) ** 2)

b = numerator / denominator

# Step 4: Calculate intercept (a)
a = mean_y - b * mean_x

print("Slope (b):", b)
print("Intercept (a):", a)

# Step 5: Predicted values
Y_pred = a + b * X

# Step 6: Plot graph
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, Y_pred, color='red', label='Regression Line')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")

plt.legend()
plt.show()
