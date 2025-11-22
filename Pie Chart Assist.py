import matplotlib.pyplot as plt
import numpy as np

players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
assists = [8, 7, 11, 6, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(assists, labels=players, autopct='%1.1f%%', 
                                   colors=colors, startangle=90, 
                                   explode=(0, 0, 0.1, 0, 0))  # Έμφαση στον Bruno

plt.title('Assists Distribution among EPL Players (Season)', fontsize=14, fontweight='bold')

# Βελτίωση εμφάνισης κειμένου
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.axis('equal')
plt.show()