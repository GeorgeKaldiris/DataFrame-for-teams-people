import matplotlib.pyplot as plt
import numpy as np

players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
goals = [23, 25, 21, 22, 19]

plt.figure(figsize=(10, 6))
plt.plot(players, goals, marker='o', linewidth=2, markersize=8)
plt.title('Goals Scored by EPL Players in a Season')
plt.xlabel('Players')
plt.ylabel('Goals Scored')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()