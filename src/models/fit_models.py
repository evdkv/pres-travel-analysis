from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import NMF, PCA
from sklearn.manifold import TSNE
import pandas as pd
import joblib


def main():
    df = pd.read_csv('data/travel_processed.csv')
    tfidf = extract_features(df['remarks'])
    models = fit_models(tfidf)
    save_models(models[0], models[1], models[2], models[3])

def extract_features(df):   

    tfidf_vectorizer = TfidfVectorizer(max_df=0.6, min_df=2,stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(df)

    joblib.dump(tfidf, 'models/' + 'tfidf_features.joblib')
    joblib.dump(tfidf_vectorizer, 'models/' + 'tfidf_vectorizer.joblib')
    # tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

    # tf_vectorizer = CountVectorizer(max_df=0.7, min_df=5, stop_words='english')
    # tf = tf_vectorizer.fit_transform(df)
    # tf_feature_names = tf_vectorizer.get_feature_names_out()

    return tfidf

def fit_models(tfidf):
    no_topics = 10
    no_clusters = 7

    # Run NMF (topics)
    nmf = NMF(n_components=no_topics, init='nndsvd').fit(tfidf)

    # Run t-SNE (dimensionality reduction)
    tsne = TSNE(n_components=2, init='random').fit_transform(tfidf)

    kmeans = KMeans(n_clusters=no_clusters, n_init=20).fit_predict(tfidf)

    pca = PCA(n_components=3).fit_transform(tfidf.toarray())

    return nmf, tsne, kmeans, pca

def save_models(nmf, tsne, kmeans, pca):
    joblib.dump(nmf, 'models/' + 'nmf.joblib')
    joblib.dump(tsne, 'models/' + 'tsne.joblib')
    joblib.dump(kmeans, 'models/' + 'kmeans.joblib')
    joblib.dump(pca, 'models/' + 'pca.joblib')

if __name__ == '__main__':
    main()