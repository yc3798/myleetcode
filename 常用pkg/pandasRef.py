# Pandas 常用 

import pandas as pd
import numpy as np


# Load  
fp = "./test.csv"
df = pd.read_csv(fp)
print(df.head())

# basic 
df.describe()
df.size
df.groupby("Rating").mean()

# plot
# 1. Histogram
df = pd.DataFrame({
    'length': [1.5, 0.5, 1.2, 0.9, 3],
    'width': [0.7, 0.2, 0.15, 0.2, 1.1]
    }, index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
hist = df.hist(bins=3)


# arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
#           ['Captive', 'Wild', 'Captive', 'Wild']]
# index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
# df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]},
#                   index=index)
# df
#                 Max Speed
# Animal Type
# Falcon Captive      390.0
#        Wild         350.0
# Parrot Captive       30.0
#        Wild          20.0
# df.groupby(level=0).mean()
#         Max Speed
# Animal
# Falcon      370.0
# Parrot       25.0
# df.groupby(level="Type").mean()
#          Max Speed
# Type
# Captive      210.0
# Wild         185.0


# ==== Simple linear reg ====
# Best fit polynomials.

df_males = df[df['Gender']=='Male']
df_females = df[df['Gender']=='Female']

# Polynomial males.
male_fit = np.polyfit(df_males.Height,df_males.Weight,1)
# array([   5.96177381, -224.49884071])

# Polynomial females.
female_fit = np.polyfit(df_females.Height,df_females.Weight,1)
# array([   5.99404661, -246.01326575])