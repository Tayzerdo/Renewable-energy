# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:48:04 2020

@author: tayze
"""

#Excel file link is
#https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/xlsx/energy-economics/statistical-review/bp-stats-review-2019-all-data.xlsx

###0 Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas import ExcelWriter

print('libraries imported')

### 1. Takw all places, countries and regions
#Take the Places
Places = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Primary Energy Consumption', skiprows = 2)
Places.rename(columns={'Million tonnes oil equivalent':'Countries'}, inplace =True)
Places.set_index('Countries', inplace=True)
Places = Places.iloc[:Places.index.get_loc('Total World')]
Places.dropna(how='all', axis=0, inplace=True)
Places = Places.index

#Take the countries
Countries = Places[~Places.str.startswith('Total')]

#Countries in Total North America
North_America = Places[:Places.get_loc('Total North America')]
#Countries in Total S. & Cent. America
Cent_America = Places[Places.get_loc('Total North America')+1:Places.get_loc('Total S. & Cent. America')]
#Countries in Total Europe
Europe = Places[Places.get_loc('Total S. & Cent. America')+1:Places.get_loc('Total Europe')]
#Countries in Total CIS
CIS = Places[Places.get_loc('Total Europe')+1:Places.get_loc('Total CIS')]
#Countries in Total Middle East
Middle_East = Places[Places.get_loc('Total CIS')+1:Places.get_loc('Total Middle East')]
#Countries in Total Africa
Africa = Places[Places.get_loc('Total Middle East')+1:Places.get_loc('Total Africa')]
#Countries in Total Asia Pacific
Asia_Pacific = Places[Places.get_loc('Total Africa')+1:Places.get_loc('Total Asia Pacific')]
#Countries by region
Countries_Region = [North_America,Cent_America,Europe,CIS,Middle_East,Africa,Asia_Pacific]


#Take the regions
Regions = Places[Places.str.startswith('Total')]

#### 2. Import energy data
#Import the Oil production data
Oil = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Oil Production - Tonnes', skiprows = 2)
Oil.rename(columns={'Million tonnes':'Countries'}, inplace =True)
Oil.set_index('Countries', inplace=True)
Oil.dropna(how='all', axis=0, inplace=True)
Oil.dropna(how='all', axis=1, inplace=True)
Oil.fillna(0, inplace=True)
Oil = Oil.iloc[:Oil.index.get_loc('Total World'),:Oil.columns.get_loc(2018)+1]

#Import the Gas production data
Gas = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Gas Production - Mtoe', skiprows = 2)
Gas.rename(columns={'Million tonnes oil equivalent':'Countries'}, inplace =True)
Gas.set_index('Countries', inplace=True)
Gas.dropna(how='all', axis=0, inplace=True)
Gas.dropna(how='all', axis=1, inplace=True)
Gas.fillna(0, inplace=True)
Gas = Gas.iloc[:Gas.index.get_loc('Total World'),:Gas.columns.get_loc(2018)+1]

#Import Coal Production data 
Coal = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Coal Production - Mtoe', skiprows = 2)
Coal.rename(columns={'Million tonnes oil equivalent':'Countries'}, inplace =True)
Coal.set_index('Countries', inplace=True)
Coal.dropna(how='all', axis=0, inplace=True)
Coal.dropna(how='all', axis=1, inplace=True)
Coal.fillna(0, inplace=True)
Coal = Coal.iloc[:Coal.index.get_loc('Total World'),:Coal.columns.get_loc(2018)+1]

#Import the nuclear generation
Nuclear = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Nuclear Generation - TWh', skiprows = 2)
Nuclear.rename(columns={'Terawatt-hours':'Countries'}, inplace =True)
Nuclear.set_index('Countries', inplace=True)
Nuclear.dropna(how='all', axis=0, inplace=True)
Nuclear.dropna(how='all', axis=1, inplace=True)
Nuclear.fillna(0, inplace=True)
Nuclear = Nuclear.iloc[:Nuclear.index.get_loc('Total World'),:Nuclear.columns.get_loc(2018)+1]

#Import the hydro generation data
Hydro = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Hydro Generation - TWh', skiprows = 2)
Hydro.rename(columns={'Terawatt-hours':'Countries'}, inplace =True)
Hydro.set_index('Countries', inplace=True)
Hydro.dropna(how='all', axis=0, inplace=True)
Hydro.dropna(how='all', axis=1, inplace=True)
Hydro.fillna(0, inplace=True)
Hydro = Hydro.iloc[:Hydro.index.get_loc('Total World'),:Hydro.columns.get_loc(2018)+1]

#Import the solar generation data
Solar = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Solar Generation - TWh', skiprows = 2)
Solar.rename(columns={'Terawatt-hours':'Countries'}, inplace =True)
Solar.set_index('Countries', inplace=True)
Solar.dropna(how='all', axis=0, inplace=True)
Solar.dropna(how='all', axis=1, inplace=True)
Solar.fillna(0, inplace=True)
Solar = Solar.iloc[:Solar.index.get_loc('Total World'),:Solar.columns.get_loc(2018)+1]

#Import the Wind energy generation data
Wind = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Wind Generation - TWh ', skiprows=2)
Wind.rename(columns={'Terawatt-hours':'Countries'}, inplace =True)
Wind.set_index('Countries', inplace=True)
Wind.dropna(how='all', axis=0, inplace=True)
Wind.dropna(how='all', axis=1, inplace=True)
Wind.fillna(0,inplace=True)
Wind = Wind.iloc[:Wind.index.get_loc('Total World'),:Wind.columns.get_loc(2018)+1]

#Import the Biofuel energy generation data
Biofuel = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Biofuels Production - Ktoe', skiprows=2)
Biofuel.rename(columns={'Thousand tonnes oil equivalent':'Countries'}, inplace =True)
Biofuel.set_index('Countries', inplace=True)
Biofuel.dropna(how='all', axis=0, inplace=True)
Biofuel.dropna(how='all', axis=1, inplace=True)
Biofuel.fillna(0,inplace=True)
Biofuel = Biofuel.iloc[:Biofuel.index.get_loc('Total World'),:Biofuel.columns.get_loc(2018)+1]

#Import the Other energy generation data
Other = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Geo Biomass Other - TWh', skiprows = 2)
Other.rename(columns={'Terawatt-hours':'Countries'}, inplace =True)
Other.set_index('Countries', inplace=True)
Other.dropna(how='all', axis=0, inplace=True)
Other.dropna(how='all', axis=1, inplace=True)
Other.fillna(0, inplace=True)
Other = Other.iloc[:Other.index.get_loc('Total World'),:Other.columns.get_loc(2018)+1]

#Import the Carbon Dioxe data
Carbon = pd.read_excel('bp-stats-review-2019-all-data.xls', sheet_name = 'Carbon Dioxide Emissions', skiprows = 2)
Carbon.rename(columns={'Million tonnes of carbon dioxide':'Countries'}, inplace =True)
Carbon.set_index('Countries', inplace=True)
Carbon.dropna(how='all', axis=0, inplace=True)
Carbon.dropna(how='all', axis=1, inplace=True)
Carbon.fillna(0, inplace=True)
Carbon = Carbon.iloc[:Carbon.index.get_loc('Total World'),:Carbon.columns.get_loc(2018)+1]

#Save the Carbon emission graph for each country
for i in Countries:
    a=Carbon.loc[i].transpose()
    a.plot(kind='line')
    plt.title('Carbon Emission for {}'.format(i))
    plt.xlabel('Years')
    plt.ylabel('Carbon Emission (Million tonnes)')
    #plt.show()
    plt.savefig(f"Carbon Emission {i}.png",dpi=150,bbox_inches='tight')
    plt.clf()
    

#C:\Users\tayze\Documents\Project\BP_Stats_Review\Comparison\CarbonEmission


### 3. Create energy data variables
Energy_type = [Oil, Gas, Coal, Nuclear, Hydro, Solar, Wind, Biofuel, Other, Carbon]
energy = ["Oil","Gas","Coal","Nuclear","Hydro","Solar", "Wind", "Biofuel", "Other", "Carbon"]

#Create a dict to correlate the Energy with specific color
color = ['blue', 'orange', 'green', 'red','purple', 'brown', 'cyan', 'black', 'gray', 'olive']
dicts = {}
for i in range(0,len(energy)):
    dicts[energy[i]] = color[i]

### 5. Correlation table
#Create the correlation table for all the countries
a = pd.DataFrame([])
m=0
for j in Countries:
    type_energy = []
    n=0
    Table = []
    for i in Energy_type:
        try:
            Table.append(i.loc[j])
            type_energy.append(energy[n])
        except KeyError:
            pass
            #print(f"{j} don't have information of {energy[n]}")

        n+=1

    Table=pd.DataFrame(Table)
    Table.index=type_energy
    Table = Table[(Table.T != 0).any()]
    Table=Table.transpose()
    x = Table.corr()
    x = x.tail(1)
    x.replace({1.0:j}, inplace=True)
    a = a.append(x)
    m+=1

#Set the correlation with Carbon for each country
a.rename(columns={'Carbon':'Countries'}, inplace =True)

#Build the corr table
Countries_corr=a.set_index('Countries')

#Append the Regions on the table by country checking the name of the country inside the region
y = []

for i in range(0,len(Countries)):
    if a.iloc[i,1] in Countries_Region[0]:
        y.append(Regions[0])
    elif a.iloc[i,1] in Countries_Region[1]:
        y.append(Regions[1])
    elif a.iloc[i,1] in Countries_Region[2]:
        y.append(Regions[2])
    elif a.iloc[i,1] in Countries_Region[3]:
        y.append(Regions[3])
    elif a.iloc[i,1] in Countries_Region[4]:
        y.append(Regions[4])
    elif a.iloc[i,1] in Countries_Region[5]:
        y.append(Regions[5])
    elif a.iloc[i,1] in Countries_Region[6]:
        y.append(Regions[6])

a['Regions'] = y

a.set_index('Regions',inplace=True)
a.to_csv('table.xlsx')
Total_Countries_Corr = a

### 5. Correlation graphs for each energy type using scatter plots
#Create the x axis
x = np.arange(-1.00,1.10,0.25)

#Create the scatter plot with the correlation for all the regions
b=a.drop('Countries',axis=1)
for i in range(0,len(b.columns)):
    plt.scatter(b.iloc[:,i],b.index, alpha=0.5)
    plt.legend(energy,bbox_to_anchor=(1.02,1.025), loc="upper left")
    plt.title('Energy correlation with Carbon Emission')
    #plt.show()
    plt.savefig('Energy correlation with Carbon Emission.png',dpi=150,bbox_inches='tight')

#Create the scatter plot for type of energy with the correlation for all the regions
for j in range(0,len(energy)-1):
    print(j)
    plt.scatter(b[energy[j]],b.index, alpha=0.5, c=dicts[energy[j]])
    plt.title(f'{energy[i]} correlation with Carbon Emission')
    plt.xticks(x)
    #plt.show()
    plt.savefig(f'Scatter plot {energy[i]}.png',dpi=150,bbox_inches='tight')
    plt.clf()


### 6. Correlation graphs for each region using heatmap
#Save the Corr tables in Excel
Total_Countries_Corr.rename(columns={'Carbon':'Countries'},inplace=True)

North_America_Corr=Total_Countries_Corr.loc[Regions[0]]
Cent_America_Corr=Total_Countries_Corr.loc[Regions[1]]
Europe_Corr=Total_Countries_Corr.loc[Regions[2]]
CIS_Corr=Total_Countries_Corr.loc[Regions[3]]
Middle_East_Corr=Total_Countries_Corr.loc[Regions[4]]
Africa_Corr=Total_Countries_Corr.loc[Regions[5]]
Asia_Pacific_Corr=Total_Countries_Corr.loc[Regions[6]]

Countries_Region_Corr = [North_America_Corr,Cent_America_Corr,Europe_Corr,CIS_Corr,Middle_East_Corr,Africa_Corr,Asia_Pacific_Corr]

#Create an excel with the information
with ExcelWriter('Countries_Corr.xlsx', mode='w') as writer:
    for i in range(0,len(Regions)):
        c=Countries_Region_Corr[i]
        c.set_index('Countries',inplace=True)
        c=c.astype(float).round(3)        
        c.to_excel(writer, '%s' % Regions[i])

#Heatmap of North America region
corrmap=North_America_Corr.fillna(0)
corrmap.sort_values('Countries', inplace=True)
f, ax = plt.subplots(figsize=(7,1)) 
sns.heatmap(corrmap, cmap ="RdBu_r", linewidths = 0.001, linecolor='black', vmin=-1, vmax=1, annot=True, fmt=".2g", cbar=False)
plt.yticks(rotation=0, fontsize="10", va="center")
plt.tick_params(axis='x', which='major', labelsize=10, labelbottom = True, bottom=True, top = False, labeltop=False)
bottom,top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
plt.title('{} correlation heatmap with Carbon emission'.format(Regions[0][5:]), fontsize="12")
ax.set_ylabel('') 
#plt.show()
plt.savefig("Heat map North_America_Corr.png",dpi=150,bbox_inches='tight')

#Heatmap of Central/South America region
corrmap=Cent_America_Corr.fillna(0)
corrmap.sort_values('Countries', inplace=True)
f, ax = plt.subplots(figsize=(7,4)) 
sns.heatmap(corrmap, ax = ax, cmap ="RdBu_r", linecolor='black', vmin=-1, vmax=1, annot=True, fmt=".2g", cbar=False, mask=(corrmap==0))
plt.yticks(rotation=0, fontsize="10", va="center")
plt.tick_params(axis='x', which='major', labelsize=10, labelbottom = True, bottom=True, top = False, labeltop=False)
bottom,top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
plt.title('{} correlation heatmap with Carbon emission'.format(Regions[1][5:]), fontsize="12")
ax.set_ylabel('') 
#plt.show()
plt.savefig("Heat map Cent_America_Corr.png",dpi=150,bbox_inches='tight')

#Heatmap of Europe region
corrmap=Europe_Corr.fillna(0)
corrmap.sort_values('Countries', inplace=True)
f, ax = plt.subplots(figsize=(7,12)) 
sns.heatmap(corrmap, ax = ax, cmap ="RdBu_r", linecolor='black', vmin=-1, vmax=1, annot=True, fmt=".2g", cbar=False, mask=(corrmap==0))
plt.yticks(rotation=0, fontsize="10", va="center")
plt.tick_params(axis='x', which='major', labelsize=10, labelbottom = True, bottom=True, top = False, labeltop=False)
bottom,top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
plt.title('{} correlation heatmap with Carbon emission'.format(Regions[2][5:]), fontsize="12")
ax.set_ylabel('') 
#plt.show()
plt.savefig("Heat map Europe_Corr.png",dpi=150,bbox_inches='tight')

#Heatmap of CIS region
corrmap=CIS_Corr.fillna(0)
corrmap.sort_values('Countries', inplace=True)
f, ax = plt.subplots(figsize=(7,4)) 
sns.heatmap(corrmap, ax = ax, cmap ="RdBu_r",  linecolor='black', vmin=-1, vmax=1, annot=True, fmt=".2g", cbar=False, mask=(corrmap==0))
plt.yticks(rotation=0, fontsize="10", va="center")
plt.tick_params(axis='x', which='major', labelsize=10, labelbottom = True, bottom=True, top = False, labeltop=False)
bottom,top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
plt.title('{} correlation heatmap with Carbon emission'.format(Regions[3][5:]), fontsize="12")
ax.set_ylabel('') 
#plt.show()
plt.savefig("Heat map CIS_Corr.png",dpi=150,bbox_inches='tight')

#Heatmap of Middle East region
corrmap=Middle_East_Corr.fillna(0)
corrmap.sort_values('Countries', inplace=True)
f, ax = plt.subplots(figsize=(7,4)) 
sns.heatmap(corrmap, ax = ax, cmap ="RdBu_r",  linecolor='black',  vmin=-1, vmax=1, annot=True, fmt=".2g", cbar=False, mask=(corrmap==0))
plt.yticks(rotation=0, fontsize="10", va="center")
plt.tick_params(axis='x', which='major', labelsize=10, labelbottom = True, bottom=True, top = False, labeltop=False)
bottom,top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
plt.title('{} correlation heatmap with Carbon emission'.format(Regions[4][5:]), fontsize="12")
ax.set_ylabel('') 
#plt.show()
plt.savefig("Heat map Middle_East_Corr.png",dpi=150,bbox_inches='tight')

#Heatmap of Africa region
corrmap=Africa_Corr.fillna(0)
corrmap.sort_values('Countries', inplace=True)
f, ax = plt.subplots(figsize=(7,4)) 
sns.heatmap(corrmap, ax = ax, cmap ="RdBu_r",  linecolor='black', vmin=-1, vmax=1, annot=True, fmt=".2g", cbar=False, mask=(corrmap==0))
plt.yticks(rotation=0, fontsize="10", va="center")
plt.tick_params(axis='x', which='major', labelsize=10, labelbottom = True, bottom=True, top = False, labeltop=False)
bottom,top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
plt.title('{} correlation heatmap with Carbon emission'.format(Regions[5][5:]), fontsize="12")
ax.set_ylabel('') 
#plt.show()
plt.savefig("Heat map Africa_Corr.png",dpi=150,bbox_inches='tight')

#Heatmap of Asia Pacific region
corrmap=Asia_Pacific_Corr.fillna(0)
corrmap.sort_values('Countries', inplace=True)
f, ax = plt.subplots(figsize=(7,7)) 
sns.heatmap(corrmap, ax = ax, cmap ="RdBu_r",  linecolor='black', vmin=-1, vmax=1, annot=True, fmt=".2g", cbar=False, mask=(corrmap==0))
plt.yticks(rotation=0, fontsize="10", va="center")
plt.tick_params(axis='x', which='major', labelsize=10, labelbottom = True, bottom=True, top = False, labeltop=False)
bottom,top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
plt.title('{} correlation heatmap with Carbon emission'.format(Regions[6][5:]), fontsize="12")
ax.set_ylabel('') 
#plt.show()
plt.savefig("Heat map Asia_Pacific_Corr.png",dpi=150,bbox_inches='tight')
