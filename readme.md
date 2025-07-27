# User Behavior & Similarity Analysis on the Last.fm Dataset  
*ITC6001 – Introduction to Big Data (MSc Data Science, ACG)*

## Overview  
This project presents an analytical exploration of the Last.fm dataset to uncover patterns of user behavior, music preferences, and social connections. The dataset includes music listening habits, tags, friendships, and artist metadata for 1,892 users on the Last.fm platform.

The work is structured into six stages—from exploratory data analysis to user similarity scoring—using Python-based tools and methods consistent with big data principles.

## Objectives  
- Describe key features of the dataset and perform initial exploration  
- Identify outliers in listening activity  
- Quantify user-to-user similarity using cosine metrics  
- Construct a graph-based representation of user connections  
- Extract community structure using Louvain modularity  
- Analyze social and musical overlap among clusters

## Dataset  
The dataset originates from the **Last.fm Music Social Network Dataset** and includes:  
- `user_artists.dat`: Listening counts per user-artist pair  
- `tags.dat`: Community tagging behavior  
- `user_friends.dat`: User social graph  
- `artists.dat`: Artist metadata  
- `user_taggedartists.dat`: User-applied tags per artist

## Methodology  
- **Data cleaning & preprocessing** using pandas and NumPy  
- **Similarity analysis** via cosine similarity and k-nearest neighbors  
- **Graph construction** with NetworkX  
- **Community detection** using Louvain clustering  
- **Visualization** of networks and tag distributions with matplotlib  

## Tools  
- Python 3  
- pandas, NumPy  
- NetworkX  
- scikit-learn  
- matplotlib  

## Results  
- Identification of super-listener users with unusually high activity  
- Clear segmentation of music listeners based on artist overlap  
- Social clusters showed moderate musical similarity, validating community structure  
- Tags aligned with detected communities, suggesting consistency between user tastes and social links

## Deliverables  
- `ITC6001_code_file.py`: Source code  
- Project Report (PDF & DOCX)  
- Final Presentation (PPTX)

## Authors  
- Christoforos Kapsalis  
- Charalampos Stavrogiannis  

## License  
For academic and demonstration purposes only.
