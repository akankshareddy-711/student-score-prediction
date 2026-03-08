import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset: study hours vs scores
hours = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
scores = np.array([20,30,40,50,60,70,80,90])

# Train model
model = LinearRegression()
model.fit(hours, scores)

# Predict score for 9 hours study
prediction = model.predict([[9]])

print("Predicted score for 9 hours study:", prediction[0])

# Visualization
plt.scatter(hours, scores, color="blue")
plt.plot(hours, model.predict(hours), color="red")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Student Score Prediction")
plt.show()