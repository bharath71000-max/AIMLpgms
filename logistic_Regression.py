# Logistic Regression (Simple Code)

from sklearn.linear_model import LogisticRegression

# Sample data
X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict
print(model.predict([[2.5]]))
