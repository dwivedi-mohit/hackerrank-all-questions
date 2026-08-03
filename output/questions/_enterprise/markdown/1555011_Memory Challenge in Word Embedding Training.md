# Memory Challenge in Word Embedding Training

## Metadata

- **ID:** 1555011
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Word Embedding Model, Memory consumption, Hard, Word2Vec Algorithm
- **Skills:** Natural Language Processing (Advanced)

## Summary

This multiple choice question evaluates natural language processing, memory consumption, and the word2vec algorithm concepts, ideal for senior-level roles. The problem requires identifying the cause of an Out of Memory error during the training of a word embedding model.

## Problem Statement

An NLP project trains a word embedding model using the Word2Vec algorithm. Its objective is to represent words as vectors in high-dimensional space to facilitate further analysis and natural language processing tasks as shown in the code below.

`print('Loading Data')
corpus_k = pickle.load(open('../data/keywords_cleaned_100.pkl', 'rb'))
corpus_c = pickle.load(open('../data/corpus_cleaned_100.pkl', 'rb'))

if os.path.exists('../data/y_keyword_retrival.pkl'):
    y = pickle.load(open('../data/y_keyword_retrival.pkl', 'rb'))
else:
    y = []
    for i in range(corpus_c.shape[0]):
        if i % 1000 == 0: print(i)
        t1 = corpus_k[i]
        t2 = corpus_c[i]

        s1 = set(t1)
        l = []
        for word in t2:
            if word in s1:
                l.append('1')
            else:
                l.append('0')
        y.append(l)
    y = np.array(y)
    pickle.dump(y, open('../data/y_keyword_retrival.pkl', 'wb+'))

vec = gensim.models.word2vec.Word2Vec.load('../data/w2v_0428')

weights_file = './model_weights.h5'
params_file = './params.json'
preprocessor_file = './preprocessor.json'

print('Train Test Split ... ')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(corpus_c, y, test_size=0.1, random_state=42)

print('Training ... ')
import anago
model = anago.Sequence(
    word_lstm_size=300,
    word_embedding_dim=300,
    embeddings=vec,
    use_char=False
)
model.fit(X_train, y_train, batch_size=256, epochs=5)
s = model.score(X_test, y_test)
model.save(weights_file, params_file, preprocessor_file)`
```

On execution, it throws an Out of Memory (OOM) error along with a warning message.

 

What is the likely cause?

## Preview

An NLP project trains a word embedding model using the Word2Vec algorithm. It
