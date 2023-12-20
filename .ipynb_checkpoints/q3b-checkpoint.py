# I'll create series objects of length = 5 for each quarter, and then I'll join them into a single df for each sub-question
top_artists = [] 
for i in range(len(user_tags_ts['quarters'].unique())):
    q = user_tags_ts['quarters'].unique()[i]  # the df is sorted in ascending order based on this column, so the corresponding values will
    # be considered in ascending order as well
    fin = user_tags_ts['artistID'][user_tags_ts['quarters'] == q].groupby(user_tags_ts['artistID']).count().sort_values(ascending=False)[:5]
    if len(fin) < 5:
        fin += [np.nan] * (5 - len(fin))
    top_artists.append([q, fin])
    
    
top_5_ids = [] 
top_5_freqs = [] 
qqs = [] 
for t in top_artists:
    for i in range(len(t[1].values)):
        qqs.append(t[0])
        top_5_ids.append(t[1].index[i])
        top_5_freqs.append(t[1].values[i])       
        
res_artists = pd.DataFrame([qqs, top_5_ids, top_5_freqs]).T
res_artists.columns = ['quarter', 'id', 'freq']
# res_artists['artist_id'] = res_artists['artist_id'].replace(-1, np.nan)
# res_artists['freq'] = res_artists['freq'].replace(0, np.nan)
# res_artists.dropna(how='any', axis=0, inplace=True)
#res_artists['artist_id'] = res_artists['artist_id'].astype('int8')
res_artists.sort_values(by=['quarter', 'freq'], ascending=[True,False])