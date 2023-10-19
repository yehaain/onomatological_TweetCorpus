##########################################################################3
import pickle

def save(name, dataset):
    fileObj = open(name, 'wb')
    pickle.dump(dataset,fileObj)
    fileObj.close()

def load(dataset):
    with (open(dataset, "rb")) as openfile:
        f = pickle.load(openfile)
    return f

import csv

def save_csv(dataset):
    with open(dataset, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile)
        for item in pos_patterns:
            csvwriter.writerow(item)

##########################################################################3
import twint #https://github.com/twintproject/twint

# Sample Number
sample_numbers = []
for profile in dataset:
    sample_number = profile['sampled_number']
    if sample_number is not None: sample_numbers.append(sample_number)
    else                        : sample_numbers.append(0)
sum(sample_numbers)            #379610

# Languages
languages = {}
for profile in dataset:
    if profile['tweet_samplelist'] is not None:
        for tweet in profile['tweet_samplelist']:
            try   : languages[tweet.lang] += 1
            except: languages[tweet.lang]  = 1
    else: pass
    #{'ja': 20159, 'und': 23556, 'en': 253720, 'nl': 7785, 'es': 20180, 'et': 486, 'ro': 477, 'sv': 2016,
    # 'it': 2079, 'in': 3322, 'el': 221, 'ht': 417, 'pt': 8998, 'hu': 448, 'fr': 8490, 'fi': 601,
    # 'de': 5404, 'tl': 1252, 'lt': 145, 'ru': 5393, 'uk': 358, 'sr': 11, 'is': 175, 'no': 1079,
    # 'da': 758, 'lv': 71, 'tr': 421, 'pl': 577, 'ca': 563, 'cy': 260, 'zh': 3739, 'cs': 359, 'eu': 143,
    # 'hi': 155, 'ar': 2557, 'vi': 79, 'ur': 97, 'fa': 486, 'bg': 57, 'ml': 3, 'sl': 128, 'ko': 1475,
    # 'th': 449, 'iw': 387, 'te': 2, 'hy': 1, 'bn': 1, 'kn': 1, 'my': 2, 'ne': 19, 'lo': 1, 'ta': 47}            
    # consistir isso com proporćão de utilizadores por lingua
#CONSISTIR com Twitter Data: https://www.omnicoreagency.com/twitter-statistics/

    
# English Partition
english_partition = []
for profile in dataset:
    if profile['tweet_samplelist'] is not None:
        for tweet in profile['tweet_samplelist']:
            if tweet.lang == 'en': english_partition.append(tweet)
    else: pass

len(english_partition) #253720

save('english(plain).pik', english_partition)

handles = {}
for tweet in english_partition:
    try: handles[tweet.username] += 1
    except: handles[tweet.username] = 0
len(handles) #2172

import numpy as np
np.mean(list(handles.values()))   #115.81399631675875
np.std(list(handles.values()))    #149.2847786775428
np.median(list(handles.values())) #22.0
np.max(list(handles.values()))    #799
np.min(list(handles.values()))    #0

repeated, tweets = [], []
for i, tweet in enumerate(english_partition):
  print(f'\r {i}', end='')
  if tweet in tweets: repeated.append(tweet)
  texts.append(tweet)

non_repeating = []
for i, tweet in enumerate(english_partition):
  print(f'\r {i}', end='')
  if record['twint'] not in repeated: non_repeating.append(tweet['twint'])
len(non_repeating) #247075; 6645 repeated tweets

save('english(plain).pik', non_repeating)

##########################################################################3
# ANNOTATIONS #

english_partition = load('english(plain).pik')

corpus = []
for tweet in english_partition:
    record = {'twint': tweet}
    corpus.append(record)

save('english_corpus.pik', corpus)

import CMUTweetTagger #https://github.com/ianozsvald/ark-tweet-nlp-python/blob/master/CMUTweetTagger.py

tweets = []
for record in corpus: tweets.append(record['twint'].tweet)

pos = CMUTweetTagger.runtagger_parse(tweets)
for record, p in zip(corpus, pos): record['ark'] = p

save('english_corpus.pik', corpus)

import ftfy
fixed_corpus = []
for record in corpus:
    fixed_record = {'twint': record['twint'],
                    'ark'  : []}
    for token in record['ark']:
        fixed_record['ark'].append([ftfy.fix_text(token[0]), token[1], float(token[2])])
    fixed_corpus.append(fixed_record)

save('english_corpus.pik', fixed_corpus)

#Frequencies, concordances and collocations
frequencia_palavras, frequencia_tags = {}, {}
for record in corpus:
    for token in record['ark']:
#
        try   : frequencia_palavras[token[0].lower()] += 1
        except: frequencia_palavras[token[0].lower()] = 1
#
        try   : frequencia_tags[token[1]] += 1
        except: frequencia_tags[token[1]] = 1
    
len(frequencia_palavras) # types = 335470
sum(list(frequencia_palavras.values())) # tokens = 4,412,656

sorted(frequencia_tags.items(), key=lambda x:x[1], reverse=True)
#[('N', 727902), ('V', 672228), (',', 535007), ('P', 461593), ('D', 333408), ('A', 268751),
#('^', 252965), ('O', 246276), ('R', 207692), ('@', 196244), ('U', 111286), ('&', 93785),
#('$', 73319), ('#', 58485), ('L', 55074), ('!', 35020), ('T', 20704), ('G', 19546),
#('E', 18104), ('~', 9391), ('Z', 8455), ('X', 4939), ('S', 2422), ('Y', 60)]


corpus = load('english_corpus.pik')

pos_strings = []
for record in corpus:
    pos_strings.append(''.join([c[1] for c in record['ark']]))


from statistics import mean, median, pstdev

pos_patterns = {}
for p in pos_strings:
    try   : pos_patterns[p] += 1
    except: pos_patterns[p] = 1
pos_patterns = sorted(list(pos_patterns.items()), key = lambda x: x[1], reverse=True)

save_csv('pos_patterns_fullMatch.csv')

len(pos_patterns) #215,517 de 247,075 (31558 padrões)

pos_patterns_values = [p[1] for p in pos_patterns]
print(f'{median(pos_patterns_values)}, {mean(pos_patterns_values)}, \
        {pstdev(pos_patterns_values)}, {max(pos_patterns_values)}, \
        {min(pos_patterns_values)}')
# 1, 1.1464292840007981, 2.846019964900234, 428, 1

pos_patterns[0:7296] #pelo menos duas ocorrências no corpus

import csv, string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(width=900,height=500, max_words=215517,relative_scaling=1, background_color="white",
                      normalize_plurals=False).generate_from_frequencies({p[0]:int(p[1]) for p in pos_patterns})

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off"); plt.show()

pos_patterns[:10]
#[('OVDANP^U', 428), ('@!,', 346), ('RVDNU', 306), ('DN#P$,$N&$NV,U', 298), ('@AN,', 289), ('@N,', 261), ('@A,', 228), ('@A', 220), ('@VO,', 220), ('@!', 210)]

##########################################################################3
# LEXICO #

corpus = load('english_corpus.pik')

import csv

frequencias = {}
for record in corpus:
    for token in record['ark']:
        token = list(token)
        if token[1] == '@': token[0] = '@USER' #for anonymizing
#        
        try   : frequencias[(token[0].lower(), token[1])] += 1
        except: frequencias[(token[0].lower(), token[1])] = 1

with open('english_lexicon.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    for item in list(frequencias.items()):
        csvwriter.writerow([item[0][0], item[0][1], item[1]])
        
##########################################################################3

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
stopwords = list(stopwords.words('english'))
import string
punctuation = [s for s in string.punctuation]

broadTweet_df = pd.read_json('https://raw.githubusercontent.com/GateNLP/broad_twitter_corpus/master/a.json', lines = True)
tokens = broadTweet_df['text'].str.split()

freqs_BT = list(pd.DataFrame(tokens).explode('text').value_counts().to_dict().items())
filtered_BT = [f for f in freqs_BT if str(f[0][0]).lower() not in stopwords and f[0][0] not in punctuation]

wordcloud = WordCloud(width=900,height=500, max_words=215517, background_color="white",
                      normalize_plurals=False).generate_from_frequencies({str(p[0][0]):int(p[1]) for p in filtered_BT})
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off"); plt.show()


freqs_OT = pd.read_csv('english_lexicon.csv')
freqs_OT.columns = ['token', 'pos', 'frequency']

a = freqs_OT[['token','frequency']].values.tolist()
a[2][0].lower()

filtered_OT = [f for f in freqs_OT[['token','frequency']].values.tolist() if str(f[0]).lower() not in stopwords and f[0] not in punctuation]

wordcloud = WordCloud(width=900,height=500, max_words=215517, background_color="white",
                      normalize_plurals=False).generate_from_frequencies({str(p[0]):int(p[1]) for p in filtered_OT})
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off"); plt.show()



