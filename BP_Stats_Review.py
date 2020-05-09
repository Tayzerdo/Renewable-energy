# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:47:51 2020

@author: tayze
"""
import pandas as pb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split 

###Excel file
#https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/xlsx/energy-economics/statistical-review/bp-stats-review-2019-all-data.xlsx
test = pd.read_excel('bp-stats-review-2019-all-data.xlsx')

###Worksheet names
Worksheet_names = test.iloc[:,0].tolist()
#print(Worksheet_names)

###Worksheet Electricity generation - TWh (from 1985)
file = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Elec Gen by fuel', headers = 2, skiprows=2, usecols = range(17)).dropna(axis=0,how='all').iloc[:-6]
#print(file)

#Find the lines for each categorie (in terms of Region)
Countries = file[~file['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
#print(type(Countries))    

#Find Total values for region
Total_Countries = file[file['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
Total_Countries.set_index('Terawatt-hours', inplace=True)

#Take the fuel names
fuels_name = Total_Countries.head(0)

#Plot Bar graphics by fuel name
print(fuels_name)
for i in fuels_name:
    Total_Countries.plot(kind='bar', y=i)
    plt.title('Electricity generation by fuel')
    plt.xlabel('Coutries by region')
    plt.ylabel('Electricity (MTw)')
    plt.show()

    
####Worksheet Renewables: Generation*
##Renewables - TWh
Renew = pd.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Renewables - TWh', headers = 2, skiprows=2, usecols = range(55)).dropna(axis=0,how='all').iloc[:-10]
Renew.fillna('0',inplace=True)
#print(Renew)

#Taking only the countries
Countries_Renew = Renew[~Renew['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
Countries_Renew.set_index('Terawatt-hours', inplace=True)
#print(Countries_Renew.head())    

#Taking only the Totals
Countries_Renew_Total = Renew[Renew['Terawatt-hours'].str.startswith('Total')].sort_values(['Terawatt-hours'])
Countries_Renew_Total.set_index('Terawatt-hours', inplace=True)

#build the Linear plot regression by region
df=Countries_Renew_Total.drop(['Total World']).transpose()
n=0
for j in df.columns:
    print('The region is: '+j)
    for i in range(1,3):
        x=df.index.values.reshape(-1,1)
        y=df.iloc[:,int(n)].values.reshape(-1,1)
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
        poly = PolynomialFeatures(degree = i)
        x_poly = poly.fit_transform(x)
        lin2=LinearRegression()
        lin2.fit(x_poly,y)
        plt.scatter(x,y,color='blue')
        plt.plot(x,lin2.predict(poly.fit_transform(x)),color='red')
        plt.title('Polynomial Regression degree '+str(i))
        plt.xlabel('Year')
        plt.ylabel('Renewable Generation (TWh)')
        plt.show()
        print(lin2.predict(poly.fit_transform([[2019]])))
        print(lin2.predict(poly.fit_transform([[2020]])))
    n=+1
