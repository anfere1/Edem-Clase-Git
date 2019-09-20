# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:11:59 2019

@author: dafer

Title: Python's exercise. Hey ho! Python!!
"""

#Reset all. This is as magic command that runs only in the console.



#load libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


##########################################################################################
#Working directory
os.getcwd()

#Change working directory
os.chdir('C:/Users/dafer/OneDrive/0-Master_Data_Analytics/0-Bloque1/0-Fundamentos/2-Programación_Estad_Python/3-Workgroup')
os.getcwd()
##########################################################################################
#Read data from CSV file and store it in a dataframe with rentals for the year 2011

rentals_11 = pd.read_csv('washington_bike_rentals_2011.csv',sep=';',decimal=',')

#Quality Control
rentals_11.shape
rentals_11.head()
rentals_11.tail()
#QC OK
##########################################################################################
#Read data from CSV file and store it in a dataframe with rentals for the year 2011

weather_11 = pd.read_csv('weather_washington_2011.csv',sep=';',decimal=',')

#Quality Control
weather_11.shape
weather_11.head()
weather_11.tail()
#QC OK
##########################################################################################
#Merge the two dataframes into a new one
rw_11=pd.merge(weather_11,rentals_11,on='dteday',)

rw_11.shape
rw_11.head()
rw_11.tail()
list(rw_11)

#Delete day_y variable because is duplicated
rw_11=rw_11.drop(columns=['day_y'])

#Rename variable day_y as day
rw_11=rw_11.rename(columns={'day_x':'day'})

##########################################################################################
#Read data from CSV file and store it in a dataframe with rentals for the year 2012

rw_12 = pd.read_csv('rentals_weather_2012.csv',sep=';',decimal=',')

#Quality Control
rw_12.shape
rw_12.head()
rw_12.tail()
list(rw_12)
#QC OK
##########################################################################################
#Append 2012 data to 2011 data 
rw_11_12 = rw_11.append(rw_12,ignore_index=True,sort=True)

rw_11_12.shape
rw_11_12.head()
rw_11_12.tail()
list(rw_11_12)

#Columns order was changed while merginging (now is alphabetical)
#We will reorder it from the original rentals_weather_2011 column order 
rw_11_12 = rw_11_12[rw_11.columns]
##########################################################################################
#Assign data to variables 2011
y11 = rentals_11.loc[:,'cnt']
x11 = weather_11.loc[:,'temp_celsius']

#Print the plot 2011
z11 =  plt.scatter(x11,y11,color='red',edgecolor='black' )
plt.ylabel('Rented bikes')
plt.xlabel('Temperature in celsius')
plt.title('Figure 1. Distribution of rented bikes according to temperature in 2011')
plt.axhspan(3500, 5500, alpha = 0.3)
plt.axvline(x=9,linewidth=1,linestyle='dashed',color="green",label='9 C')
plt.axvline(x=32,linewidth=1,linestyle='dashed',color="green",label='32 C')
plt.legend(loc ='upper left',shadow=True)
plt.savefig('Fig1.jpg')
plt.show()


##########################################################################################
#Assign data to variables 2012
y12 = rw_11_12.loc[366:730,'cnt']
x12 = rw_11_12.loc[366:730,'temp_celsius']

#Print the plot 2012
z12 =  plt.scatter(x12,y12,color='blue',edgecolors='black' )
plt.ylabel('Rented bikes')
plt.xlabel('Temperature in celsius')
plt.title('Figure 2. Distribution of rented bikes according to temperature in 2012')
plt.axhspan(5500, 8000, alpha = 0.3,color='red')
plt.axvline(x=10,linewidth=1,linestyle='dashed',color="green",label='10 C')
plt.axvline(x=32,linewidth=1,linestyle='dashed',color="green",label='32 C')
plt.legend(loc ='upper left',shadow=True)
plt.savefig('Fig2.jpg')
plt.show()

##########################################################################################
#Assign data to variables 2011-2012
y11_12 = rw_11_12.loc[:,'cnt']
x11_12 = rw_11_12.loc[:,'temp_celsius']

#Print the plot 2011-2012
z11_12 =  plt.scatter(x11_12,y11_12,color='green',edgecolors='black' )
plt.ylabel('Rented bikes')
plt.xlabel('Temperature in celsius')
plt.title('Figure 3. Distribution of rented bikes according to temperature')
plt.axhspan(3500, 8000, alpha = 0.3,color='red')
plt.axvline(x=10,linewidth=1,linestyle='dashed',color="green",label='10 C')
plt.axvline(x=32,linewidth=1,linestyle='dashed',color="green",label='32 C')
plt.legend(loc ='upper left',shadow=True)
plt.savefig('Fig3.jpg')
plt.show()

##########################################################################################
#Describing nominal variable - % rented casual bikes casual and registered bikes in work days VS
#% rented casual bikes and registered bikes in holidays

rent_work=0
rent_holi=0
rent_work_cas=0
rent_work_reg=0
rent_holi_cas=0
rent_holi_reg=0

for i in rw_11_12.index:
   if rw_11_12['holiday'][i] == 0:
      rent_work = rent_work + int(rw_11_12['cnt'][i])
      rent_work_cas = rent_work_cas + int(rw_11_12['casual'][i])
      rent_work_reg = rent_work_reg + int(rw_11_12['registered'][i])
   elif rw_11_12['holiday'][i] == 1:
      rent_holi = rent_holi + int(rw_11_12['cnt'][i])
      rent_holi_cas = rent_holi_cas + int(rw_11_12['casual'][i])
      rent_holi_reg = rent_holi_reg + int(rw_11_12['registered'][i])


print (rent_work)
print(rent_work_cas)
print(rent_work_reg)
print (rent_holi)
print(rent_holi_cas)
print(rent_holi_reg)

#percentage rent workinday casual      
prwc = (rent_work_cas/rent_work)*100
print (prwc)

#percentage rent workinday registered      
prwr = 100-prwc
print (prwr)

#percentage rent holiday casual      
prhc = (rent_holi_cas/rent_holi)*100
print (prhc)

#percentage rent holiday registered      
prhr = 100-prhc
print (prhr)

##########################################################################################
#Graphically
#Barchart

N = 2
workdays = (prwr, prhr)
holidays = (prwc, prhc)
ind = np.arange(N)    
width = 0.4       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, workdays, width,edgecolor='black')
p2 = plt.bar(ind, holidays, width,bottom=workdays,edgecolor='black')
plt.ylabel('Percentage by rent type')
plt.title('Figure 4. Rent distribution')
plt.xticks(ind, ('Workday', 'Holiday'))
plt.axhline(y=81.4,linewidth=1,linestyle='dashed',color="green",label='81.4 %')
plt.axhline(y=71.5,linewidth=1,linestyle='dashed',color="green",label='71.5 %')
plt.legend((p1[0], p2[0]), ('Registered', 'Casual'))
plt.savefig('Fig4.jpg')
plt.show()

##########################################################################################
#Graphically
#Histogram of bike rentals

#Firt plot with matplotlib
#Select the caribale to plot
rent = rw_11_12.loc[:,'cnt']

#Generate statics
rent.describe()

mean = rent.mean()
std = rent.std()
n = rent.count()

plt.hist(rent,bins =10,edgecolor='black')

plt.axvline(x=mean,linewidth=1,linestyle='solid',color="red",label='Mean')
plt.axvline(x=mean-std,linewidth=1,linestyle='dashed',color='green',label='M + 1 S.D.')
plt.axvline(x=mean+std,linewidth=1,linestyle='dashed',color='green',label='M - 1 S.D.')
plt.xticks(np.arange(0,10000,step=1000))
plt.title('Figure 5. Daily Bicycle rentals in Washington DC''\n'
          'in period 2011-2012')
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles')

plt.legend(loc ='upper right',bbox_to_anchor =(1.01,1))
props=dict(boxstyle ='round',facecolor='white',lw=0.5)
textstr='$\mathrm{n}=%.0f$'%(n)
plt.text(6650,95,textstr,bbox=props)
plt.savefig('Fig5.jpg')
plt.show()
##########################################################################################
#Describing quantitative by weathersit
#1-Sunny 2-Cloudy 3-Rainny
#Compare data distribution in funtion of weathersitu

rw_sun = rw_11_12[['cnt']][rw_11_12.weathersit.eq(1)]
print(rw_sun)
rw_sun.shape
rw_cld = rw_11_12[['cnt']][rw_11_12.weathersit.eq(2)]
print(rw_cld)
rw_cld.shape
rw_rai = rw_11_12[['cnt']][rw_11_12.weathersit.eq(3)]
print(rw_rai)
rw_rai.shape

#del(rw_ws)
rw_ws = pd.concat([rw_sun,rw_cld], axis=1)
rw_ws = pd.concat([rw_ws,rw_rai], axis=1)

rw_ws_fig=rw_11_12.boxplot(by ='weathersit', column =['cnt'], grid = True) 
fig = rw_ws_fig.get_figure()
fig.savefig('Fig6.jpg')
