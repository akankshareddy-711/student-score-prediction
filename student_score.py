import pandas as pd
import matplotlib.pyplot as plt

# Create sample student dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 70, 90, 60, 88],
    "Science": [78, 65, 92, 55, 80],
    "English": [82, 75, 88, 62, 85]
}

df = pd.DataFrame(data)

# Calculate average score
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("Student Data:")
print(df)

# Top performer
top_student = df.loc[df["Average"].idxmax()]
print("\nTop Performer:")
print(top_student)

# Plot average scores
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Scores")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.show()