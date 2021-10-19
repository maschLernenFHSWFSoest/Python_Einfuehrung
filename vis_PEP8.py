# ---------------------------------------------------------------------------
# Description: # Einfuehrungsvorlesung in Python, Visualisierung von Daten
# Authors: Schumacher, Bartels, Langer, Loubane, Ramme, Hafner
# Copyright: Free to use
# Credits:
# Version: 1.0.1
# Maintainer: Prof. Hafner
# E-Mail: hafner.sigrid@fh-swf.de
# Status: pep8, done in class
# Creation Date: 16-12-2020
# Last Edit: 19-10-2021 SH
# Python-Version: 3.7.9
# Datei sample_data.csv muss im gleichen Directory liegen.
# Zellen sind alle streng nacheinander auszufuehren von oben nach unten.
# --------------------------------------------------------------------------

# %%
# Loading the libraries

# Pandas for working with tzhe csv file
import pandas as pd

# Matplotlib for plotting the results 
from matplotlib import pyplot as plt

print('Libraries loaded!')

# %%
# Read data from csv fole using Panda, saved as 'sampledata'
sampledata = pd.read_csv("sample_data.csv")

# Outprint the array 'sampledata'
sampledata

print('Reading data was successfull!')

# %%
# Outprint the column 'C'
print('Outprint column c:')

sampledata.column_c



# %%
# Plotting a diagram using Matplotlib 
plt.plot(sampledata.column_a, sampledata.column_b)
plt.plot(sampledata.column_a, sampledata.column_c)
plt.title("Diagramm")
plt.xlabel("x")
plt.ylabel("y")
plt.show

print('Plotting the data was successfull!')
