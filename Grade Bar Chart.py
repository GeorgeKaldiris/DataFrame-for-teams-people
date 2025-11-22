import matplotlib.pyplot as plt
import numpy as np

teams = ['Tottenham Hotspur', 'Liverpool', 'Manchester United', 'Leicester City']
team_points = [65, 74, 70, 64]
colors = ['#132257', '#C8102E', '#DA020E', '#003090']  # Χρώματα ομάδων

plt.figure(figsize=(12, 6))
plt.bar(teams, team_points, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
plt.title('EPL Team Points (Season)')
plt.xlabel('Teams')
plt.ylabel('Points')
plt.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=45)

# Προσθήκη τιμών πάνω από τις ράβδους
for i, points in enumerate(team_points):
    plt.text(i, points + 1, str(points), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()