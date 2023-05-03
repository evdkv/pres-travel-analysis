import joblib

# def display_topics(model, feature_names, no_top_words):
#     for topic_idx, topic in enumerate(model.components_):
#         print("Topic %d:" % (topic_idx))
#         print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

# topic_word_list = []
# def get_topics(components, feat): 
#     for i, comp in enumerate(components):
#         terms_comp = zip(feat,comp)
#         sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
#         topic=" "
#         for t in sorted_terms:
#             topic = topic + ' ' + t[0]
#         topic_word_list.append(topic)
#         print(topic_word_list)
#     return topic_word_list

# def main():
#     model = joblib.load('models/nmf.joblib')
#     features = joblib.load('models/tfidf_features.sav')
#     # print(model.get_feature_names_out())

#     get_topics(model.components_, features.get_feature_names_out())
# main()