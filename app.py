from pathlib import Path
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hormuz Dashboard", layout="wide")
st.title("Hormuz: Economic Impact")

# Legge il CSV dalla cartella che contiene app.py
file_path = Path(__file__).parent / "shipping_demo.csv"
df = pd.read_csv(file_path)

# Converte le date e ordina le osservazioni
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

st.header("Shipping: daily crossings")
st.caption("Dati dimostrativi trascritti dalla schermata, da verificare.")

# Mostra i dati per controllare che siano stati importati
st.dataframe(df)

# Crea il grafico
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df["date"].dt.strftime("%d %b"), df["transits"],
       color="orange")

ax.set_xlabel("Date")
ax.set_ylabel("Number of transits")
ax.set_title("Daily ship crossings")
plt.xticks(rotation=45)
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)
