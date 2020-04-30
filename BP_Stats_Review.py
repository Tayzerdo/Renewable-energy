# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:47:51 2020

@author: tayze
"""
import pandas as pb

#Worksheet Primary Energy Consumption
file = pb.read_excel('bp-stats-review-2019-all-data.xlsx', sheet_name = 'Primary Energy Consumption', hearders = 2, skiprows=2, usecols=range(55)).dropna(axis=0,how='all')

#Find the lines for each categorie (in terms of Region)
Places = file[~file['Million tonnes oil equivalent'].str.startswith('Total')]

#Find only the Total values
Total_Countries = file[file['Million tonnes oil equivalent'].str.startswith('Total')]
