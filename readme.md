# User Similarity & Behavior Analysis on Last.fm  
**Course**: ITC6001 – Introduction to Big Data  

**Institution**: MSc in Data Science, The American College of Greece  

**Term**: Fall 2023  

## 📌 Overview  
This project explores user activity, similarity, and community structures on the Last.fm music platform. Using user-artist interaction data and social graphs, we identify outliers, cluster users by listening behavior, and quantify relationships using cosine similarity and community detection methods.

## 📁 Project Structure

```
.
├── data/                       # Raw Last.fm datasets
│   ├── artists.dat
│   ├── tags.dat
│   ├── user_artists.dat
│   ├── user_friends.dat
│   ├── user_taggedartists.dat
│   ├── user_taggedartists-timestamps.dat
│   └── README.md
│
├── results/                    # Output files: CSVs and similarity matrices
│   ├── Q3a_users.csv
│   ├── neighbors-k-users.data
│   └── ...
│
├── report/                     # Final report, presentation, and documentation
│   ├── ITC6001_Stavrogiannis_Kapsalis.docx
│   ├── ITC6001 Final-Project-Fall-2023.pdf
│   └── ITC_6001_presentation_Kapsalis_Stavrogiannis.pptx
│
├── src/                        # Python script(s)
│   └── analysis.py
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview (this file)
```

## 🔧 How to Run

1. Clone the repository:  
   `git clone https://github.com/yourusername/lastfm-user-analysis`

2. Navigate to the project folder:  
   `cd lastfm-user-analysis`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Run the main script:  
   `python src/analysis.py`

Outputs will be saved in the `results/` directory.

## 📦 Dependencies  
The project uses Python 3 with the following core libraries:
- pandas
- numpy
- scikit-learn
- networkx
- matplotlib

All dependencies are listed in `requirements.txt`.

## 📊 Input Data  
Stored in the `data/` directory. It contains six `.dat` files from the Last.fm academic dataset, covering user listening behavior, artist metadata, tags, and friendships.  
See `data/README.md` for full file descriptions.

## 📈 Output Data  
Stored in `results/` and includes:
- Outlier detection results (Z-score, IQR)
- User and tag rankings
- Cosine similarity matrices
- K-nearest neighbor user clusters
- Community detection assignments

## 📎 Deliverables  
The full report, presentation, and documentation are included in the `report/` folder:
- Project write-up (DOCX + PDF)
- Final presentation (PPTX)

## 📝 License  
For academic and demonstration purposes only.
