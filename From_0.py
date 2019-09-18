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

# --------------------------------------------------------------- FIRST STEPS WITH PYTHON --------------------------------------------------------

#Declaración de Variables

a = 3
b = 2
c = a + b

Msg1 = 'Good Morning '
Msg2 = 'Vietnam'

Msg = Msg1 + Msg2
print (Msg)

#Borrado de Variables

del (a,b,c)

# %reset -f  # Run only at the console. It cleans the enviroment

# Create a Dataframe for the class

Name = ['Miguel', 'Marta', 'Pau', 'Alberto', 'Diego', 'Jose'] # LIST. It is defined with brackets []
Age = [44, 32, 22, 25, 27, 34] # Another LIST
Gender = ['M', 'F', 'M', 'M', 'M', 'M'] # Another LIST
Nat = ['ES', 'ES', 'ES', 'ES', 'ES', 'ES']

Class_2019_MDA = pd.DataFrame({'Name': Name, 'Age': Age, 'Gender': Gender, 'Nat': Nat}) # DICCIONARIO en la Clase Dataframe de la libreria PANDAS asignada a la variable Class_2019_MDA

del (Name,Age,Gender,Nat)

# Get working directory

os.getcwd()

# Con os.chdir('') Changes the working directory for this script

# Save Dataframe to HD in different formats

Class_2019_MDA.to_excel("FirstDataset.xlsx")
Class_2019_MDA.to_csv("FirstDataset.csv")

print(Class_2019_MDA.Age)

Class_2019_MDA.Age.describe() # Shows different statistics of the DataFrame

plt.hist(Class_2019_MDA.Age) # Shows graphically the data

# ---------------------------------------------- Import the Data from a csv and creating our first BAR CHART -------------------------------------

Rentals_2011_Csv = pd.read_csv("washington_bike_rentals_2011.csv", sep =';' , decimal = ',') 
Rentals_2011_Excel = pd.read_excel("washington_bike_rentals_2011.xlsx") 
Weather_2011_Csv = pd.read_csv("weather_washington_2011.csv", sep = ';', decimal = ',') 


Rentals_2011_Csv.shape  # Shows us the size of the csv data
Rentals_2011_Csv.head() # Shows us the head of the data
Rentals_2011_Csv.tail() # Shows us the end of the data

# Create the variables to plot

Rentals = Rentals_2011_Csv.loc[:, "cnt"]
Holidays = Rentals_2011_Csv.loc[:, "holiday"]

# Plot Rentals Individually

plt.hist(Rentals)
plt.hist(Holidays)

# Statistical Data of the Series

Rentals.describe()
Holidays.describe()

# Shows data types of the data

Weather_2011_Csv.dtypes

# Create the variable to plot

Temperature = Weather_2011_Csv.loc[:, "temp_celsius"] 

# Merge both files by a common index. In this case "day". We get new dataframe of (365,16)

Rentals_Weather_2011 = pd.merge(Rentals_2011_Csv, Weather_2011_Csv, on = "day")

Rentals_Weather_2011 = Rentals_Weather_2011.drop(columns = ['dteday_y']) # Erase duplicated column

Rentals_Weather_2011 = Rentals_Weather_2011.rename(columns = {"dteday_x" : "dteday"}) # Rename one column

# We import 2012 data to merge it with 2011 Data

Rentals_Weather_2012 = pd.read_csv("rentals_weather_2012.csv", sep = ';', decimal = ',') 

Rentals_Weather_2011.shape == Rentals_Weather_2012.shape # We compare data shape and see that there is 1 more file in 2012 because of 29/02/2012

Rental_Weather_2011_2012 = Rentals_Weather_2011.append(Rentals_Weather_2012, ignore_index = True) # We add new data of 2012 to our 2011 data

del (Rentals_Weather_2011, Rentals_Weather_2012, Class_2019_MDA, Holidays, Msg, Msg1, Msg2, Rentals, Rentals_2011_Csv, Rentals_2011_Excel, Temperature, Weather_2011_Csv)  # We erase what we don´t need anymore

# ------------------------------ CREATING AND PLOTTING TEMPERATURE / RENTALS 2011-2012 SCATTER CHART ---------------------------------------------

def Scatter_Temp_Rent():

    wbr = Rental_Weather_2011_2012
    
    TR_x_Axis = wbr.loc[:, "temp_celsius"]
    TR_y_Axis = wbr.loc[:, "cnt"]

    plt.scatter(TR_x_Axis, TR_y_Axis)
    plt.title(label = 'Figure 1.1 - Bike Rental By Temperature 2011-2012')
    plt.xlabel('Temperature Cº')
    plt.ylabel('Bikes Rental')

# -------------------- DESCRIBING A NOMINAL VARIABLE WITH A CROSSTAB (table) IN A FUNCTION  AND PLOTTING A BAR CHART -----------------------------

def CrossTab_WS():

    wbr = Rental_Weather_2011_2012
    
    CT_wbr_Weathersit = pd.crosstab(index = wbr["weathersit"], columns = "Count") # Counts group by

    Sample = CT_wbr_Weathersit.sum() # We Sum the Sample Size for the Weather Situation

    CT_wbr_Weathersit = (CT_wbr_Weathersit/Sample)*100 # We get the %

    plt.bar(CT_wbr_Weathersit.index, CT_wbr_Weathersit['Count']) # We do the bar chart

    WeatherSituation = ('Sunny', 'Cloudy', 'Rainy')

    plt.bar(CT_wbr_Weathersit.index, CT_wbr_Weathersit['Count']) # We do the bar chart again
    plt.xticks(CT_wbr_Weathersit.index, WeatherSituation) # We change the legend

    plt.title(label = 'Figure 1.2 - Weather Situation in Washington')
    plt.ylabel('Percentage %')
    plt.xlabel('Weather Situation')
    props = dict (boxstyle = 'round', facecolor = 'white', lw = 0.5)
    textstr = '$\mathrm{Sample} = %.0f$' %(Sample) # Insert Legend with sample size
    plt.text (2.7,50, textstr, bbox = props) # Paints the Legend in some part of the chart

# GROUP EXERCISE --------------------------- CREATING A BAR CHART WITH HOLIDAY DAYS -------------------------------------------------------------

def BarChart_Holidays():

    wbr = Rental_Weather_2011_2012
     
    Holidays = pd.crosstab(index = wbr["holiday"], columns = "Count")
    Sample = Holidays.sum() # We Sum the Sample Size for the Weather Situation
    
    plt.bar(Holidays.index, Holidays["Count"]) # We do the bar chart
    YN_Holiday = ('Working Days', 'Holiday')  
    plt.xticks(Holidays.index, YN_Holiday)
    plt.title(label = 'Figure 1.3 - Holiday Days')
    plt.ylabel('Days')
    plt.xlabel('Holidays')
    
    props = dict (boxstyle = 'round', facecolor = 'red', lw = 0.5)
    textstr = '$\mathrm{Sample} = %.0f$' %(Sample) # Insert Legend with sample size
    plt.text (0.85,300, textstr, bbox = props) # Paints the Legend in some part of the chart
    
    c = """Day Total
        Work  710
        Holiday  21"""

    df = pd.read_csv(StringIO(c), sep="\s+", header=0)

    print(tabulate(df, headers='keys', tablefmt='psql'))

# GROUP EXERCISE --------------------------- CREATING A PROFESSIONAL HISTOGRAM OF BIKE RENTALS --------------------------------------------------

def Histogram_Cnt():

    wbr = Rental_Weather_2011_2012 
    Rentals = wbr.loc[:, "cnt"]

    print(Rentals.describe())
    
    mu = Rentals.mean()
    sigma = Rentals.std()
    x = wbr.cnt
    num_bins = 50
    
    Sample = Rentals.count()
    
    fig, ax = plt.subplots()
    
    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=1)
    
    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    
    ax.plot(bins, y, '--')
    ax.set_xlabel('Rentals')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Figure 1.4 - Daily Bicycle Rentals in Washington DC ' '\n' 'by Capital BikeShare 2011-2012')
    ax.grid(axis='both', alpha=0.75)
    
    ax.axvline(x=mu, linewidth = 1, linestyle = 'solid', color = "red", label = 'Mean') # Adds Reference line for the Mean
    
    props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
    textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(mu, sigma, Sample)
    ax.text (6600, 0.00022, textstr, bbox = props)
    
    fig.tight_layout()
    plt.show()

# GROUP EXERCISE --------------------------- ANALIZYNG DATES / RENTALS BY CASUALS AND REGISTERED USERS -------------------------------------------

def Cas_Reg_Users():
    
    wbr = Rental_Weather_2011_2012

    wbr['yr'].replace([0, 1], [2011, 2012], inplace = True)
    wbr = wbr.rename(columns = {"yr" : "Year"}) # Rename one column
    wbr = wbr.drop(columns = ['atemp', 'cnt', 'day', 'dteday', 'holiday', 'hum', 'mnth', 'season', 'weathersit', 'weekday', 'windspeed_kh', 'workingday']) # Erase duplicated column
    wbr = wbr.rename(columns = {"casual" : "Casual"}) # Rename one column
    wbr = wbr.rename(columns = {"temp_celsius" : "Mean Temp"}) # Rename one column
    wbr = wbr.rename(columns = {"registered" : "Registered"}) # Rename one column

    CasReg = wbr.groupby(['Year']).agg({'Casual':sum, 'Registered':sum, 'Mean Temp':'mean'})

    ax = CasReg.plot.bar(rot=0)
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Custormers')
    ax.set_title(r'Figure 1.5 - Casual/Reg Users in Washington DC ' '\n' 'by Capital BikeShare 2011-2012')
    ax.grid(axis='both', alpha=0.75)
     
    c = """Casual Registered MeanTemp
        2011  247.252     995.851  19.95
        2012  372.765     1.676.811  20.67"""

    df = pd.read_csv(StringIO(c), sep="\s+", header=0)

    print(tabulate(df, headers='keys', tablefmt='psql'))

# ---------------------------------------------------- MAIN - CALLING SCRIPT FUNCTIONS -----------------------------------------------------------

Scatter_Temp_Rent() # OUR FIRST SCATTER CHART - FIGURE 1.1 - Bike Rental By Temperature 2011-2012
CrossTab_WS()       # OUR FIRST BAR CHART - FIGURE 1.2 - Weather Situation in Washington
BarChart_Holidays() # GROUP EXERCISE HOLIDAYS - FIGURE 1.3 - Holiday Days
Histogram_Cnt()     # GROUP EXERCISE HISTOGRAM CNT - FIGURE 1.4 - Daily Bicycle Rentals in Washington DC by Capital BikeShare 2011-2012
Cas_Reg_Users()     # GROUP EXERCISE EXTRA - FIGURE 1.5 - Casual/Registered Users in 2011-2012





























