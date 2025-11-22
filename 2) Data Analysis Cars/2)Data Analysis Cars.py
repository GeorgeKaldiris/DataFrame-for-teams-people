import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df = pd.read_csv(url, names=column_names, delim_whitespace=True)
# Clean the dataset
df['horsepower'] = df['horsepower'].replace('?', np.nan)
df['horsepower'] = df['horsepower'].astype(float)
df.dropna(inplace=True)
# Basic statistics
print(df.describe())
# Correlation matrix
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
print(df[numeric_columns].corr())
# Scatter plot of weight vs. mpg
plt.scatter(df['weight'], df['mpg'])
plt.xlabel('Weight')
plt.ylabel('Miles Per Gallon')
plt.title('Weight vs. MPG')
plt.show()