# ---------------------------------------------------------------------------
# Description: # Einfuehrungsvorlesung in Python,
# Introduction in Python,code pro Folie, PEP 8 Standard
# Authors: Schumacher, Bartels, Langer, Loubane, Hafner
# Copyright: Free to use
# Credits:
# Version: 1.0.1
# Maintainer: Prof. Hafner
# E-Mail: hafner.sigrid@fh-swf.de
# Status: pep8, done in class
# Creation Date: 16-12-2020
# Last Edit: 14-10-2021 SH
# Python-Version: 3.7.9

# !!! Datei sample_data.csv muss im gleichen Directory liegen.

# Zellen sind alle streng nacheinander auszufuehren von oben nach unten.
# --------------------------------------------------------------------------

# %%

# Bibliotheken Einbinden Folie 6
# Bibliotheken müssen vorher durch 3_install_libraries.bat installiert sein.

# pandas zum Datei lesen, super fuer Analyse von Daten
import pandas as pd
# numpy: wissenschaftliches Rechnen (Arrays, Matrizen)
import numpy as np
# matplotlib fuer Vislualisierung 2D und 3D
import matplotlib.pyplot as plt
# seaborn: Visualisierung
import seaborn as sns
# und viele andere

# %%
# *** 1. Aufgabe Hello world ausgeben. Wir bevorzugen single quations
print('Hello world \n')
# Oder String literals in python are surrounded by either
# Single quotation marks, or double quotation marks
print("Hello world \n")


# %%
# *** Folie 7 Variable und Datentypen
counter = 100  # integer
miles = 1000.0   # floatin point
name = "Nils"  # string
cmplx = 10 + 4j  # komplexe Zahl
# Ausgabe aller Variablen
print(counter, miles, name, cmplx)
# Ausgabe des Types aller Variablen
print(type(counter), type(miles), type(name), type(cmplx))


# %%
# *** Folie 8 Direktes Einlesen von der Konsole mit while
# Oben wird erwartet, dass Sie eine Zahl eingeben

n = int(input("Zahl von 1 bis 5:"))
while n < 6:
    print("Wert: ", n)
    n = n+1
print("fertig \n")

# %%
# *** Folie 9 for Schleife Einrueckungen verstehen

for i in range(0, 3):
    print("Wert: ", i)
print("fertig \n")

print("*** *** *** \n")
for i in range(0, 3):
    print("Wert: ", i)
    print("fertig \n")

# %%
# Folie 10 die while Schleife mit break,
# Oben wird erwartet, dass Sie eine Zahl eingeben.

n = int(input("Zahl zwischen 1 und 10 = korrekt eingeben:"))
while(n > 10 or n < 1):
    if n > 10:
        print("Zahl ist zu groß!")
        break
    else:
        print("Zahl ist zu klein!")
        break
else:
    print("n = ", n)
    print("Korrekte Eingabe")

# %%
# Folie 11 Text aus Datei lesen

dataset = pd.read_csv("sample_data.csv")
print(dataset)

print("*** *** ***")
# oder mit Open()
daten_lesen = open("sample_data.csv")
for line in daten_lesen:
    print(line)
daten_lesen.close()

# %%
# Folie 12 Schreiben in eine Datei
daten_lesen = open("sample_data.csv")
daten_schreiben = open("Dateiausgabe_intro_python_course.txt", "w")

for line in daten_lesen:
    print(line.rstrip())
    daten_schreiben.write(line)
    print('\n')
daten_lesen.close()
daten_schreiben.close()

# %%
# Folie 13 Schreiben in eine Datei
with open("sample_data.csv") as fobj_in:
    with open("Dateiausgabe_intro_python_course.txt", "w") as fobj_out:
        for line in fobj_in:
            print(line.rstrip())
            fobj_out.write(line)
            print('\n')
print("Ende des Programms, Danke fürs Mitmachen")
