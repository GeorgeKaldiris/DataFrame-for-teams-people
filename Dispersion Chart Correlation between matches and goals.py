import matplotlib.pyplot as plt
import numpy as np

goals = [23, 25, 21, 22, 19]
games = [34, 33, 34, 35, 33]

plt.figure(figsize=(10, 6))
plt.scatter(games, goals, s=100, alpha=0.7, color='red')
plt.title('Goals Scored vs Games Played (Season)')
plt.xlabel('Games Played')
plt.ylabel('Goals Scored')
plt.grid(True, alpha=0.3)

# Προσθήκη ονομάτων παικτών
players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
for i, player in enumerate(players):
    plt.annotate(player, (games[i], goals[i]), xytext=(5, 5), 
                textcoords='offset points', fontsize=9)

plt.tight_layout()
plt.show()