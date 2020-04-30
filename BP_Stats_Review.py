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

###4,17,53,63,74,85,105 til the end###

Countries = file.drop([4,17,53,63,74,85,105,106,107,108,109,110,111,112,113,114,115,116,117],0).dropna(axis=0,how='all').sort_values(by='Million tonnes oil equivalent')

#print(Countries.describe())
