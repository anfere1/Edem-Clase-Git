# -*- coding: utf-8 -*-

"""

Created on Sat Sep 14 08:26:55 2019
@author: Ander
From 0

"""
# --------------------------------------------------------------- Libraries Importation ----------------------------------------------------------

import os
import pandas as pd # pd it's the 'alias' we will use for pandas
import numpy as np  # np it's the 'alias' we will use for numpy
import matplotlib.pyplot as plt # plt it's the 'alias' we will use for matplotlib
from io import StringIO
from tabulate import tabulate

# ---------------------------------------------- Import the Data from a csv and cleaning  --------------------------------------------------------

abny_pep2019 = pd.read_csv('abny_pep2019.csv',sep=',',decimal='.')

abny_pep2019 = abny_pep2019.drop(columns = ['id','name','host_id','host_name','neighbourhood','latitude','longitude', 'last_review', 'calculated_host_listings_count', 'availability_365'])

abny_pep2019 = abny_pep2019.rename(columns = {'neighbourhood_group':'Neighbourhood', 'room_type':'Room_Type', 'price':'Price', 'minimum_nights':'Min_Nights', 'number_of_reviews':'Reviews','reviews_per_month':'Reviews_Month'})

NeighGroups = abny_pep2019["Neighbourhood"].unique()

abny_pep2019 = abny_pep2019.replace({'Manhatan':'Manhattan'})

NeighGroups = abny_pep2019["Neighbourhood"].unique()

Room_Type = abny_pep2019["Room_Type"].unique()

abny_pep2019 = abny_pep2019.replace({'private room':'Private room'})

Room_Type = abny_pep2019["Room_Type"].unique()

abny_pep2019.drop(abny_pep2019[abny_pep2019.Price <= 0].index, inplace = True)

abny_pep2019.dropna(subset = ['Price'], inplace = True)

del(NeighGroups, Room_Type)

# -------------------- DESCRIBING A NOMINAL VARIABLE WITH A CROSSTAB (table) IN A FUNCTION  AND PLOTTING A BAR CHART -----------------------------

def CrossTab_Neigh():

    wbr = abny_pep2019

    Neigh = wbr.groupby(['Neighbourhood']).agg({'Price':'mean'})

    ax = Neigh.plot.bar(rot=10)
    
    ax.set_xlabel('Neighbourhoods')
    ax.set_ylabel('Median Price')
    ax.set_title('Figure 1.11 - Median Price per Neighbourhood')
    ax.grid(axis='both', alpha=0.75)

def CrossTab_Room():

    wbr = abny_pep2019

    Room = wbr.groupby(['Room_Type']).agg({'Price':'mean'})

    ax = Room.plot.bar(rot=10)
    
    ax.set_xlabel('Room Types')
    ax.set_ylabel('Median Price')
    ax.set_title('Figure 1.12 - Median Price per Room Types')
    ax.grid(axis='both', alpha=0.75)


# ---------------------------------------------------- MAIN - CALLING SCRIPT FUNCTIONS -----------------------------------------------------------

CrossTab_Neigh() # BAR CHART - FIGURE 1.11 - Median Price per Neighbourhood
CrossTab_Room()  # BAR CHART - FIGURE 1.12 - Median Price per Room Types

gp = abny_pep2019.groupby(['Room_Type', 'Neighbourhood'])['Price', 'Min_Nights', 'Reviews', 'Reviews_Month'].mean()
print(gp)

# data to plot
n_groups = 5
Means_Entire = gp.loc['Entire home/apt','Price']
Means_Private = gp.loc['Private room','Price']
Means_Shared = gp.loc['Shared room','Price']

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.70
opacity = 0.8

rects1 = Means_Entire.plot.bar(index, rot = 10, color = 'b', label = 'Entire home/apt')

rects2 = Means_Private.plot.bar(index, rot = 10, color = 'g', label = 'Private room')

rects3 = Means_Shared.plot.bar(index, rot = 10, color = 'r', label = 'Shared room')

plt.xlabel('Neighbourhood')
plt.ylabel('Mean Price')
plt.title('Mean Prices by Room Type and Neighbourhood')
plt.xticks(index)
plt.legend()

plt.tight_layout()
plt.show()

gp.to_excel("abny_pep2019.xlsx")

