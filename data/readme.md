# Last.fm Dataset – Data Folder

This folder contains preprocessed `.dat` files from the [Last.fm Music Social Network Dataset](https://www.last.fm) (academic version). These were used for exploratory, graph-based, and similarity-based analyses.

## Files

- **user_artists.dat**  
  Format: `userID\tartistID\tweight`  
  Number of plays per user-artist pair.

- **user_friends.dat**  
  Format: `userID\tfriendID`  
  Directed edge list representing the social graph.

- **artists.dat**  
  Format: `artistID\tname\turl\tpictureURL`  
  Artist metadata.

- **tags.dat**  
  Format: `tagID\ttagValue`  
  Global music tags.

- **user_taggedartists.dat**  
  Format: `userID\tartistID\ttagID\ttimestamp`  
  Specific tags applied by users to artists.

- **user_taggedartists-timestamps.dat**  
  Same structure as above, preserving timestamps separately for temporal analysis.

## Notes  
- Fields are tab-separated.  
- All IDs are integer-encoded.  
- Missing values and duplicates were filtered during preprocessing.

