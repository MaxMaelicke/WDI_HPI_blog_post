#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:52:41 2020

@author: max
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Import WDI data (World Development Indicators)
df_wdi = pd.read_csv('data/WDIData.csv')

# Import HPI dataset (Happy Planet Index)
df_hpi = pd.read_excel('data/hpi-data-2016.xlsx', sheet_name = 'Complete HPI data', header = 5, usecols = 'B:O')
#df_hpi.head()

# Import WDI indicator descriptions (World Development Indicators)
'''
df_wdi_inds = pd.read_csv('../data/WDISeries.csv')

# All indicator codes
wdi_inds = list(df_wdi_inds['Indicator Code'])
wdi_inds.insert(0, 'Country Name')
wdi_inds
'''
wdi_inds = list(df_wdi['Indicator Code'].unique())
wdi_inds.insert(0, 'Country Name')
wdi_inds

# Create DataFrame with WDI Data for year 2016 (same year as HPI data)
# Show Indicator Code in columns, Country Code in row, 2016 values in appropriate column/row
#list_cty = []
#list_ind = []
#list_val = []
#for row in df_wdi:
#    list_cty.append(df_wdi['Country Name'])
#    list_ind.append(df_wdi['Indicator Name'])
#    list_val.append(df_wdi['2016'])

#cty_ind_val = [comb for comb in zip(list_cty, list_ind, list_val)]
    
df_wdi_2016 = pd.DataFrame(columns = wdi_inds)

for row in df_wdi:
    df_wdi_2016['Country Name'] = df_wdi['Country Name']
    df_wdi_2016[df_wdi['Indicator Code']] = df_wdi['2016']

df_wdi_2016

