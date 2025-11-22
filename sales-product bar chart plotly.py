# Εισαγωγή των βιβλιοθήκων
import plotly.graph_objects as go
import pandas as pd

# Δημιουργία ενός λεξικού με δεδομένα πωλήσεων για τέσσερα προϊόντα
data = {
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Sales": [2000, 2500, 1800, 2200],
}

# Μετατροπή του λεξικού σε pandas DataFrame
df = pd.DataFrame(data)

# Δημιουργία ενός νέου αντικειμένου plotly Figure
fig = go.Figure()

# Προσθήκη ενός ίχνους ράβδου στο σχήμα
fig.add_trace(
    go.Bar(
        x=df["Product"],
        y=df["Sales"],
        text=df["Sales"],
        textposition="auto",
        marker_color=["blue", "red", "green", "purple"],
    )
)

# Ενημέρωση της διάταξης του σχήματος
fig.update_layout(
    title="Sales in 2020",
    xaxis_title="Product",
    yaxis_title="Sales",
    plot_bgcolor="rgba(0, 0, 0, 0)",
    hovermode="x unified",
)

# Εμφάνισει του σχήματος
fig.show()