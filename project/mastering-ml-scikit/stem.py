from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

wordnet_tags=['n', 'v']

corpus = [
    'He ate the sandwiches',
    'Every sandwich was eaten by him'
]

stemmer = PorterStemmer()
print('Stemmed:', [[stemmer.stem(token) for token in
    word_tokenize(document)] for document in corpus])

def lemmatize(token, tag):
        if tag[0].lower() in ['n', 'v']:
            return lemmatizer.lemmatize(token, tag[0].lower())
        return token

lemmatizer = WordNetLemmatizer()

tagged_corpus = [pos_tag(word_tokenize(document)) for document in corpus]

print('\nTagged_corpus', tagged_corpus)

print('\nLemmatized:', [[lemmatize(token, tag) for token, tag in document] for document in tagged_corpus])
#

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

corpus = ['The dog ate a sandwich, the wizard transfigured a sandwich, and I ate a sandwich']

vectorizer = CountVectorizer(stop_words='english')

frequencies = np.array(vectorizer.fit_transform(corpus).todense())[0]

print(frequencies)

print('Token indices %s ' % vectorizer.vocabulary_)

for token, index in vectorizer.vocabulary_.items():
    print('The token "%s" appears %s times' % (token, frequencies[index]))




