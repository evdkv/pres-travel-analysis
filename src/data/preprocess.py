import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def main():
    df = pd.read_csv('data/travel_tidy.csv')
    df = df[['event_id', 'visit_type','name', 'remarks']]
    df = df.drop_duplicates()
    df = df[['event_id', 'visit_type', 'name', 'remarks']]

    df['remarks'] = df['remarks'].apply(lambda remarks: ' '.join(preprocess(remarks)))
    df.to_csv('data/travel_processed.csv', index=False)

def preprocess(sentence):
    clean = remove_stop_words_digits(clean_sent(sentence))
    return lemmatize_sent(clean)

def clean_sent(sentence):
    clean = sentence.lower()
    clean = re.sub(r'[^\w\s]', '', clean)
    clean = re.sub(r'\w*[0-9]\w*', '', clean) # remove all digit-word combinations
    return word_tokenize(clean)

def remove_stop_words_digits(sent_list):
    stop_words = set(stopwords.words('english'))
    filtered = [word for word in sent_list if (word not in stop_words) and not (word.isdigit())]
    return filtered

def lemmatize_sent(sent_list):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, 'v') for word in sent_list]

if __name__ == '__main__':
    main()