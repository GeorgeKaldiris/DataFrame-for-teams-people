# Import pandas
import pandas as pd

# Define data
data = {
    'Name': ['John Doe', 'Jane Smith', 'Mike Brown', 'Alice Johnson', 'Charlie Davis', 
             'Elizabeth Green', 'James White', 'Linda Miller', 'David Clark', 'Jennifer Rodriguez'],
    'Occupation': ['Engineer', 'Doctor', 'Lawyer', 'Artist', 'Scientist', 
                   'Teacher', 'Nurse', 'Journalist', 'Actor', 'Architect'],
    'Age': [30, 28, 29, 32, 31, 30, 32, 33, 32, 30],
    'Experience': [5, 3, 4, 2, 5, 2, 3, 1, 2, 4],
    'Projects': [12, 7, 15, 11, 7, 16, 2, 10, 11, 6],
    'Sick_Days': [1, 3, 4, 2, 1, 2, 3, 1, 2, 2],
    'Vacation_Days': [10, 12, 15, 12, 10, 9, 11, 13, 10, 14]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Εκτύπωση του σχήματος του DataFrame
print('DataFrame Shape:', df.shape, '')

# Εκτύπωση των στηλών του DataFrame
print('DataFrame Columns:', df.columns, '')

# Εκτύπωση λεπτομερών πληροφοριών για το DataFrame
print('DataFrame Info:')
print(df.info())

# Εκτύπωση των περιγραφικών στατιστικών για το DataFrame
print('DataFrame Statistics:')
print(df.describe(), '')

# Εκτύπωση του μέσου αριθμού ετών εμπειρίας
print('Mean Experience:', df['Experience'].mean(), '')

# Εκτύπωση του ατόμου με τα περισσότερα έργα
print('Individual with Most Projects:', df['Name'][df['Projects'].idxmax()])

# Εκτύπωση των 5 πρώτων γραμμών του DataFrame
print('First 5 Rows:')
print(df.head(), '')

# Εκτύπωση στηλών 'Name' και 'Experience' για άτομα με περισσότερα από 3 έτη εμπειρίας
print('Individuals with More Than 3 Years of Experience:')
print(df.loc[df['Experience'] > 3, ['Name', 'Experience']], '')

# Εκτύπωση της γραμμής για τον 'John Doe'
print('Row for John Doe:')
print(df.loc[df['Name'] == 'John Doe'])




