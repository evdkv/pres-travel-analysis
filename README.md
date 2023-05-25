[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

U.S. Officials Travel Analysis
==============================

A textual analysis of the travel patterns for the US president 
and secretary using NMF, PCA, t-SNE, and TF-IDF. I found this dataset
online when I was preparing a final project for my data science class and
thought that these data might be interesting to look at on their own + I
wanted to practice some of my data analysis skills :). <br>

I scraped the raw dataset for the analysis from the U.S. Historian website using 
BeautifulSoup and cleaned the data which can be found in the tidy dataset. I primarily 
used scikit-learn to analyze the data and seaborn + plotly for visualizations. <br>

A project report/analysis interpretations can be found [here](https://evdkv.github.io/proj/travel).

Project Organization
------------

```bash
.
├── LICENSE
├── README.md
├── data
│   ├── README.md               # Data dictionaries
│   ├── travel_processed.csv    # A tidy dataset with a processed textual component
│   ├── travel_raw.csv          # A raw scraped dataset
│   └── travel_tidy.csv         # A tidy dataset with an unprocessed textual component
├── external
│   ├── LICENSE     # License for ctfidf.py
│   ├── README.md   # Credit for ctfidf.py
│   └── ctfidf.py   # A class for calculating class-based TF-IDF
├── models
│   ├── kmeans.joblib           # K-Means saved model
│   ├── nmf.joblib              # NMF saved model
│   ├── pca.joblib              # PCA saved model
│   ├── tfidf_features.joblib   # TF-IDF matrix
│   ├── tfidf_vectorizer.joblib # TF-IDF scikit object
│   └── tsne.joblib             # t-SNE saved model
├── notebooks
│   ├── visualize_clusters.ipynb  # Visualizing PCA and t-SNE embeddings
│   ├── visualize_exp.ipynb       # Exploratory analyses and visualizations
│   └── visualize_tfidf.ipynb     # Visualizing TF-IDF results
└── src
    ├── data
    │   ├── preprocess.py   # Script for cleaning the textual portion of the data
    │   ├── scrape.py       # Script for scraping the raw data
    │   └── tidy.py         # Script for cleaning up the dates and separating locales
    └── models
        └── fit_models.py   # Script for fitting the models
```

[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/