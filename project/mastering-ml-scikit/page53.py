# coding: utf-8
from sklearn.feature_extraction import DictVectorizer
onehot_encoder = DictVectorizer()
X=[
{'city': 'New York'},
{'city': 'San Francisco'},
{'city': 'Chapel Hill'}
]
print(onehot_encoder.fit_transform(X).toarray())
from sklearn import preprocessing
import numpy as np
Y = np.array([
[0., 0., 5., 13., 9., 1.],
[0., 0., 13., 15., 10., 15.],
[0., 3., 15., 2., 0., 11.]
])
print(preprocessing.scale(Y))
corpus=[
'UNC played Duke in basketball',
'Duke lost the basketball game'
]
print(corpus)
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)
print(vectorizer.vocabulary)
corpus.append('I ate a sandwich')
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)
from sklearn.metrics.pairwise import euclidean_distances
Z = vectorizer.fit_transform(corpus).todense()
print('Distance between 1st and 2nd documents:',
euclidean_distances(Z[0], Z[1]))
print('Distance between 1st and 3rd documents:',
euclidean_distances(Z[0], Z[2]))
print('Distance between 2nd and 3rd documents:',
euclidean_distances(Z[1], Z[2]))




