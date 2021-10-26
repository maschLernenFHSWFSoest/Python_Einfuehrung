# ---------------------------------------------------------------------------
# Schachbrettaufgabe,Berechnung und Ausgabe der Reiskornanzahl auf
# den jeweiligen Feldern, sowie die Gesamtmenge.
#
# Python-Version: 3.7.9, Linter flake 8
#
# Authors: Frau Hafner
# Copyright: Free to use
# Credits: https://www.youtube.com/watch?v=sUmNJZBvR0I s. Gravitar.
# Version: 1.0.0
# Maintainer: Sigrid Hafner
# E-Mail: hafner@fh-swf.de
# Status: use in Class 2020
# Last Edit: 03.05.2021
#  ---------------------------------------------------------------------------

# %%
# Initalisierung der Variable reiskorn_summe
reiskorn_summe = 0

# Das Schachbrett besitzt 64 Felder, in einer for Schleife werden diese Felder
# durchiteriert.
for schachbrett_feld in range(64):
    # Die Summe der Reiskörner auf dem Feld ist 2 potenziert mit der Feldnummer
    reiskorn_feld = 2**schachbrett_feld
    # Die Reiskornzahl des jeweiligen Feldes wird auf
    # die Gesamtsumme aufaddiert.
    reiskorn_summe = reiskorn_summe + reiskorn_feld
    # Ausgabe der Reiskornzahl
    print("Auf Feld: ", schachbrett_feld+1, "sind: ",
          reiskorn_feld, "Reiskörner, in der Summe gibt es: ",
          reiskorn_summe, "Reiskörner")
print('******* Done: Alle Felder wurden berechnet')

