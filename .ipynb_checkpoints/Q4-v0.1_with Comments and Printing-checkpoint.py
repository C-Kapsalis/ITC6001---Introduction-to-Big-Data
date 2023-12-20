# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:38:07 2023

@author: Chris
"""

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns

#Creating the dataframes for friends and users AND for artists and users
df_artists= pd.read_csv('user_artists.dat', sep='\\t', encoding=None, names=None, header=0, index_col=None)
df_friends= pd.read_csv('user_friends.dat', sep='\\t', encoding=None, names=None, header=0, index_col=None)


# Dropping weigth column from df_artists
df_artist_dropped_weight=df_artists.drop(columns=['weight'])

#creating dataframe holding the count of artists for each user
df_artists_count=df_artist_dropped_weight.groupby('userID').count().rename(columns={'artistID':'count_of_artists'})


#creating dataframe holding the count of friends for each user
df_friends_count=df_friends.groupby('userID').count().rename(columns={'friendID':'count_of_friends'})

# Merge dataframes based on 'userID'
merged_df = pd.merge(df_friends_count, df_artists_count, on='userID')



######################################### Part a #################################################


#calculate correlation between two columns  using corr() function
corr = merged_df["count_of_friends"].corr(merged_df["count_of_artists"])
corr2=merged_df.corr(method='pearson')

#plotting the scatterplot for the correlation
sns.lmplot(x="count_of_artists", y="count_of_friends", data=merged_df);

## plotting the correlation matrix
plt.figure(figsize=(10,10))
plt.show()
sns.heatmap(corr2, cmap="Greens",annot=True)

print("\n\n################## Part a ##########################\n\n")
print(merged_df)
print("\n Correlation Part A (pearson): ",corr)
print("\n Correlation Matrix Part A (pearson): \n", corr2)

######################################### Part a Alegebraic#################################################


# Extract the two columns
x = merged_df['count_of_friends']
y = merged_df['count_of_artists']

# Calculate mean of each column
mean_x = x.mean()
mean_y = y.mean()

# Calculate the numerator and denominators
numerator = sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y))
denominator_x = sum((x_i - mean_x) ** 2 for x_i in x)
denominator_y = sum((y_i - mean_y) ** 2 for y_i in y)

correlation = numerator / (denominator_x**0.5 * denominator_y**0.5)
print(f"\n Alegebraically calculated Correlation for part A between count_of_friends and count_of_artists: {correlation}")


######################################### Part b #################################################

#Dropping the artistID , hold only the weight column which represents the number of streams/listenings
df_artist_dropped_artistsID=df_artists.drop(columns=['artistID'])

#creating dataframe with user id and the SUM of all their streams/listening instances
df_listening_count=df_artist_dropped_artistsID.groupby('userID').sum().rename(columns={'weight':'sum_of_listening'})

# merge the two dataframes (one holding the count of friends, one holding the sum of weights)
merged_df_part_b = pd.merge(df_friends_count, df_listening_count, on='userID')

#calculate correlation between the two columns using the corr() function
corr3 = merged_df_part_b["sum_of_listening"].corr(merged_df_part_b["count_of_friends"])
corr4=merged_df_part_b.corr(method='pearson')

#plotting the scatterplot for the correlation
sns.lmplot(x="count_of_friends", y="sum_of_listening", data=merged_df_part_b);

#plotting the correlation matrix
plt.figure(figsize=(10,10))
sns.heatmap(corr4, cmap="Blues",annot=True)
plt.show()

print("\n\n#################### Part b #############################\n\n")
print(merged_df_part_b)
print("\n Correlation part B (pearson): ",corr3)
print("\n Correlation Matrix Part B (pearson): \n", corr4)


######################################### Part b Alegebraic#################################################

# Extract the two columns
x1 = merged_df_part_b['count_of_friends']
y1 = merged_df_part_b['sum_of_listening']

# Calculate mean of each column
mean_x1 = x1.mean()
mean_y1 = y1.mean()

# Calculate the numerator and denominators
numerator1 = sum((x_i - mean_x1) * (y_i - mean_y1) for x_i, y_i in zip(x1, y1))
denominator_x1 = sum((x_i - mean_x1) ** 2 for x_i in x1)
denominator_y1 = sum((y_i - mean_y1) ** 2 for y_i in y1)

correlation1 = numerator1 / (denominator_x1**0.5 * denominator_y1**0.5)
print(f"\n Alegebraically calculated Correlation for part B between count_of_friends and sum_of_listening: {correlation1}")