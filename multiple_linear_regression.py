# Import libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
# X = independent variables (multiple features)
# y = dependent variable

X = np.array([
    [1, 2],
    [2, 3],
    [4, 5],
    [3, 6],
    [5, 8]
])

y = np.array([3, 5, 9, 7, 11])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Predict new values
X_new = np.array([[6, 9]])
prediction = model.predict(X_new)

print("Prediction:", prediction)