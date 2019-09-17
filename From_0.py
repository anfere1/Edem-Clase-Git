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

del (Rentals_Weather_2011, Rentals_Weather_2012)  # We erase what we don´t need anymore

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
    
    print (Holidays)
    
    plt.bar(Holidays.index, Holidays["Count"]) # We do the bar chart
    YN_Holiday = ('Working Days', 'Holiday')  
    plt.xticks(Holidays.index, YN_Holiday)
    plt.title(label = 'Figure 1.3 - Holiday Days')
    plt.ylabel('Days')
    plt.xlabel('Holidays')
    props = dict (boxstyle = 'round', facecolor = 'white', lw = 0.5)
    textstr = '$\mathrm{Sample} = %.0f$' %(Sample) # Insert Legend with sample size
    plt.text (0.85,600, textstr, bbox = props) # Paints the Legend in some part of the chart

# GROUP EXERCISE --------------------------- CREATING A PROFESSIONAL HISTOGRAM OF BIKE RENTALS --------------------------------------------------

def Histogram_Cnt():

    wbr = Rental_Weather_2011_2012 
    Rentals = wbr.loc[:, "cnt"]

    print(Rentals.describe())
    
    md = Rentals.mean()
    std = Rentals.std()
    Sample = Rentals.count()
    
    fig, ax = plt.subplots()
    
    plt.hist(Rentals, bins = 'auto', edgecolor = 'black', color='#0504aa', alpha=0.7, rwidth=0.85)
        
    plt.grid(axis='y', alpha=0.75)
    plt.xticks(np.arange(0, 10000, step=1000))
    plt.xlabel('Rentals')
    plt.ylabel('Frecuency')
    plt.title('Figure 1.4 - Daily Bicycle Rentals in Washington DC ' '\n' 'by Capital BikeShare 2011-2012')
        
    props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
    textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(md, std, Sample)
    plt.text (6600, 81, textstr, bbox = props)
    
    plt.axvline(x=md, linewidth = 1, linestyle = 'solid', color = "red", label = 'Mean') # Adds Reference line for the Mean

    y = ((1/(np.sqrt(2*np.pi)*std))*np.exp(-0.5*(1/std*(Rentals - md))**2))
    ax.plot(Rentals, y, '--')    
    fig.tight_layout()
    plt.show()
    
# ---------------------------------------------------- MAIN - CALLING SCRIPT FUNCTIONS ----------------------------------------------------------

Scatter_Temp_Rent() # OUR FIRST SCATTER CHART - FIGURE 1.1 - Bike Rental By Temperature 2011-2012
CrossTab_WS()       # OUR FIRST BAR CHART - FIGURE 1.2 - Weather Situation in Washington
BarChart_Holidays() # GROUP EXERCISE HOLIDAYS - FIGURE 1.3 - Holiday Days
Histogram_Cnt()     # GROUP EXERCISE HISTOGRAM CNT - FIGURE 1.4 - Daily Bicycle Rentals in Washington DC by Capital BikeShare 2011-2012


wbr = Rental_Weather_2011_2012 
Rentals = wbr.loc[:, "cnt"]
    
md = Rentals.mean()
std = Rentals.std()
x = md + std * np.random.randn(731)

print(md)
print(std)
print(x)
    
fig, ax = plt.subplots()

y = ((1/(np.sqrt(2*np.pi)*std))*np.exp(-0.5*(1/std*(bins - md))**2))
ax.plot(std, y, '--')    
fig.tight_layout()
plt.show()
























