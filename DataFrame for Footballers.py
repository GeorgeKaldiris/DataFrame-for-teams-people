# Εισαγωγή pandas
import pandas as pd

# Ορισμός δεδομένων παικτών
player_data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 
               'Kylian Mbappé', 'Robert Lewandowski'],
    'Team': ['PSG', 'Manchester United', 'PSG', 'PSG', 'Bayern Munich'],
    'Position': ['Forward', 'Forward', 'Forward', 'Forward', 'Forward']
}

# Δημιουργία DataFrame παικτών
df_player = pd.DataFrame(player_data)

# Ορισμός δεδομένων απόδοσης
performance_data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 
               'Kylian Mbappé', 'Robert Lewandowski'],
    'Goals': [30, 31, 27, 33, 36],
    'Assists': [15, 12, 17, 15, 9]
}

# Δημιουργία DataFrame επιδόσεων
df_performance = pd.DataFrame(performance_data)

# Εμφάνιση των DataFrames
print('Player DataFrame:')
print(df_player)
print('\nPerformance DataFrame:')
print(df_performance)

# Ορισμός της συνάρτησης για τον υπολογισμό του goal-assist ratio
def calculate_ratio(goals, assists):
    if assists == 0:
        return goals
    return goals / assists

# Προσθήκη νέας στήλη
df_performance['Goal_Assist_Ratio'] = df_performance.apply(
    lambda row: calculate_ratio(row['Goals'], row['Assists']), axis=1
)

# Εκτύπωση του ενημερωμένου DataFrame
print('\nPerformance DataFrame with Goal-Assist Ratio:')
print(df_performance)

# Ταξινόμηση με βάση τους στόχους
df_sorted_goals = df_performance.sort_values('Goals', ascending=False)

# Προσθήκη κατάταξης με βάση τους στόχους
df_sorted_goals['Goal_Rank'] = df_sorted_goals['Goals'].rank(ascending=False)

# Εκτύπωση του ενημερωμένου DataFrame
print('\nDataFrame Sorted by Goals:')
print(df_sorted_goals)

# Ομαδοποίηση ανά ομάδα
df_grouped = df_player.groupby('Team')['Player'].size()

# Εκτύπωση του ομαδοποιημένου DataFrame
print('\nNumber of Players per Team:')
print(df_grouped)

# Συγχώνευση των πλαισίων των δεδομένων στο 'Player'
df_merged = pd.merge(df_player, df_performance, on='Player')

# Εκτύπωση του συγχωνευμένο DataFrame
print('\nMerged DataFrame:')
print(df_merged)