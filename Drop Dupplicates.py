import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Eve', 'Alice', 'Eve', 'Charlie'],
    'Age': [25, 32, 29, 25, 29, 35],
    'City': ['Athens', 'Thessaloniki', 'Patras', 'Athens', 'Patras', 'Athens']
}
df = pd.DataFrame(data)

# Remove duplicates
df_no_duplicates = df.drop_duplicates(subset=["Name","Age","City"], keep='first')
print(df_no_duplicates)