import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. CSV laden
# -------------------------------------------------------
df = pd.read_csv(r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv")

# -------------------------------------------------------
# 2. Datumsspalte umwandeln
# -------------------------------------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -------------------------------------------------------
# 3. Ein Jahr auswählen
# -------------------------------------------------------
year = 2013
df_year = df[df["Datum"].dt.year == year].copy()

# -------------------------------------------------------
# 4. Trendlinie (30-Tage Rolling Mean)
# -------------------------------------------------------
df_year["Umsatz_trend"] = df_year["Umsatz"].rolling(window=30, center=True, min_periods=1).mean()

# -------------------------------------------------------
# 5. Plot mit zwei Y-Achsen
# -------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# --- Umsatz ---
ax1.set_xlabel("Datum")
ax1.set_ylabel("Umsatz", color="tab:blue")

# Original Umsatz
ax1.plot(df_year["Datum"], df_year["Umsatz"], color="tab:blue", alpha=0.3, label="Umsatz")

# Trendlinie
ax1.plot(df_year["Datum"], df_year["Umsatz_trend"], 
         color="tab:purple", linewidth=2.5, label="Umsatz-Trend (30T-Glättung)")

ax1.tick_params(axis="y", labelcolor="tab:blue")

# --- Temperatur ---
ax2 = ax1.twinx()
ax2.set_ylabel("Temperatur (°C)", color="tab:red")
ax2.plot(df_year["Datum"], df_year["Temperatur"], color="tab:red", label="Temperatur")
ax2.tick_params(axis="y", labelcolor="tab:red")

# -------------------------------------------------------
# Legende beider Achsen zusammenführen
# -------------------------------------------------------
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title(f"Umsatz & Temperatur im Jahr {year} (inkl. Trend & Wochenenden)")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\user\Documents\Data science\bakery_prediction\1_DatasetCharacteristics\sales_temperature_2013.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. CSV laden
# -------------------------------------------------------
df = pd.read_csv(r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv")

# -------------------------------------------------------
# 2. Datumsspalte umwandeln
# -------------------------------------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -------------------------------------------------------
# 3. Ein Jahr auswählen
# -------------------------------------------------------
year = 2014
df_year = df[df["Datum"].dt.year == year].copy()

# -------------------------------------------------------
# 4. Trendlinie (30-Tage Rolling Mean)
# -------------------------------------------------------
df_year["Umsatz_trend"] = df_year["Umsatz"].rolling(window=30, center=True, min_periods=1).mean()

# -------------------------------------------------------
# 5. Plot mit zwei Y-Achsen
# -------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# --- Umsatz ---
ax1.set_xlabel("Datum")
ax1.set_ylabel("Umsatz", color="tab:blue")

# Original Umsatz
ax1.plot(df_year["Datum"], df_year["Umsatz"], color="tab:blue", alpha=0.3, label="Umsatz")

# Trendlinie
ax1.plot(df_year["Datum"], df_year["Umsatz_trend"], 
         color="tab:purple", linewidth=2.5, label="Umsatz-Trend (30T-Glättung)")

ax1.tick_params(axis="y", labelcolor="tab:blue")

# --- Temperatur ---
ax2 = ax1.twinx()
ax2.set_ylabel("Temperatur (°C)", color="tab:red")
ax2.plot(df_year["Datum"], df_year["Temperatur"], color="tab:red", label="Temperatur")
ax2.tick_params(axis="y", labelcolor="tab:red")

# -------------------------------------------------------
# Legende beider Achsen zusammenführen
# -------------------------------------------------------
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title(f"Umsatz & Temperatur im Jahr {year} (inkl. Trend & Wochenenden)")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\user\Documents\Data science\bakery_prediction\1_DatasetCharacteristics\sales_temperature_2014.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. CSV laden
# -------------------------------------------------------
df = pd.read_csv(r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv")

# -------------------------------------------------------
# 2. Datumsspalte umwandeln
# -------------------------------------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -------------------------------------------------------
# 3. Ein Jahr auswählen
# -------------------------------------------------------
year = 2015
df_year = df[df["Datum"].dt.year == year].copy()

# -------------------------------------------------------
# 4. Trendlinie (30-Tage Rolling Mean)
# -------------------------------------------------------
df_year["Umsatz_trend"] = df_year["Umsatz"].rolling(window=30, center=True, min_periods=1).mean()

# -------------------------------------------------------
# 5. Plot mit zwei Y-Achsen
# -------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# --- Umsatz ---
ax1.set_xlabel("Datum")
ax1.set_ylabel("Umsatz", color="tab:blue")

# Original Umsatz
ax1.plot(df_year["Datum"], df_year["Umsatz"], color="tab:blue", alpha=0.3, label="Umsatz")

# Trendlinie
ax1.plot(df_year["Datum"], df_year["Umsatz_trend"], 
         color="tab:purple", linewidth=2.5, label="Umsatz-Trend (30T-Glättung)")

ax1.tick_params(axis="y", labelcolor="tab:blue")

# --- Temperatur ---
ax2 = ax1.twinx()
ax2.set_ylabel("Temperatur (°C)", color="tab:red")
ax2.plot(df_year["Datum"], df_year["Temperatur"], color="tab:red", label="Temperatur")
ax2.tick_params(axis="y", labelcolor="tab:red")

# -------------------------------------------------------
# Legende beider Achsen zusammenführen
# -------------------------------------------------------
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title(f"Umsatz & Temperatur im Jahr {year} (inkl. Trend & Wochenenden)")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\user\Documents\Data science\bakery_prediction\1_DatasetCharacteristics\sales_temperature_2015.png")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. CSV laden
# -------------------------------------------------------
df = pd.read_csv(r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv")

# -------------------------------------------------------
# 2. Datumsspalte umwandeln
# -------------------------------------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -------------------------------------------------------
# 3. Ein Jahr auswählen
# -------------------------------------------------------
year = 2015
df_year = df[df["Datum"].dt.year == year].copy()

# -------------------------------------------------------
# 4. Trendlinie (30-Tage Rolling Mean)
# -------------------------------------------------------
df_year["Umsatz_trend"] = df_year["Umsatz"].rolling(window=30, center=True, min_periods=1).mean()

# -------------------------------------------------------
# 5. Plot mit zwei Y-Achsen
# -------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# --- Umsatz ---
ax1.set_xlabel("Datum")
ax1.set_ylabel("Umsatz", color="tab:blue")

# Original Umsatz
ax1.plot(df_year["Datum"], df_year["Umsatz"], color="tab:blue", alpha=0.3, label="Umsatz")

# Trendlinie
ax1.plot(df_year["Datum"], df_year["Umsatz_trend"], 
         color="tab:purple", linewidth=2.5, label="Umsatz-Trend (30T-Glättung)")

ax1.tick_params(axis="y", labelcolor="tab:blue")

# --- Temperatur ---
ax2 = ax1.twinx()
ax2.set_ylabel("Temperatur (°C)", color="tab:red")
ax2.plot(df_year["Datum"], df_year["Temperatur"], color="tab:red", label="Temperatur")
ax2.tick_params(axis="y", labelcolor="tab:red")

# -------------------------------------------------------
# Legende beider Achsen zusammenführen
# -------------------------------------------------------
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title(f"Umsatz & Temperatur im Jahr {year} (inkl. Trend & Wochenenden)")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\user\Documents\Data science\bakery_prediction\1_DatasetCharacteristics\sales_temperature_2016.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. CSV laden
# -------------------------------------------------------
df = pd.read_csv(r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv")

# -------------------------------------------------------
# 2. Datumsspalte umwandeln
# -------------------------------------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -------------------------------------------------------
# 3. Ein Jahr auswählen
# -------------------------------------------------------
year = 2016
df_year = df[df["Datum"].dt.year == year].copy()

# -------------------------------------------------------
# 4. Trendlinie (30-Tage Rolling Mean)
# -------------------------------------------------------
df_year["Umsatz_trend"] = df_year["Umsatz"].rolling(window=30, center=True, min_periods=1).mean()

# -------------------------------------------------------
# 5. Plot mit zwei Y-Achsen
# -------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# --- Umsatz ---
ax1.set_xlabel("Datum")
ax1.set_ylabel("Umsatz", color="tab:blue")

# Original Umsatz
ax1.plot(df_year["Datum"], df_year["Umsatz"], color="tab:blue", alpha=0.3, label="Umsatz")

# Trendlinie
ax1.plot(df_year["Datum"], df_year["Umsatz_trend"], 
         color="tab:purple", linewidth=2.5, label="Umsatz-Trend (30T-Glättung)")

ax1.tick_params(axis="y", labelcolor="tab:blue")

# --- Temperatur ---
ax2 = ax1.twinx()
ax2.set_ylabel("Temperatur (°C)", color="tab:red")
ax2.plot(df_year["Datum"], df_year["Temperatur"], color="tab:red", label="Temperatur")
ax2.tick_params(axis="y", labelcolor="tab:red")

# -------------------------------------------------------
# Legende beider Achsen zusammenführen
# -------------------------------------------------------
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title(f"Umsatz & Temperatur im Jahr {year} (inkl. Trend & Wochenenden)")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\user\Documents\Data science\bakery_prediction\1_DatasetCharacteristics\sales_temperature_2016.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. CSV laden
# -------------------------------------------------------
df = pd.read_csv(r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv")

# -------------------------------------------------------
# 2. Datumsspalte umwandeln
# -------------------------------------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -------------------------------------------------------
# 3. Ein Jahr auswählen
# -------------------------------------------------------
year = 2017
df_year = df[df["Datum"].dt.year == year].copy()

# -------------------------------------------------------
# 4. Trendlinie (30-Tage Rolling Mean)
# -------------------------------------------------------
df_year["Umsatz_trend"] = df_year["Umsatz"].rolling(window=30, center=True, min_periods=1).mean()

# -------------------------------------------------------
# 5. Plot mit zwei Y-Achsen
# -------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# --- Umsatz ---
ax1.set_xlabel("Datum")
ax1.set_ylabel("Umsatz", color="tab:blue")

# Original Umsatz
ax1.plot(df_year["Datum"], df_year["Umsatz"], color="tab:blue", alpha=0.3, label="Umsatz")

# Trendlinie
ax1.plot(df_year["Datum"], df_year["Umsatz_trend"], 
         color="tab:purple", linewidth=2.5, label="Umsatz-Trend (30T-Glättung)")

ax1.tick_params(axis="y", labelcolor="tab:blue")

# --- Temperatur ---
ax2 = ax1.twinx()
ax2.set_ylabel("Temperatur (°C)", color="tab:red")
ax2.plot(df_year["Datum"], df_year["Temperatur"], color="tab:red", label="Temperatur")
ax2.tick_params(axis="y", labelcolor="tab:red")

# -------------------------------------------------------
# Legende beider Achsen zusammenführen
# -------------------------------------------------------
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title(f"Umsatz & Temperatur im Jahr {year} (inkl. Trend & Wochenenden)")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\user\Documents\Data science\bakery_prediction\1_DatasetCharacteristics\sales_temperature_2017.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. CSV laden
# -------------------------------------------------------
df = pd.read_csv(r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv")

# -------------------------------------------------------
# 2. Datumsspalte umwandeln
# -------------------------------------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -------------------------------------------------------
# 3. Ein Jahr auswählen
# -------------------------------------------------------
year = 2018
df_year = df[df["Datum"].dt.year == year].copy()

# -------------------------------------------------------
# 4. Trendlinie (30-Tage Rolling Mean)
# -------------------------------------------------------
df_year["Umsatz_trend"] = df_year["Umsatz"].rolling(window=30, center=True, min_periods=1).mean()

# -------------------------------------------------------
# 5. Plot mit zwei Y-Achsen
# -------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# --- Umsatz ---
ax1.set_xlabel("Datum")
ax1.set_ylabel("Umsatz", color="tab:blue")

# Original Umsatz
ax1.plot(df_year["Datum"], df_year["Umsatz"], color="tab:blue", alpha=0.3, label="Umsatz")

# Trendlinie
ax1.plot(df_year["Datum"], df_year["Umsatz_trend"], 
         color="tab:purple", linewidth=2.5, label="Umsatz-Trend (30T-Glättung)")

ax1.tick_params(axis="y", labelcolor="tab:blue")

# --- Temperatur ---
ax2 = ax1.twinx()
ax2.set_ylabel("Temperatur (°C)", color="tab:red")
ax2.plot(df_year["Datum"], df_year["Temperatur"], color="tab:red", label="Temperatur")
ax2.tick_params(axis="y", labelcolor="tab:red")

# -------------------------------------------------------
# Legende beider Achsen zusammenführen
# -------------------------------------------------------
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title(f"Umsatz & Temperatur im Jahr {year} (inkl. Trend & Wochenenden)")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\user\Documents\Data science\bakery_prediction\1_DatasetCharacteristics\sales_temperature_2018.png")
plt.show()

from PIL import Image

# Liste der Bilddateien mit vollständigem Pfad
images = [Image.open(r"C:\Users\user\Documents\Data science\bakery_prediction\Plots\sales_temperature_2013.png"),
          Image.open(r"C:\Users\user\Documents\Data science\bakery_prediction\Plots\sales_temperature_2014.png"),
          Image.open(r"C:\Users\user\Documents\Data science\bakery_prediction\Plots\sales_temperature_2015.png"),
          Image.open(r"C:\Users\user\Documents\Data science\bakery_prediction\Plots\sales_temperature_2016.png"),
          Image.open(r"C:\Users\user\Documents\Data science\bakery_prediction\Plots\sales_temperature_2017.png"),
          Image.open(r"C:\Users\user\Documents\Data science\bakery_prediction\Plots\sales_temperature_2018.png")]
# Bestimme Größe eines Bildes
width, height = images[0].size

# Collage-Größe: 2 Reihen x 3 Spalten
collage = Image.new('RGB', (3*width, 2*height))

# Bilder einfügen
collage.paste(images[0], (0,0))
collage.paste(images[1], (width,0))
collage.paste(images[2], (2*width,0))
collage.paste(images[3], (0,height))
collage.paste(images[4], (width,height))
collage.paste(images[5], (2*width,height))

# Speichern
collage.save("collage_final.png")


# over the years averages
# total monthly averages
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. CSV laden
# -----------------------------
file_path = r"C:\Users\user\Documents\Data science\bakery_prediction\0_DataPreparation\Processed\merged_data.csv"
df = pd.read_csv(file_path)

# -----------------------------
# 2. Datum in datetime
# -----------------------------
df["Datum"] = pd.to_datetime(df["Datum"])

# -----------------------------
# 3. Jahr und Monat extrahieren
# -----------------------------
df["Jahr"] = df["Datum"].dt.year
df["Monat"] = df["Datum"].dt.month

# -----------------------------
# 4. Durchschnitt pro Monat & Jahr berechnen
# -----------------------------
df_monthly = df.groupby(["Jahr", "Monat"]).agg({
    "Umsatz": "mean",
    "Temperatur": "mean"
}).reset_index()

# -----------------------------
# 5. Gleitende Trendlinie Umsatz
# -----------------------------
window_size = 3  # 3-Monats-Durchschnitt
df_monthly["Umsatz_trend"] = df_monthly["Umsatz"].rolling(window=window_size, min_periods=1, center=True).mean()

# -----------------------------
# 6. X-Achse vorbereiten (Monat-Jahr)
# -----------------------------
df_monthly["Monat_Jahr"] = df_monthly["Jahr"].astype(str) + "-" + df_monthly["Monat"].astype(str).str.zfill(2)

# -----------------------------
# 7. Plot
# -----------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))

# Umsatz Trendlinie (linke Y-Achse)
ax1.plot(df_monthly["Monat_Jahr"], df_monthly["Umsatz_trend"], color="blue", label="Umsatz Trend", marker="o")
ax1.set_xlabel("Monat-Jahr")
ax1.set_ylabel("Umsatz", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.set_xticks(df_monthly["Monat_Jahr"][::max(1, len(df_monthly)//20)])  # nur ca. 20 X-Ticks
ax1.set_xticklabels(df_monthly["Monat_Jahr"][::max(1, len(df_monthly)//20)], rotation=45)

# Temperatur (rechte Y-Achse)
ax2 = ax1.twinx()
ax2.plot(df_monthly["Monat_Jahr"], df_monthly["Temperatur"], color="red", label="Temperatur", marker="s")
ax2.set_ylabel("Temperatur", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Legende kombinieren
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title("Monatlich aggregierter Umsatz & Temperatur über alle Jahre")
plt.grid(True)
plt.tight_layout()
plt.show()
