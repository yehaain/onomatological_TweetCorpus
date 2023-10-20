# Onomatological Tweet Corpus

In order to read the corpus, it is necessary to use Python, an example of which is presented below:

```
>>> import pickle
>>> import twint
>>> def load(dataset):
...    with (open(dataset, "rb")) as openfile:
...        f = pickle.load(openfile)
...    return f
>>>
>>> corpus = load('english_corpus.pik')
>>> 
>>> corpus[0]['twint'].tweet
'got the panels to work. Yippee.'
>>> # for other options refer to: https://github.com/twintproject/twint/wiki/Tweet-attributes
>>>
>>> corpus[0]['ark']
[['got', 'V', 0.9866], ['the', 'D', 0.9995], ['panels', 'N', 0.997], ['to', 'P', 0.9984], ['work', 'N', 0.7365], ['.', ',', 0.9985], ['Yippee', '!', 0.954], ['.', ',', 0.9978]]
```
