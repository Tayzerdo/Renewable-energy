# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:47:51 2020

@author: tayze
"""
import pandas as pb

#Worksheet Primary Energy Consumptioin
file = pb.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Primary Energy Consumption', hearders = 2, skiprows=2, usecols=range(55))
#print(file)


#Find the lines for each categorie (in terms of Region)
places= file['Million tonnes oil equivalent']
#print(places)
#print(type(places))
number=0
lines=list()


Countries = file.drop([4,17,53,63,74,85,105,106,107,108,109,110,111,112,113,114,115,116,117],0).dropna(axis=0,how='all').sort_values(by='Million tonnes oil equivalent')

#print(Countries.describe())

Statistic_Describe=Countries.describe()
print(Statistic_Describe.iloc[2,:])

#4,17,53,63,74,85,105 em diante (107 total world)

#.dropna(axis=0,how='all')
#print(lines)

#Countries = places.drop(index=lines)

#print(Countries.head(50))

#Total_Countries = file







##Total North America
#Total_North = file.iloc[:4,:]
#print(Total_North)
#
##Total S. & Cent. America
#Total_Latin = file.iloc[6:16,:]
#print(Total_Latin)
#
##Total Europe
#Total_Europe = file.iloc[17,51,:]
#print(Total_Europe)
#
##Total CIS
#Total_CIS = file.iloc[52:60,:]
#print(Total_CIS)
#
##Total Middle East
#Total_Middle = file.iloc[61,70,:]
#print(Total_Middle)
#
##Total Africa
#Total_Africa = file.iloc[71,80,:]
#print(Total_Africa)
#
##Total Asia Pacific
#Total_Asia = file.iloc[81,99,:]
#print(Total_Asia)
