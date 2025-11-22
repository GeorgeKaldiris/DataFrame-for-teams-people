import matplotlib.pyplot as plt
import numpy as np

# Δημιουργία δεδομένων κατηγοριών
years = np.arange(2010, 2021)
category1 = np.random.randint(50, 100, 11)
category2 = np.random.randint(100, 150, 11)
category3 = np.random.randint(150, 200, 11)

# Δημιουργία γραφήματος κατηγοριών
plt.figure(figsize=(12, 6))
plt.plot(years, category1, label='Category 1', linestyle='-', color='blue', marker='o')
plt.plot(years, category2, label='Category 2', linestyle='--', color='green', marker='^')
plt.plot(years, category3, label='Category 3', linestyle=':', color='red', marker='s')

# Προσθήκη ετικετών και τίτλου
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Annual Trends for Category 1, 2, and 3 (2010-2020)')
plt.legend()
plt.show()