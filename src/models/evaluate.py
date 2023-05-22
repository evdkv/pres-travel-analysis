import joblib
import numpy as np

def display_topics(components, vocab):
    for i, topic in enumerate(components):
        print("Topic {}: {}".format(i + 1, ",".join([str(x) for x in vocab[topic.argsort()[-6:]]])))

def main():
    model = joblib.load('models/nmf.joblib')
    features = joblib.load('models/tfidf_features.joblib')
    vocab = np.array(features.get_feature_names_out())

    display_topics(model.components_, vocab)

main()