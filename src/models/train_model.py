from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
import pandas as pd
import joblib

def main():
    df = pd.read_csv('../pres-travel-analysis/data/travel_processed.csv')
    tf, tfidf = extract_features(df['remarks'])
    models = train_models(tf, tfidf)
    save_models(models[0], models[1], models[2])

def extract_features(df):   

    tfidf_vectorizer = TfidfVectorizer(max_df=0.7, min_df=5, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(df)
    # tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

    tf_vectorizer = CountVectorizer(max_df=0.7, min_df=5, stop_words='english')
    tf = tf_vectorizer.fit_transform(df)
    # tf_feature_names = tf_vectorizer.get_feature_names_out()

    return tf, tfidf

def train_models(tf, tfidf):
    no_topics = 10

    # Run NMF
    nmf = NMF(n_components=no_topics, init='nndsvd').fit(tfidf)

    # Run LDA
    lda = LatentDirichletAllocation(n_components=no_topics, max_iter=100, learning_method='online').fit(tf)

    # Run LSA (via TruncatedSVD)
    lsa = make_pipeline(TruncatedSVD(n_components=no_topics), Normalizer(copy=False))

    return nmf, lda, lsa

def save_models(nmf, lda, lsa):
    joblib.dump(nmf, '../pres-travel-analysis/models/' + 'nmf.sav')
    joblib.dump(lda, '../pres-travel-analysis/models/' + 'lda.sav')
    joblib.dump(lsa, '../pres-travel-analysis/models/' + 'lsa.sav')

if __name__ == '__main__':
    main()