# Εισαγωγή pandas
import pandas as pd

# Define data
data = {
    'Name': ['John Doe', 'Jane Smith', 'Bill Gates', 'Elon Musk', 'John Doe', 
             None, 'Steve Jobs', 'Mark Zuckerberg', 'Jack Dorsey', 'Sundar Pichai'],
    'Previous_Team': ['Team Alpha', 'Team Bravo', 'Team Charlie', 'Team Delta', 'Team Alpha', 
                      'Team Echo', 'Team Foxtrot', 'Team Golf', 'Team Hotel', None],
    'Current_Team': ['Team Bravo', 'Team Charlie', 'Team Delta', 'Team Echo', 'Team Bravo', 
                     'Team Foxtrot', 'Team Golf', 'Team Hotel', 'Team India', 'Team Juliet'],
    'Contract_Fee_Millions': [0, 15, 222, 180, 0, 37, 35, 76, 85, 42],
    'Contract_Transition_Date': ['2021-08-10', '2021-08-31', '2017-08-03', '2018-07-01', 
                                 '2021-08-10', None, '2014-07-01', '2015-08-30', 
                                 '2018-07-01', '2017-07-01']
}

# Δημιουργία του DataFrame
df = pd.DataFrame(data)

# Εμφάνιση του DataFrame
print(df)

# Εκτυπώση του αριθμού των τιμών που λείπουν σε κάθε στήλη
print('Missing Values:')
print(df.isnull().sum(), '\n')

# Συμπλήρωση των ονομάτων που λείπουν και την προηγούμενη ομάδα με 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')
df['Previous_Team'] = df['Previous_Team'].fillna('Unknown')

# Απάλειψη των γραμμών με ελλείπουσες ημερομηνίες μετάβασης στη σύμβαση
df = df.dropna(subset=['Contract_Transition_Date'])

# Εκτύπωση του DataFrame μετά το χειρισμό των ελλιπών τιμών
print('\nDataFrame after handling missing values:')
print(df)

# Εκτύπωση του αριθμού των διπλότυπων γραμμών
print('Number of duplicate rows:', df.duplicated().sum())

# Αφαίρεση των διπλότυπων γραμμών
df = df.drop_duplicates()

# Εκτύπωση του DataFrame μετά την αφαίρεση των διπλότυπων
print('\nDataFrame after removing duplicates:')
print(df)

# Ορισμός νέων ονομάτων στηλών
new_column_names = {
    'Name': 'name',
    'Previous_Team': 'previous_team',
    'Current_Team': 'current_team',
    'Contract_Fee_Millions': 'contract_fee_millions',
    'Contract_Transition_Date': 'contract_transition_date'
}

# Μετονομασία των στηλών
df = df.rename(columns=new_column_names)

# Εκτύπωση του DataFrame μετά τη μετονομασία των στηλών
print('\nDataFrame after renaming columns:')
print(df)

# Αντικατάσταση των ονομάτων 'Unknown' με 'Undisclosed'
df['previous_team'] = df['previous_team'].replace('Unknown', 'Undisclosed')

# Εκτύπωση του DataFrame μετά την αντικατάσταση των τιμών
print('\nDataFrame after replacing values:')
print(df)