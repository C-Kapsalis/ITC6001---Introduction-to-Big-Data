# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:39:54 2023

@author: Chris
"""

import pandas as pd
import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity

##################################### Q2 Part 1 ###############################################

df = pd.read_csv('user_artists.dat', sep='\\t', encoding=None, names=None, header=0, index_col=None)
# Create a pivot table without filling missing values
pivot_table = df.pivot_table(index='userID', columns='artistID', values='weight')

# Fill missing values with 0
pivot_table.fillna(0, inplace=True)

# Calculate cosine similarity  using dot product and np.linalg.norm
cosine_sim = pivot_table.dot(pivot_table.T) / (np.linalg.norm(pivot_table, axis=1)[:, None] * np.linalg.norm(pivot_table.T, axis=0))

# Create a DataFrame from the similarity matrix
cosine_sim_df = pd.DataFrame(cosine_sim, index=pivot_table.index, columns=pivot_table.index)




pivot_table = df.pivot_table(index='userID', columns='artistID', values='weight')

# Fill missing values with 0
pivot_table.fillna(0, inplace=True)

# Calculate cosine similarity directly using dot product and np.linalg.norm
cosine_sim = pivot_table.dot(pivot_table.T) / (np.linalg.norm(pivot_table, axis=1)[:, None] * np.linalg.norm(pivot_table.T, axis=0))


######################################Q2 Part 1 using  sklearn#########################################

# Calculate cosine similarity directly on the pivot table
#cosine_sim = cosine_similarity(pivot_table)
#######################################################################################################



# Create a DataFrame from the similarity matrix
cosine_sim_df = pd.DataFrame(cosine_sim, index=pivot_table.index, columns=pivot_table.index)

cosine_sim_df_with_id = cosine_sim_df.copy()
cosine_sim_df_with_id.insert(0, 'user_id', cosine_sim_df.index)

# Save the cosine similarity matrix with user IDs to a CSV file
cosine_sim_df_with_id.to_csv('user-pairs-similarity.data', index=False)




##################################### Q2 Part 2 ###############################################




# Function to find k-nearest neighbors for a user
def find_neighbors(user_id, k):
    # Get the user's similarity scores with all other users
    user_similarities = cosine_sim_df.loc[user_id]

    # Sort the users based on similarity and select the top k (excluding the user itself)
    neighbors = user_similarities.sort_values(ascending=False).index[1:k+1].tolist()

    return neighbors

# Dictionary to store neighbors for each user
neighbors_dict = {}

# Find and store neighbors for each user for k=3 and k=10
for user_id in pivot_table.index:
    neighbors_dict[user_id] = {
        'k=3': find_neighbors(user_id, 3),
        'k=10': find_neighbors(user_id, 10),
    }

# Save the neighbors dictionary to a JSON file
with open('neighbors-k-users.data', 'w') as json_file:
    json.dump(neighbors_dict, json_file, indent=2)




