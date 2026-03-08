import numpy as np
from sklearn.linear_model import LinearRegression

# dataset
hours = np.array([1,2,3,4,5]).reshape(-1,1)
scores = np.array([20,35,45,55,65])

# model
model = LinearRegression()
model.fit(hours, scores)

# prediction
pred = model.predict([[6]])

print("Predicted score for 6 hours study:", pred[0])