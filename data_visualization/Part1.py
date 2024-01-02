# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:09:22 2024

Analysis of Northern Ireland labour market structure, aged 16 to 64, 
numbers and rates, seasonally adjusted
Reference: https://www.nisra.gov.uk/publications/labour-market-report-december-2023

@author: Snehal
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\User\Downloads\Northern Ireland labour market structure-Part 1.csv")

# First plot
plt.bar(data['Rolling monthly quarter'], data['Total in employment'], width = 0.5)
plt.xlabel('Rolling monthly quarter')
plt.ylabel('Employed population')
plt.xticks(rotation=90, fontsize = 'small')
plt.title('Employment gradient from Aug 2021 to Oct 2023')
plt.show()

# Second plot
plt.figure()
plt.plot(data['Rolling monthly quarter'], data['Unemployed'])
plt.xlabel('Rolling monthly quarter')
plt.ylabel('Unemployed population')
plt.title('Unemployment gradient from Aug 2021 to Oct 2023')
plt.xticks(rotation=90, fontsize = 'small')
plt.show()

# Third plot
plt.figure()
plt.plot(data['Rolling monthly quarter'], data['Male employment rate (%)'], label ='Male Employment rate')
plt.plot(data['Rolling monthly quarter'], data['Female employment rate (%)'], label ='Female Employment rate')
plt.legend()
plt.xlabel('Rolling monthly quarter')
plt.ylabel('Employment rate')
plt.title('Male vs Female employment rate')
plt.xticks(rotation=90, fontsize = 'small')
plt.show()

# Fourth plot
plt.figure()
plt.scatter(data['Rolling monthly quarter'], data['Male unemployment rate (%)'],
         label ='Male unemployment rate', color='blue', marker= '*')
plt.scatter(data['Rolling monthly quarter'], data['Female unemployment rate (%)'],
         label ='Female unemployment rate', color= 'red', marker='v')
plt.legend()
plt.xlabel('Rolling monthly quarter')
plt.ylabel('Unemployment rate')
plt.title('Male vs Female unemployment rate')
plt.xticks(rotation=90, fontsize = 'small')
plt.show()















