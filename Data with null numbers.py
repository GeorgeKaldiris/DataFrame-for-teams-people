import pandas as pd
import numpy as np

data = {
   'Name': ['Alice', 'Bob', None, 'Eve'],
   'Age': [25, 32, 45, None],
   'Profession': ['Engineer', None, 'Doctor', 'Artist']
}

df = pd.DataFrame(data)
print(df)

# Εντοπισμός ελλιπών τιμών
print("Ελλιπείς τιμές:")
print(df.isnull())

print("Σύνολο ελλιπών τιμών ανά στήλη:")
print(df.isnull().sum())

# Αφαίρεση γραμμών με ελλιπείς τιμές
df_dropped = df.dropna()
print("Μετά την αφαίρεση:")
print(df_dropped)

print(f"Σχήμα πριν: {df.shape}")
print(f"Σχήμα μετά: {df_dropped.shape}")

 #Συμπλήρωση με σταθερή τιμή
df_filled = df.fillna('Unknown')
print("Μετά τη συμπλήρωση:")
print(df_filled)

# Συμπλήρωση με διαφορετικές τιμές ανά στήλη
fill_values = {'Name': 'Unknown', 'Age': df['Age'].mean(), 'Profession': 'Unemployed'}
df_custom = df.fillna(fill_values)
print("Προσαρμοσμένη συμπλήρωση:")
print(df_custom)