# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:47:51 2020

@author: tayze
"""
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split 

print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
color=dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
#####Excel file
##https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/xlsx/energy-economics/statistical-review/bp-stats-review-2019-all-data.xlsx

#####Worksheet names
#test = pd.ExcelFile('bp-stats-review-2019-all-data.xlsx')
#worksheet_names=test.sheet_names
#print(worksheet_names)
#for i in worksheet_names:
#    print(i)
#    qw=pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name=i)
#    print(qw)

#####Worksheet Electricity generation - TWh (from 1985)
#file = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Elec Gen by fuel', headers = 2, skiprows=2, usecols = range(17)).dropna(axis=0,how='all').iloc[:-6]
#file.fillna('0',inplace=True)
##print(file)
#
####Taking only the countries
#Countries = file[~file['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
##print(type(Countries))    
#
####Taking only the Totals
#Total_Countries = file[file['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Total_Countries.set_index('Terawatt-hours', inplace=True)
#
#fuels_name = Total_Countries.head(0)
#
#
#print(fuels_name)
#for i in fuels_name:
#    Total_Countries.plot(kind='bar', y=i)
#    plt.title('Electricity generation by fuel')
#    plt.xlabel('Coutries by region')
#    plt.ylabel('Electricity (MTw)')
#    plt.show()
#
#
#
#
####Worksheet Renewables: Generation*
##Renewables - TWh
#Renew = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Renewables - TWh', headers = 2, skiprows=2, usecols = range(55)).dropna(axis=0,how='all').iloc[:-10]
#Renew.fillna('0',inplace=True)
##print(Renew)
#
####Taking only the countries
#Countries_Renew = Renew[~Renew['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Countries_Renew.set_index('Terawatt-hours', inplace=True)
##print(Countries_Renew.head())    
#
####Taking only the Totals
#Total_Renew = Renew[Renew['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Total_Renew.set_index('Terawatt-hours', inplace=True)
#
##Plot line chart with the Renew generation by region
#df=Total_Renew.drop(['Total World']).transpose()
#df.plot(kind='box', figsize=(15,5), color=color, sym='r+')
#plt.title('Renewable generation by region')
#plt.xlabel('Year')
#plt.ylabel('Generation (TWh)')
#plt.show()
#
#
##build the Linear plot regression by region
#n=0
#for j in df.columns:
#    print('The region is: '+j)
#    print(n)
#    for i in range(1,4):
#        #import the dataset
#        x=df.index.values.reshape(-1,1)
#        y=df.iloc[:,int(n)].values.reshape(-1,1)
#        
#        #Fit the linear regression
#        lin=LinearRegression()
#        lin.fit(x,y)
#        
#        #Fit the Poly regression
#        poly = PolynomialFeatures(degree = i)
#        x_poly = poly.fit_transform(x)
#        poly.fit(x_poly,y)
#        lin2=LinearRegression()
#        lin2.fit(x_poly,y)
#        
#        #Plot Poly regression
#        plt.scatter(x,y,color='blue')
#        plt.plot(x,lin2.predict(poly.fit_transform(x)),color='red')
#        plt.title('Polynomial Regression degree '+str(i))
#        plt.xlabel('Year')
#        plt.ylabel('Renewable Generation (TWh)')
#        plt.show()
#        print(lin2.predict(poly.fit_transform([[2019]])))
#        print(lin2.predict(poly.fit_transform([[2020]])))
#    n=n+1
#
#
#    
#####Worksheet Renewables: Generation- Solar* 
##Solar Generation - TWh
#Solar_Gen = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Solar Generation - TWh', headers = 2, skiprows=2, usecols = range(55)).dropna(axis=0,how='all').iloc[:-10]
#Solar_Gen.fillna('0',inplace=True)
##print(Solar_Gen)
#
####Taking only the countries
#Countries_Solar_Gen = Solar_Gen[~Solar_Gen['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Countries_Solar_Gen.set_index('Terawatt-hours', inplace=True)
##print(Countries_Sold()ar_Gen.hea)    
#
####Taking only the Totals
#Total_Solar_Gen = Solar_Gen[Solar_Gen['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Total_Solar_Gen.set_index('Terawatt-hours', inplace=True)
##print(Total_Solar_Gen)
#
##Plot line chart with the Renew generation by region
#df=Total_Solar_Gen.drop('Total World').transpose()
#df.plot(kind='box', figsize=(15,5))
#plt.title('Solar generation by region')
#plt.xlabel('Year')
#plt.ylabel('Generation (TWh)')
#plt.show()
#
#
######Worksheet Renewables: Generation- Wind*
##Wind Generation - TWh
#Wind_Gen = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Wind Generation - TWh ', headers = 2, skiprows=2, usecols = range(55)).dropna(axis=0,how='all').iloc[:-10]
#Wind_Gen.fillna('0',inplace=True)
##print(Wind_Gen)
#
####Taking only the countries
#Countries_Wind_Gen = Wind_Gen[~Wind_Gen['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Countries_Wind_Gen
##print(Countries_Wind_Gen)    
#
####Taking only the Totals
#Total_Wind_Gen = Wind_Gen[Wind_Gen['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Total_Wind_Gen.set_index('Terawatt-hours', inplace=True)
##print(Total_Wind_Gen)
#
##Plot line chart with the Renew generation by region
#df=Total_Wind_Gen.drop('Total World').transpose()
#df.plot(kind='box', figsize=(15,5), color=color, sym='r+')
#df.plot(kind='line', figsize=(15,5))
#plt.title('Wind generation by region')
#plt.xlabel('Year')
#plt.ylabel('Generation (TWh)')
#plt.show()


#
#####Worksheet Renewables: Generation- Geothermal, Biomass and Other*
##Geo Biomass Other - TWh 
#Other = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Geo Biomass Other - TWh', headers = 2, skiprows = 2, usecols = range(55)).dropna(axis=0,how='all').iloc[:-10]
#Other.fillna('0', inplace=True)
##print(Other)
#
####Taking only the countries
#Countries_Other = Other[~Other['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Countries_Other.set_index('Terawatt-hours',inplace=True)
##print(Countries_Other)
#
####Taking only the Totals
#Total_Other = Other[Other['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#Total_Other.set_index('Terawatt-hours',inplace=True)
##print(Total_Other)
#
##Plot line chart with the Renew generation by region
#df=Total_Other.drop('Total World').transpose()
#df.plot(kind='box', figsize=(15,5), color=color, sym='r+')
#df.plot(kind='line', figsize=(15,5))
#plt.title('Other renewable generation by region')
#plt.xlabel('Year')
#plt.ylabel('Generation (TWh)')
#plt.show()




#####Work sheet Carbon Dioxide Emissions (from 1965) 
###Carbon Dioxide Emissions
#Carbon = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Carbon Dioxide Emissions', headers = 2, skiprows = 2, usecols = range(55)).dropna(axis=0,how='all').iloc[:-11]
#Carbon.fillna('0', inplace=True)
#print(Carbon)
#
####Taking only the countries
#Countries_Carbon = Carbon[~Carbon['Million tonnes of carbon dioxide'].str.startswith('Total')].sort_values(['Million tonnes of carbon dioxide'])
#Countries_Carbon.set_index('Million tonnes of carbon dioxide',inplace=True)
##print(Countries_Carbon)
#
####Taking only the Totals
#Total_Carbon = Carbon[Carbon['Million tonnes of carbon dioxide'].str.startswith('Total')].sort_values(['Million tonnes of carbon dioxide'])
#Total_Carbon.set_index('Million tonnes of carbon dioxide',inplace=True)
##print(Total_Other)
#
##Plot line chart with the Renew generation by region
#df=Total_Carbon.drop('Total World').transpose()
#df.plot(kind='box', figsize=(15,5), color=color, sym='r+')
#df.plot(kind='line', figsize=(15,5))
#plt.title('Carbon Dioxide Emissions')
#plt.xlabel('Year')
#plt.ylabel('Generation (TWh)')
#plt.show()

