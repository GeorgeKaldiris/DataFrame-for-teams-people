import plotly.express as px

# Λίστες δεδομένων
months = ["Μάρτιος", "Απρίλιος", "Μάιος"]
temperatures = [30, 35, 40]

# Δημιουργία γραμμικού διαγράμματος
fig = px.line(
    x=months,
    y=temperatures,
    title="Θερμοκρασίες Άνοιξης",
    labels={"x": "Μήνες", "y": "Θερμοκρασία (°C)"}
)

# Αλλαγή πλάτους γραμμής και χρώματος
fig.update_traces(line=dict(color="blue", width=5))

# Εμφάνιση διαγράμματος
fig.show()