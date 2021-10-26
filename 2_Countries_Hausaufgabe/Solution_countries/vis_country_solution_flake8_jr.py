# ---------------------------------------------------------------------------
# Description: Solution of the homework 'countries'
# Authors: CS Dojo, Bartels, Schuhmacher, Langer, Ramme
# Copyright: none
# Credits:  https://www.youtube.com/watch?v=a9UrKTVEeZA 13:51
#           CS Dojo
# Python-Version: 3.7.9, flake 8, pep8 Standard
# countries.csv has to be in the same directory
# Version: 3.0.0
# Maintainer: Prof. Hafner
# E-Mail: hafner.sigrid@fh-swf.de
# Status: used in class
# Creation Date: 18.12.2019
# Last Edit: 25.10.2021
#
# ---------------------------------------------------------------------------


# %%
# Cell 1. Import the needed libraries.

# Library Pandas is used to read the data
import pandas as pd

# matplotlib is used to visualize images and graphs
from matplotlib import pyplot as plt

print('\nCell 1 done. Libraries loaded.')

# %%
# Cell 2. Read the data.
# The file 'country.csv' has to be in the same directory.

data = pd.read_csv('countries.csv',)

# Show the input data
print(data)

print('Cell 2 done. Printed image data')


# %%
# Cell 3. Filter the data

india = data[data.country == "India"]
china = data[data.country == "China"]
nigeria = data[data.country == "Nigeria"]
germany = data[data.country == "Germany"]

# Show the selected data
print(india)
print(china)
print(nigeria)
print(germany)
print('Cell 3 done. Filter the data')


# %%
# Cell 4. Plot the population of the selected countries.

plt.plot(india.year, india.population / 10 ** 6)
plt.plot(china.year, china.population / 10 ** 6)
plt.plot(nigeria.year, nigeria.population / 10 ** 6)
plt.plot(germany.year, germany.population / 10 ** 6)

# Set the settings of the plot
plt.legend(["China", "India", "Nigeria in Africa", "Germany"])
plt.xlabel("year")
plt.ylabel("population in millions")
plt.title("Fig 1: Population of different countries")
plt.grid(1)

# Visualization of the plot
plt.show

print('\nCell 4 done. Results visualized.')


# %%
# Cell 5. Calculate the growth rate based on 1952
# iloc[0]: first row of the dataset

india_growth = ((india.population / india.population.iloc[0]) - 1) * 100
china_growth = ((china.population / china.population.iloc[0]) - 1) * 100
nigeria_growth = ((nigeria.population / nigeria.population.iloc[0]) - 1) * 100
germany_growth = ((germany.population / germany.population.iloc[0]) - 1) * 100

print('\nCell 5 done. Calculate growth rate.')


# %%
# # Cell 6. Plot the growth rate of the selected countries.

plt.plot(india.year, india_growth)
plt.plot(china.year, china_growth)
plt.plot(nigeria.year, nigeria_growth)
plt.plot(germany.year, germany_growth)
plt.legend(["Indien", "China", "Nigeria", "Germany"])
plt.xlabel("year")
plt.title("Fig 2: Growth of Population, Base 1952")
plt.ylabel("Population growth in percent in regard to 1952")
plt.grid(1)
plt.show
