import pandas as pd

#Φόρτωση των δεδομένων
df = pd.read_csv(r"C:\Users\zaaaa\OneDrive\Υπολογιστής\New folder\Python Projects\Python Assignement\finance_liquor_sales.csv")

# Μετατροπή της στήλης 'date' σε αντικείμενο datetime
df['date'] = pd.to_datetime(df["date"])

# Εφαρμογή του φίλτρου για τα έτη και επαναφορά του index
filtered_df = df[(df["date"].dt.year >= 2016) & (df["date"].dt.year <= 2019)].reset_index()

# Έλεγχος πληροφοριών και ελλιπών τιμών
filtered_df.info()

#Task A: Distinguishing the most popular type in each postal code

# Ομαδοποίηση και άθροιση των πωληθέντων φιαλών
bottles_sold = filtered_df.groupby(["zip_code", "item_number"])["bottles_sold"].sum().reset_index()

# Εύρεση του δείκτη (index) του μέγιστου για κάθε ομάδα
idx = bottles_sold.groupby("zip_code")["bottles_sold"].idxmax()

# Επιλογή των γραμμών με τις μέγιστες πωλήσεις
max_bottles_sold = bottles_sold.loc[idx].reset_index()

#Οπτικοποίηση: Δημιουργία Γραφήματος
import matplotlib.pyplot as plt

# Ταξινόμηση τιμών και επιλογή των κορυφαίων 20
sorted_values = max_bottles_sold.sort_values(by="bottles_sold", ascending=False).head(20)

# Δημιουργία του γραφήματος
plt.figure(figsize=(12, 7))
plt.bar(sorted_values["zip_code"].astype(str), sorted_values["bottles_sold"], color='skyblue')
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.title("Maximum Bottle Sold per Zip Code")
plt.xticks(rotation=45, ha = "right")
plt.tight_layout()
plt.show()

#Task B:Calculating the percentage of sales per store (in dollars)

# Υπολογισμός συνολικών πωλήσεων
total_sales = filtered_df["sale_dollars"].sum()

# Ομαδοποίηση ανά κατάστημα και άθροιση πωλήσεων
sales_by_store = filtered_df.groupby("store_number")["sale_dollars"].sum().reset_index()   

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

