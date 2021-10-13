# ---------------------------------------------------------------------------
# Description: # Einfuehrungsvorlesung in Python, Visualisierung von Daten
# Authors: Schumacher, Bartels, Langer, Loubane, Ramme, Hafner
# Copyright: Free to use
# Credits:
# Version: 1.0.0
# Maintainer: Prof. Hafner
# E-Mail: hafner.sigrid@fh-swf.de
# Status: pep8, done in class
# Creation Date: 16-12-2020
# Last Edit: 13-10-2021 JR
# Python-Version: 3.7.9
# Datei sample_data.csv muss im gleichen Directory liegen.
# Zellen sind alle streng nacheinander auszufuehren von oben nach unten.
# --------------------------------------------------------------------------

# %%
# Cell 1: Libraries

# Libaries einbinden
import pandas as pd
from matplotlib import pyplot as plt
print('Libraries loaded')

# %%
# Cell 2: Daten einlesen
# Pfad muss korrekt sein
# sampledata = pd.read_csv(r"VSCode\sample_data.csv")
sampledata = pd.read_csv("sample_data.csv")

# Daten als Tabelle ausgeben
sampledata

print('Cell 2 done.')

# %%
# Cell 3
# Nur Spalte C ausgeben
sampledata.column_c

print('Cell 3 done.')

# %%
# Cell 4
# Graph erstellen Spalte b über a und c über a
plt.plot(sampledata.column_a, sampledata.column_b)
plt.plot(sampledata.column_a, sampledata.column_c)
plt.title("Diagramm")
plt.xlabel("x")
plt.ylabel("y")
plt.show
print('Cell 3 done.')
