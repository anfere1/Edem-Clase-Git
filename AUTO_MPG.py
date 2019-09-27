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

Auto_Mpg_Csv = pd.read_csv("auto-mpg.csv", sep =',' , decimal = '.')

Auto_Mpg_Csv.origin = Auto_Mpg_Csv.origin.replace({1:'EEUU', 2:'Europa', 3:'Japón'}) # Changing Data at 'origin' column
Auto_Mpg_Csv.horsepower = Auto_Mpg_Csv.horsepower.replace({'?':0}) # Changing value ? for 0

Auto_Mpg_Csv.describe()
Auto_Mpg_Csv.dtypes

Auto_Mpg_Csv.horsepower = pd.to_numeric(Auto_Mpg_Csv.horsepower)
Auto_Mpg_Csv.horsepower = Auto_Mpg_Csv.horsepower.replace({0:105}) # Changing value 0 for 105 that it´s the mean
Auto_Mpg_Csv.dtypes

# EXTRA EXERCISE --------------------------- CREATING A PROFESSIONAL HISTOGRAM OF MPG CARS -------------------------------------------------------

def Histogram_Mpg():

    data = Auto_Mpg_Csv
    Mpg = Auto_Mpg_Csv.loc[:, "mpg"]

    print(Mpg.describe())
    
    mu = Mpg.mean()
    sigma = Mpg.std()
    x = data.mpg
    num_bins = 50
    
    Sample = Mpg.count()
    
    fig, ax = plt.subplots()
    
    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=1)
    
    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    
    ax.plot(bins, y, '--')
    ax.set_xlabel('Miles Per Galon')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Figure 1.6 - Mileage per gallon performances ' '\n' 'of various cars')
    ax.grid(axis='both', alpha=0.75)
    
    ax.axvline(x=mu, linewidth = 1, linestyle = 'solid', color = "red", label = 'Mean') # Adds Reference line for the Mean
    
    props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
    textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(mu, sigma, Sample)
    ax.text (40, 0.06, textstr, bbox = props)
    
    fig.tight_layout()
    plt.show()

# EXTRA EXERCISE --------------------------- CREATING A PROFESSIONAL HISTOGRAM OF HORSEPOWER CARS -----------------------------------------------

def Histogram_Hp():

    data = Auto_Mpg_Csv
    Hp = Auto_Mpg_Csv.loc[:, "horsepower"]

    print(Hp.describe())
    
    mu = Hp.mean()
    sigma = Hp.std()
    x = data.horsepower
    num_bins = 50

    Sample = Hp.count()
    
    fig, ax = plt.subplots()
    
    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=1)
    
    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    
    ax.plot(bins, y, '--')
    ax.set_xlabel('Horse Power')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Figure 1.7 - Horse Power performances ' '\n' 'of various cars')
    ax.grid(axis='both', alpha=0.75)
    
    ax.axvline(x=mu, linewidth = 1, linestyle = 'solid', color = "red", label = 'Mean') # Adds Reference line for the Mean
    
    props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
    textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(mu, sigma, Sample)
    ax.text (175, 0.020, textstr, bbox = props)
    
    fig.tight_layout()
    plt.show()

# EXTRA EXERCISE --------------------------- DESCRIBING A NOMINAL VARIABLE WITH A CROSSTAB (table) IN A FUNCTION  AND PLOTTING A BAR CHART -----------------------------------------------

def CrossTab_Origin():

    data = Auto_Mpg_Csv
    
    CT_data_Origin = pd.crosstab(index = data["origin"], columns = "Count") # Counts group by

    Sample = CT_data_Origin.sum() # We Sum the Sample Size for the data imported

    CT_data_Origin = (CT_data_Origin/Sample)*100 # We get the %

    plt.bar(CT_data_Origin.index, CT_data_Origin['Count']) # We do the bar chart

    plt.title(label = 'Figure 1.8 - Origin Country of the Vehicles')
    plt.ylabel('Percentage %')
    plt.xlabel('Origin Country')
    props = dict (boxstyle = 'round', facecolor = 'white', lw = 0.5)
    textstr = '$\mathrm{Sample} = %.0f$' %(Sample) # Insert Legend with sample size
    plt.text (1.5,50, textstr, bbox = props) # Paints the Legend in some part of the chart

    c = """Country Mean_Cars
            EEUU    62,56%
            Europa  17,58%     
            Japón  19,85%"""

    df = pd.read_csv(StringIO(c), sep="\s+", header=0)

    print(tabulate(df, headers='keys', tablefmt='psql'))

def CrossTab_Mpg():
    
    data = Auto_Mpg_Csv

    Mpg = data.groupby(['origin']).agg({'mpg':'mean'})
    print(Mpg)
    ax = Mpg.plot.bar(rot=0)
    
    ax.set_xlabel('Origin')
    ax.set_ylabel('Mpg Mean')
    ax.set_title(r'Figure 1.9 - Mpg By Country')
    ax.grid(axis='both', alpha=0.75)
     
    c = """Country Mean_Mpg
        EEUU    20,08
        Europa  27,89     
        Japón  30,45"""

    df = pd.read_csv(StringIO(c), sep="\s+", header=0)

    print(tabulate(df, headers='keys', tablefmt='psql'))

def CrossTab_Hp():
    
    data = Auto_Mpg_Csv

    Hp = data.groupby(['origin']).agg({'horsepower':'mean'})
    
    ax = Hp.plot.bar(rot=0)
    
    ax.set_xlabel('Origin')
    ax.set_ylabel('Horse Power Mean')
    ax.set_title(r'Figure 1.10 - Horse Power By Country')
    ax.grid(axis='both', alpha=0.75)
     
    c = """Country Mean_Horse_Power
        EEUU    118,82
        Europa  81,25     
        Japón  79,83"""

    df = pd.read_csv(StringIO(c), sep="\s+", header=0)

    print(tabulate(df, headers='keys', tablefmt='psql'))

# ---------------------------------------------------- MAIN - CALLING SCRIPT FUNCTIONS -----------------------------------------------------------

Histogram_Mpg()   # EXTRA EXERCISE ANALYZING MPG DATA
Histogram_Hp()    # EXTRA EXERCISE ANALYZING HORSEPOWER DATA
CrossTab_Origin() # EXTRA EXERCISE ANALYZING ORIGIN COUNTRY OF THE CARS
CrossTab_Mpg()    # EXTRA EXERCISE ANALYZING MPG BY COUNTRY
CrossTab_Hp()     # EXTRA EXERCISE ANALYZING HORSE POWER BY COUNTRY














