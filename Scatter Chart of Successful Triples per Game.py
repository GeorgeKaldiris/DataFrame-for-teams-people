import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 'Kylian Mbappe', 'Robert Lewandowski'],
    'Games Played': [38, 40, 35, 39, 34],
    'Goals': [36, 34, 21, 33, 41],
    'Assists': [12, 7, 10, 7, 5],
    'Successful Dribbles': [174, 89, 142, 90, 41],
    'Yellow Cards': [3, 5, 6, 2, 1]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
for player in df['Player']:
    plt.scatter(df[df['Player'] == player]['Games Played'], 
                df[df['Player'] == player]['Successful Dribbles'], 
                label=player)

plt.xlabel('Games Played')
plt.ylabel('Successful Dribbles')
plt.title('Relationship between Games Played and Successful Dribbles')
plt.legend()
plt.grid(True)
plt.show()