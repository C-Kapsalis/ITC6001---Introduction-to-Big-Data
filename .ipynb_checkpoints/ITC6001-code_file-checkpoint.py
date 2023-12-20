import numpy as np
import numpy.linalg as la
import pandas as pd 
from datetime import datetime
import plotly.express as px
import matplotlib.pyplot as plt
plt.ioff()

# reading all data files into pandas dataframes
artist_info = pd.read_csv('artists.dat', sep='\t', encoding=None, names=None, header=0, index_col=None)
tag_info = pd.read_csv('tags.dat', sep='\t', encoding='ISO-8859-1', names=None, header=0, index_col=None)
user_artists = pd.read_csv('user_artists.dat', sep='\t', encoding=None, names=None, header=0, index_col=None)
user_friends = pd.read_csv('user_friends.dat', sep='\t', encoding=None, names=None, header=0, index_col=None)
user_tags_ts = pd.read_csv('user_taggedartists-timestamps.dat', sep='\t', encoding=None, names=None, header=0, index_col=None)
user_tags = pd.read_csv('user_taggedartists.dat', sep='\t', encoding=None, names=None, header=0, index_col=None)



