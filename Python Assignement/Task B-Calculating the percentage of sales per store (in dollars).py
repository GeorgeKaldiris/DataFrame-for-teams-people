import pandas as pd

#Φόρτωση των δεδομένων
df = pd.read_csv(r"C:\Users\zaaaa\OneDrive\Υπολογιστής\New folder\Python Projects\Python Assignement\finance_liquor_sales.csv")

# Μετατροπή της στήλης 'date' σε αντικείμενο datetime
df['date'] = pd.to_datetime(df["date"])

# Εφαρμογή του φίλτρου για τα έτη και επαναφορά του index
filtered_df = df[(df["date"].dt.year >= 2016) & (df["date"].dt.year <= 2019)].reset_index()

# Έλεγχος πληροφοριών και ελλιπών τιμών
filtered_df.info()

#Task B:Calculating the percentage of sales per store (in dollars)

# Υπολογισμός συνολικών πωλήσεων
total_sales = filtered_df["sale_dollars"].sum()

# Ομαδοποίηση ανά κατάστημα και άθροιση πωλήσεων
sales_by_store = filtered_df.groupby("store_name")["sale_dollars"].sum()   

# Υπολογισμός ποσοστού
percentage_sales = (sales_by_store * 100) / total_sales.round(2)

# Οπτικοποίηση: Παρουσίαση Αποτελεσμάτων
import matplotlib.pyplot as plt

# Επιλογή των κορυφαίων 15 καταστημάτων
top_15_stores = percentage_sales.sort_values(ascending=False).head(15)

# Δημιουργία του γραφήματος
plt.figure(figsize=(12, 8))
p = plt.barh(top_15_stores.index, top_15_stores.values, color='lightcoral')
plt.xlabel("Ποσοστό Πωλήσεων (%)")
plt.title("Ποσοστό Πωλήσεων ανά Κατάστημα (Top 15)")
plt.gca().invert_yaxis() # Για να είναι το κορυφαίο στην κορυφή
plt.bar_label(p, fmt="%.2f%%")
plt.tight_layout()
plt.show()