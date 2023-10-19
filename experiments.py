
import pickle
def save(name, dataset):
    fileObj = open(name, 'wb')
    pickle.dump(dataset,fileObj)
    fileObj.close()

def load(dataset):
    with (open(dataset, "rb")) as openfile:
        f = pickle.load(openfile)
    return f

######################################################################
# EXPERIMENTO 1 #        
nonNeutral_adjectives = ['angry', 'worst', 'beautiful', 'bitter', 'black', 'bland', 'bloody', 'bold', 'brave', 'bright', 'broad', 'busy', 'calm', 'cheap', 'classy', 'clean', 'clear', 'clever', 'clumsy', 'cold', 'cool', 'crazy', 'creepy', 'cruel', 'cute', 'dark', 'deadly', 'difficult', 'dirty', 'dry', 'dull', 'dumb', 'dusty', 'early', 'easy', 'expensive', 'faint', 'fair', 'far', 'fast', 'few', 'filthy', 'fine', 'firm', 'fit', 'flat', 'fresh', 'friendly', 'full', 'funny', 'gentle', 'good', 'best', 'grand', 'great', 'greatest', 'guilty', 'handy', 'happy', 'hard', 'harsh', 'healthy', 'heavy', 'high', 'hot', 'humble', 'icy', 'interesting', 'kind', 'large', 'late', 'latest', 'lazy', 'light', 'little', 'lively', 'lonely', 'long', 'loud', 'lovely', 'mad', 'mean', 'messy', 'mild', 'modern', 'narrow', 'nasty', 'naughty', 'near', 'new', 'nice', 'odd', 'old', 'plain', 'poor', 'popular', 'pretty', 'proud', 'pure', 'quick', 'rare', 'raw', 'rich', 'rough', 'rude', 'sad', 'safe', 'scary', 'shallow', 'sharp', 'shy', 'silly', 'sincere', 'slow', 'small', 'smart', 'smooth', 'soft', 'sorry', 'sour', 'strange', 'strong', 'sweet', 'thick', 'thin', 'tired', 'tough', 'true', 'ugly', 'warm', 'weak', 'wealthy', 'weird', 'wet', 'wide', 'wild', 'wise', 'worthy', 'young']
nonNeutral_adverbs = ['adventurously', 'anxiously', 'awkwardly', 'beautifully', 'bitterly', 'bleakly', 'blindly', 'boldly', 'bravely', 'brightly', 'broadly', 'busily', 'calmly', 'carefully', 'carelessly', 'certainly', 'cheerfully', 'clearly', 'cleverly', 'colorfully', 'commonly', 'coolly', 'cruelly', 'curiously', 'daintily', 'delightfully', 'dimly', 'doubtfully', 'easily', 'elegantly', 'exactly', 'excitedly', 'extremely', 'fairly', 'famously', 'far', 'fast', 'fortunately', 'freely', 'generally', 'gently', 'gladly', 'greatly', 'happily', 'healthily', 'heavily', 'highly', 'honestly', 'innocently', 'intensely', 'interestingly', 'kindly', 'lazily', 'lightly', 'limply', 'lively', 'loosely', 'loudly', 'lovingly', 'loyally', 'madly', 'meaningfully', 'miserably', 'more', 'mostly', 'naturally', 'innocently', 'intensely', 'interestingly', 'kindly', 'lazily', 'less', 'lightly', 'limply', 'lively', 'loosely', 'loudly', 'lovingly', 'loyally', 'madly', 'meaningfully', 'miserably', 'more', 'mostly', 'naturally', 'nearly', 'nicely', 'obediently', 'oddly', 'painfully', 'partially', 'perfectly', 'poorly', 'positively', 'powerfully', 'questionably', 'quickly', 'randomly', 'rarely', 'readily', 'really', 'roughly', 'rudely', 'safely', 'scarily', 'selfishly', 'seriously', 'shakily', 'sharply', 'slowly', 'smoothly', 'softly', 'successfully', 'surprisingly', 'sweetly', 'tensely', 'terribly', 'thoughtfully', 'tightly', 'tremendously', 'truthfully', 'selfishly', 'seriously', 'smoothly', 'successfully', 'surprisingly', 'thoughtfully', 'tremendously', 'truthfully', 'unexpectedly', 'unfortunately', 'unnecessarily', 'uselessly', 'usually', 'vaguely', 'very', 'viciously', 'violently', 'warmly', 'weakly', 'wetly', 'wildly', 'wisely', 'wonderfully', 'wrongly']
nonNeutral_emojis = [':COOL_button:', ':FREE_button:', ':Japanese_free_of_charge_button:', ':Japanese_not_free_of_charge_button:', ':Japanese_secret_button:', ':Japanese_secret_button:', ':NEW_button:', ':New_Caledonia:', ':New_Zealand:', ':OK_button:', ':OK_hand:', ':O_button_(blood_type):', ':O_button_(blood_type):', ':P_button:', ':P_button:', ':Papua_New_Guinea:', ':TOP_arrow:', ':alien:', ':alien_monster:', ':anger_symbol:', ':angry_face:', ':angry_face_with_horns:', ':anxious_face_with_sweat:', ':backhand_index_pointing_down:', ':backhand_index_pointing_right:', ':black_cat:', ':black_circle:', ':black_flag:', ':black_heart:', ':black_large_square:', ':black_medium-small_square:', ':black_medium_square:', ':black_medium_square:', ':black_nib:', ':black_nib:', ':black_small_square:', ':black_small_square:', ':black_square_button:', ':bright_button:', ':broken_heart:', ':cat_with_tears_of_joy:', ':cat_with_wry_smile:', ':chicken:', ':closed_book:', ':closed_mailbox_with_lowered_flag:', ':closed_mailbox_with_raised_flag:', ':closed_umbrella:', ':cold_face:', ':confused_face:', ':cow:', ':cow_face:', ':cricket_game:', ':crying_cat:', ':crying_face:', ':dim_button:', ':disappointed_face:', ':down_arrow:', ':down_arrow:', ':empty_nest:', ':face_with_tears_of_joy:', ':fast_down_button:', ':fast_reverse_button:', ':fast_up_button:', ':fearful_face:', ':first_quarter_moon:', ':first_quarter_moon_face:', ':flat_shoe:', ':fly:', ':full_moon:', ':full_moon_face:', ':game_die:', ':green_apple:', ':green_book:', ':green_circle:', ':green_heart:', ':green_salad:', ':green_square:', ':heavy_dollar_sign:', ':heavy_equals_sign:', ':high_voltage:', ':hollow_red_circle:', ':horizontal_traffic_light:', ':hot_beverage:', ':hot_dog:', ':hot_face:', ':hot_pepper:', ':hot_pepper:', ':hot_springs:', ':hot_springs:', ':kissing_face_with_closed_eyes:', ':large_blue_diamond:', ':large_orange_diamond:', ':leafy_green:', ':left_arrow_curving_right:', ':left_arrow_curving_right:', ':light_bulb:', ':light_rail:', ':long_drum:', ':loudly_crying_face:', ':love_hotel:', ':love_letter:', ':magic_wand:', ':magnifying_glass_tilted_right:', ':man_gesturing_OK:', ':man_gesturing_OK:', ':military_helmet:', ':military_medal:', ':military_medal:', ':minus:', ':nauseated_face:', ':new_moon:', ':new_moon_face:', ':old_key:', ':old_key:', ':old_man:', ':old_woman:', ':older_person:', ':orthodox_cross:', ':orthodox_cross:', ':palm_down_hand:', ':person_gesturing_OK:', ':polar_bear:', ':polar_bear:', ':police_car_light:', ':pregnant_man:', ':pregnant_person:', ':pregnant_woman:', ':red_triangle_pointed_down:', ':repeat_single_button:', ':right_anger_bubble:', ':right_anger_bubble:', ':right_arrow:', ':right_arrow:', ':right_arrow_curving_down:', ':right_arrow_curving_down:', ':right_arrow_curving_left:', ':right_arrow_curving_left:', ':right_arrow_curving_up:', ':right_arrow_curving_up:', ':roasted_sweet_potato:', ':rose:', ':round_pushpin:', ':sad_but_relieved_face:', ':shallow_pan_of_food:', ':slightly_frowning_face:', ':slightly_smiling_face:', ':small_airplane:', ':small_airplane:', ':small_blue_diamond:', ':small_orange_diamond:', ':soft_ice_cream:', ':speaker_high_volume:', ':straight_ruler:', ':sun_behind_cloud:', ':sun_behind_large_cloud:', ':sun_behind_large_cloud:', ':sun_behind_rain_cloud:', ':sun_behind_rain_cloud:', ':sun_behind_small_cloud:', ':sun_behind_small_cloud:', ':thumbs_down:', ':tired_face:', ':top_hat:', ':vertical_traffic_light:', ':video_game:', ':white_large_square:', ':white_small_square:', ':white_small_square:', ':woman_gesturing_OK:', ':woman_gesturing_OK:', ':yarn:']

from textblob import TextBlob

def filter_sentiment(word_list):
  filtered_words = []
  for s in word_list.split(','):
    blob = TextBlob(s)
    if blob.polarity != 0 and blob.subjectivity != 0: 
      filtered_words.append(s)
  return filtered_words

nonNeutral_adjectives = filter_sentiment(adjectives)  # de 30133 para 1630
nonNeutral_adverbs    = filter_sentiment(adverbs)     # de 5099 para 726
nonNeutral_verbs      = filter_sentiment(verbs)       # de 28126 para 863

filtered_emojis = [f.replace(' ', '_') for f in filter_sentiment(emojis.replace('_', ' '))]


import math, random
import emoji

from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
from nltk.tokenize import RegexpTokenizer
word_tokenizer = RegexpTokenizer(r'\w+')

from textblob import TextBlob

def prepare_source(tweet):
  source = {'raw'         : tweet,
            'polarity'    : '',
            'subjectivity': '',
            'filtered'    : ''}
  source['polarity'], source['subjectivity'] = TextBlob(source['raw']).sentiment
  source['filtered'] = [s for s in word_tokenizer.tokenize(source['raw']) if s not in en_stops]
  return source

def gatherSentimentCandidates(source, nonNeutral_words):
  candidates_blob = []
  for s in nonNeutral_words:
    blob = TextBlob(s)
    if source['polarity']-.10 <= blob.polarity <= source['polarity']+.10 \
    and source['subjectivity']-.10 <= blob.subjectivity <= source['subjectivity']+.10:
      candidates_blob.append(blob)

  filtered_candidates = {}
  for c in candidates_blob:
    filtered_candidates[c.raw] = math.fabs((c.polarity - source['polarity']) + (c.subjectivity - source['subjectivity']))

#  if len(filtered_candidates.items()) > 1:
#    minimo = min(filtered_candidates.items())[1]
#    best_match = [i for i in filtered_candidates if filtered_candidates[i] == minimo]
#    return best_match
#  else: return list(filtered_candidates.keys())
  return list(filtered_candidates.keys())

def gatherContentCandidates(source, nonNeutral_emojis):
  matched_emojis = []
  for s in source['filtered']:
    for e in emojis.split(','):
      if s in e: 
        matched_emojis.append(e)
  return list(set(matched_emojis))
   
# def build(adverb_list, adjective_list, emoji_list):
def build(adverb_list, adjective_list):
  if   len(adverb_list) == 0 : adverb    = ''
  elif len(adverb_list) == 1 : adverb    = adverb_list[0]
  elif len(adverb_list) > 1  : adverb    = random.choice(adverb_list)

  if   len(adjective_list) == 0 : adjective    = ''
  elif len(adjective_list) == 1 : adjective    = adjective_list[0]
  elif len(adjective_list) > 1  : adjective    = random.choice(adjective_list)

  # if   len(emoji_list) == 0 : emoticon    = ''
  # elif len(emoji_list) == 1 : emoticon    = emoji_list[0]
  # elif len(emoji_list) > 1  : emoticon    = random.choice(emoji_list)

  # return ' '.join([adverb, adjective, emoji.emojize(emoticon,delimiters =(':',':'))])
  return ' '.join([adverb, adjective])



def reply_itemwize(tweet):
  source = prepare_source(tweet)
  matched_adjectives = gatherSentimentCandidates(source, nonNeutral_adjectives)
  matched_adverbs    = gatherSentimentCandidates(source, nonNeutral_adverbs)
  #matched_emojis     = gatherContentCandidates(source, nonNeutral_emojis)
  #matched_emojis   = [f.replace(' ', '_') for f in gatherSentimentCandidates(source, [f.replace('_', ' ') for f in nonNeutral_emojis])]

  #reply = build(matched_adjectives, matched_adverbs, matched_emojis)
  reply = build(matched_adjectives, matched_adverbs)
  return reply 

######################################################################
# EXPERIMENTO 2 #        

import csv

lexicon = []
with open('english_lexicon.csv', mode ='r')as file:
  csvFile, l = csv.reader(file), []
  for line in csvFile: l.append(line)
  for i in l         : lexicon.append([i[0], i[1], int(i[2])])
  
adjectives, adverbs, emojis = [], [], []
for l in lexicon:
  if l[1] == 'A': adjectives.append([l[0], l[2]])
  if l[1] == 'R': adverbs.append([l[0], l[2]])
  if l[1] == 'E': emojis.append([l[0], l[2]])
  
#sorted(adjectives, key=lambda x:x[1], reverse=True)

import emoji
from textblob import TextBlob

from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
from nltk.tokenize import TweetTokenizer
tweet_tokenizer = TweetTokenizer()

def prepare_source(tweet):
  source = {'raw'         : tweet,
            'polarity'    : '',
            'subjectivity': '',
            'filtered'    : ''}
  source['polarity'], source['subjectivity'] = TextBlob(source['raw']).sentiment
  source['filtered'] = [s for s in tweet_tokenizer.tokenize(source['raw']) if s not in en_stops]
  return source

source_tweet = '''"Look both ways" on Netflix is such a good and heart warming movie. Love it!'''
source_tweet = prepare_source(source_tweet)

######################################################################
# EXPERIMENTO 3 #        
import csv

pos = []
with open('pos_patterns_fullMatch.csv', mode ='r')as file:
  csvFile, l = csv.reader(file), []
  for line in csvFile: l.append(line)
  for i in l         : pos.append([i[0], int(i[1])])

place, places = 1, {}
for p in pos:
  if p[1] not in places.keys(): 
    places[p[1]] = place
    place += 1	
places[64]  #53
places[74]  #43
places[228] #7

frq = {}
for p in pos:
  if p[1] in frq.keys(): frq[p[1]] += 1
  else: frq[p[1]] = 1

import pandas as pd
pos_df = pd.DataFrame(pos)

pos_df[1].quantile(q=0.9997)#64.0
os_df[1].quantile(q=0.99997)#224.27616000012495





ocurrencesXfrequencies = {}
for p in pos:
...   if p[1] in frq.keys(): ocurrencesXfrequencies[p[1]] += 1
...   else: ocurrencesXfrequencies[p[1]] = 1

ocurrencesXfrequencies = {428: 1, 346: 1, 306: 1, 298: 1, 289: 1, 261: 1, 228: 1, 220: 2, 210: 1, 206: 1, 188: 1, 185: 1, 181: 1, 177: 1, 165: 1, 154: 1, 140: 1, 139: 1, 124: 1, 123: 1, 120: 1, 118: 1, 114: 1, 112: 1, 111: 1, 110: 1, 109: 1, 103: 1, 101: 1, 99: 1, 98: 1, 94: 1, 91: 1, 90: 2, 89: 1, 88: 1, 86: 1, 85: 1, 84: 2, 83: 1, 80: 1, 79: 1, 74: 3, 73: 1, 72: 1, 71: 2, 70: 3, 69: 1, 68: 2, 67: 1, 66: 2, 65: 1, 64: 4, 63: 1, 62: 1, 61: 1, 60: 1, 59: 1, 58: 2, 57: 2, 56: 2, 55: 1, 54: 3, 53: 1, 52: 1, 51: 2, 49: 1, 48: 2, 47: 2, 46: 5, 45: 4, 44: 5, 43: 4, 42: 5, 41: 2, 40: 1, 39: 3, 38: 2, 37: 3, 36: 2, 35: 5, 34: 1, 33: 2, 32: 6, 31: 9, 30: 6, 29: 8, 28: 16, 27: 9, 26: 7, 25: 8, 24: 6, 23: 11, 22: 14, 21: 10, 20: 14, 19: 14, 18: 26, 17: 21, 16: 30, 15: 34, 14: 38, 13: 41, 12: 44, 11: 47, 10: 72, 9: 75, 8: 108, 7: 136, 6: 238, 5: 325, 4: 547, 3: 1130, 2: 4113, 1: 208220}


for k,v in ocurrencesXfrequencies.items(): print(f'{k} & {v[0]} & {v[1]}% \\')



from nltk.metrics.distance import jaccard_distance
groups = []
for i, o in enumerate(pos):
  print(i, end='\r')
  distance = []
  for p in pos: distance.append([p[0], jaccard_distance(set(o[0]), set(p[0]))])
  
  group = []
  for d, p in zip(distance, pos):
    if d[1] == 0: 
      group.append(d[0]) 
      distance.remove(d)
      pos.remove(p)
  groups.append(group)  

save('distance_clusters.pik', groups)
save('remaining_pos.pik', pos)

len(groups) #22555
len(pos)    #22552




pos = []
with open('pos_patterns_fullMatch.csv', mode ='r')as file:
  csvFile, l = csv.reader(file), []
  for line in csvFile: l.append(line)
  for i in l         : pos.append([i[0], int(i[1])])

patterns = []
for g in groups: patterns.append(set(g[0]))

for p in pos: p[0] = set(p[0])

pos_freq = {}
for p in pos:
  if ''.join(list(p[0])) in pos_freq.keys(): pos_freq[''.join(list(p[0]))] += p[1]
  else: pos_freq[''.join(list(p[0]))] = p[1]


unique = load('remaining_pos.pik')

chatGPT = 'APVOVO,,VDN,VR$PDAANP^EE#'

for p in pos:
...   if chatGPT == p[0]: print(p)pos





for oXf in ocurrencesXfrequencies.keys():
  ocurrencesXfrequencies[oXf] = [ocurrencesXfrequencies[oXf], round((ocurrencesXfrequencies[oXf]*100/215517), 4)]
#{428: [1, 0.0005], 346: [1, 0.0005], 306: [1, 0.0005], 298: [1, 0.0005], 289: [1, 0.0005], 261: [1, 0.0005], 228: [1, 0.0005], 220: [2, 0.0009], 210: [1, 0.0005], 206: [1, 0.0005], 188: [1, 0.0005], 185: [1, 0.0005], 181: [1, 0.0005], 177: [1, 0.0005], 165: [1, 0.0005], 154: [1, 0.0005], 140: [1, 0.0005], 139: [1, 0.0005], 124: [1, 0.0005], 123: [1, 0.0005], 120: [1, 0.0005], 118: [1, 0.0005], 114: [1, 0.0005], 112: [1, 0.0005], 111: [1, 0.0005], 110: [1, 0.0005], 109: [1, 0.0005], 103: [1, 0.0005], 101: [1, 0.0005], 99: [1, 0.0005], 98: [1, 0.0005], 94: [1, 0.0005], 91: [1, 0.0005], 90: [2, 0.0009], 89: [1, 0.0005], 88: [1, 0.0005], 86: [1, 0.0005], 85: [1, 0.0005], 84: [2, 0.0009], 83: [1, 0.0005], 80: [1, 0.0005], 79: [1, 0.0005], 74: [3, 0.0014], 73: [1, 0.0005], 72: [1, 0.0005], 71: [2, 0.0009], 70: [3, 0.0014], 69: [1, 0.0005], 68: [2, 0.0009], 67: [1, 0.0005], 66: [2, 0.0009], 65: [1, 0.0005], 64: [4, 0.0019], 63: [1, 0.0005], 62: [1, 0.0005], 61: [1, 0.0005], 60: [1, 0.0005], 59: [1, 0.0005], 58: [2, 0.0009], 57: [2, 0.0009], 56: [2, 0.0009], 55: [1, 0.0005], 54: [3, 0.0014], 53: [1, 0.0005], 52: [1, 0.0005], 51: [2, 0.0009], 49: [1, 0.0005], 48: [2, 0.0009], 47: [2, 0.0009], 46: [5, 0.0023], 45: [4, 0.0019], 44: [5, 0.0023], 43: [4, 0.0019], 42: [5, 0.0023], 41: [2, 0.0009], 40: [1, 0.0005], 39: [3, 0.0014], 38: [2, 0.0009], 37: [3, 0.0014], 36: [2, 0.0009], 35: [5, 0.0023], 34: [1, 0.0005], 33: [2, 0.0009], 32: [6, 0.0028], 31: [9, 0.0042], 30: [6, 0.0028], 29: [8, 0.0037], 28: [16, 0.0074], 27: [9, 0.0042], 26: [7, 0.0032], 25: [8, 0.0037], 24: [6, 0.0028], 23: [11, 0.0051], 22: [14, 0.0065], 21: [10, 0.0046], 20: [14, 0.0065], 19: [14, 0.0065], 18: [26, 0.0121], 17: [21, 0.0097], 16: [30, 0.0139], 15: [34, 0.0158], 14: [38, 0.0176], 13: [41, 0.019], 12: [44, 0.0204], 11: [47, 0.0218], 10: [72, 0.0334], 9: [75, 0.0348], 8: [108, 0.0501], 7: [136, 0.0631], 6: [238, 0.1104], 5: [325, 0.1508], 4: [547, 0.2538], 3: [1130, 0.5243], 2: [4113, 1.9084], 1: [208220, 96.6142]}






groups = load('distance_clusters.pik')
unique = load('remaining_pos.pik')

pos_patterns = {}

from nltk.metrics.distance import jaccard_distance
p, c = [{'pattern': set(p[0]) , 'frequency': p[1]} for p in pos], []
for e, i in enumerate([{'pattern': set(p[0]) , 'frequency': p[1]} for p in pos]):
  print(e, end='\r')
  if i['pattern'] in [k['pattern'] for k in c]: break
  for j in p:
    if jaccard_distance(i['pattern'], j['pattern']) == 0:
      i['frequency'] += j['frequency']
      p.remove(j)
  c.append(i)
      
save('distance_clusters2.pik', c)
c = load('distance_clusters2.pik')
c = sorted([(i['pattern'], i['frequency']) for i in c], key=lambda x:x[1], reverse=True)



ocurrencesXfrequencies = {}
for i in c:
   if i[1] in ocurrencesXfrequencies.keys(): ocurrencesXfrequencies[i[1]] += 1
   else: ocurrencesXfrequencies[i[1]] = 1











for i in c:
  if i[0] == set('@A,'): print(i)
#563


for i in c:
  if i[0] == set('ARE'): print(i)

f = 0
for i in pos: f += i[1]
#302612
#247075





for i in c:
  if 'A' in i[0]: print(i)




statistics.median([i[1] for i in d])



d = [(i[0], i[1]) for i in c]


pos_patterns = {}
for g in groups:
  groupFrequency = 0
  for i in g:
    groupFrequency += pos[i]
  pos_patterns[''.join(list(set(i)))] = groupFrequency

statistics.median([a[1] for a in candidates])





len(pos)unique
22552






















import pickle
def save(name, dataset):
    fileObj = open(name, 'wb')
    pickle.dump(dataset,fileObj)
    fileObj.close()


save('distance_clusters.pik', groups)





jaccard_distance(set('OVVPD^^PDANPDANPD^^U'), set('OVDANP^U'))









215517






import CMUTweetTagger
tweet='Glad to hear you enjoyed it! "Look Both Ways" is definitely one of my favorite heartwarming movies on Netflix ❤ 🎥 #FeelGoodFlicks'
pos = CMUTweetTagger.runtagger_parse([tweet])

tweet = 'Look both ways" on Netflix is such a good and heart warming movie. Love it!'



[[('Look', 'V', '0,9801'), ('both', 'D', '0,9123'), ('ways', 'N', '0,9981'), ('"', ',', '0,9982'), ('on', 'P', '0,9259'), ('Netflix', '^', '0,9980'), ('is', 'V', '0,9938'), ('such', 'X', '0,5394'), ('a', 'D', '0,9956'), ('good', 'A', '0,9960'), ('and', '&', '0,9982'), ('heart', 'N', '0,8134'), ('warming', 'N', '0,8993'), ('movie', 'N', '0,9977'), ('.', ',', '0,9979'), ('Love', 'V', '0,9689'), ('it', 'O', '0,9904'), ('!', ',', '0,9994')]]
VDN,P^VXDA&NNN,VO,


from nltk.metrics.distance import jaro_winkler_similarity
similarity = []
for p in pos:
  similarity.append([p[0], jaro_winkler_similarity('APVOVO,,VDN,VR$PDAANP^EE#', p[0])])
sorted(similarity, key=lambda x:x[1], reverse=True)


len()





  for g in group:
    for p in pos: 
      if p[0] == g: pos.remove(p)
 
 


somar a frequencia de cada cluster



import pickle
def save(name, dataset):
    fileObj = open(name, 'wb')
    pickle.dump(dataset,fileObj)
    fileObj.close()

def load(dataset):
    with (open(dataset, "rb")) as openfile:
        f = pickle.load(openfile)
    return f









import copy
distances_copy = copy.deepcopy(distances)
 
  
  
  
      








pattern = 'APVOVO,,VDN,VR$PDAANP^EE#'

distance = []
for p in pos:
  distance.append([p[0], jaccard_distance(set('A'), set(p[0]))])
distances = sorted(distance, key=lambda x:x[1])




depos pego todos e faço um diff



distances = sorted(distance, key=lambda x:x[1])

quantas ocorrencias por cluestr
eu posso agrupar padroes que tenham distancia 0





APVOVO,,VDN,VR$PDAANP^EE#
P^,OVNNNNPDNP^,#,V^VRVA,^EE$,


import math, random

def gatherSentimentCandidates(source, words):
  candidates = []
  for s in words:
    blob = TextBlob(s[0])
    if source['polarity']-.05 <= blob.polarity <= source['polarity']+.05 \
    and source['subjectivity']-.05 <= blob.subjectivity <= source['subjectivity']+.05:
      candidates.append(s)
  return candidates

adjective_candidades = gatherSentimentCandidates(source_tweet, adjectives)
sorted(adjective_candidades, key=lambda x:x[1], reverse=True)
sorted(adjective_candidades, key=lambda x:x[0])



adverb_candidades = gatherSentimentCandidates(source_tweet, adverbs)
sorted(adverb_candidades, key=lambda x:x[1], reverse=True)


import statistics
def find_Q1(candidates):
  mediana     = statistics.median([a[1] for a in candidates])
  upper_bound = statistics.median([a[1] for a in candidates if a[1] >= mediana])
  q1 = [a for a in candidates if a[1] >= upper_bound]
  return q1

q1_adjectives = find_Q1(adjective_candidades)
q1_adverbs = find_Q1(adverb_candidades)




pos_patterns_fullMatch



#emoji_candidates = gatherSentimentCandidates(source_tweet, nonNeutral_emojis)


def gatherContentCandidates(source, nonNeutral_emojis):
  matched_emojis = []
  for s in source['filtered']:
    for e in emojis:
      if s in emoji.demojize(e).split('_'): 
        matched_emojis.append(e)
  return list(set(matched_emojis))



emoji_candidates = gatherContentCandidates(source_tweet, nonNeutral_emojis)


def build(adverb_list, adjective_list):
  if   len(adverb_list) == 0 : adverb    = ''
  elif len(adverb_list) == 1 : adverb    = adverb_list[0]
  elif len(adverb_list) > 1  : adverb    = random.choice(adverb_list)

  if   len(adjective_list) == 0 : adjective    = ''
  elif len(adjective_list) == 1 : adjective    = adjective_list[0]
  elif len(adjective_list) > 1  : adjective    = random.choice(adjective_list)

  # if   len(emoji_list) == 0 : emoticon    = ''
  # elif len(emoji_list) == 1 : emoticon    = emoji_list[0]
  # elif len(emoji_list) > 1  : emoticon    = random.choice(emoji_list)

  text_tokens = [adverb, adjective]
  random.shuffle(text_tokens)
  
  # return ' '.join([adverb, adjective, emoji.emojize(emoticon,delimiters =(':',':'))])
  return ' '.join(text_tokens)

build([q[0] for q in q1_adverbs], [q[0] for q in q1_adjectives])

'securely incomparable'
'fittingly love'
"safely many's"
'ecologically smooth'

'truthfully bizarre' --> antidoto.. reforćo negativo...


'meaningfully genuine'
'incomparable interestingly'
'accurately safely'
'love truely'

emoji_number, adjective_number, adverb_number, hashtag_number = 0, 0, 0, 0
aa_number, aae_number = 0, 0
for record in corpus:
    pos = [token[1] for token in record['ark']]
    if 'E' in pos: emoji_number += 1              #15385 (6.2%) tweets
    if 'A' in pos: adjective_number += 1          #148603 (60%)
    if 'R' in pos: adverb_number += 1             #120341 (49%)
    if '#' in pos: hashtag_number += 1            #32659 (13%)    
    if 'A' in pos and 'R' in pos               : aa_number += 1  #82841 (33%)
    if 'A' in pos and 'R' in pos and 'E' in pos: aae_number +=1  #5501 (2%)
      
      
hashtag = 0
mention = 0
emoji      
for p in pos:


      
      
      
      
#quantos tweets tem emoji? 15385 de 247075 (6.2%)

5501 * 100 / 247075

https://stackoverflow.com/questions/52154875/translate-unicode-emojis-to-ascii-emojis-in-python











import statistics
statistics.median([a[1] for a in adjective_candidades])



#nonNeutral_adjectives = ['angry', 'worst', 'beautiful', 'bitter', 'black', 'bland', 'bloody', 'bold', 'brave', 'bright', 'broad', 'busy', 'calm', 'cheap', 'classy', 'clean', 'clear', 'clever', 'clumsy', 'cold', 'cool', 'crazy', 'creepy', 'cruel', 'cute', 'dark', 'deadly', 'difficult', 'dirty', 'dry', 'dull', 'dumb', 'dusty', 'early', 'easy', 'expensive', 'faint', 'fair', 'far', 'fast', 'few', 'filthy', 'fine', 'firm', 'fit', 'flat', 'fresh', 'friendly', 'full', 'funny', 'gentle', 'good', 'best', 'grand', 'great', 'greatest', 'guilty', 'handy', 'happy', 'hard', 'harsh', 'healthy', 'heavy', 'high', 'hot', 'humble', 'icy', 'interesting', 'kind', 'large', 'late', 'latest', 'lazy', 'light', 'little', 'lively', 'lonely', 'long', 'loud', 'lovely', 'mad', 'mean', 'messy', 'mild', 'modern', 'narrow', 'nasty', 'naughty', 'near', 'new', 'nice', 'odd', 'old', 'plain', 'poor', 'popular', 'pretty', 'proud', 'pure', 'quick', 'rare', 'raw', 'rich', 'rough', 'rude', 'sad', 'safe', 'scary', 'shallow', 'sharp', 'shy', 'silly', 'sincere', 'slow', 'small', 'smart', 'smooth', 'soft', 'sorry', 'sour', 'strange', 'strong', 'sweet', 'thick', 'thin', 'tired', 'tough', 'true', 'ugly', 'warm', 'weak', 'wealthy', 'weird', 'wet', 'wide', 'wild', 'wise', 'worthy', 'young']
#nonNeutral_adverbs = ['adventurously', 'anxiously', 'awkwardly', 'beautifully', 'bitterly', 'bleakly', 'blindly', 'boldly', 'bravely', 'brightly', 'broadly', 'busily', 'calmly', 'carefully', 'carelessly', 'certainly', 'cheerfully', 'clearly', 'cleverly', 'colorfully', 'commonly', 'coolly', 'cruelly', 'curiously', 'daintily', 'delightfully', 'dimly', 'doubtfully', 'easily', 'elegantly', 'exactly', 'excitedly', 'extremely', 'fairly', 'famously', 'far', 'fast', 'fortunately', 'freely', 'generally', 'gently', 'gladly', 'greatly', 'happily', 'healthily', 'heavily', 'highly', 'honestly', 'innocently', 'intensely', 'interestingly', 'kindly', 'lazily', 'lightly', 'limply', 'lively', 'loosely', 'loudly', 'lovingly', 'loyally', 'madly', 'meaningfully', 'miserably', 'more', 'mostly', 'naturally', 'innocently', 'intensely', 'interestingly', 'kindly', 'lazily', 'less', 'lightly', 'limply', 'lively', 'loosely', 'loudly', 'lovingly', 'loyally', 'madly', 'meaningfully', 'miserably', 'more', 'mostly', 'naturally', 'nearly', 'nicely', 'obediently', 'oddly', 'painfully', 'partially', 'perfectly', 'poorly', 'positively', 'powerfully', 'questionably', 'quickly', 'randomly', 'rarely', 'readily', 'really', 'roughly', 'rudely', 'safely', 'scarily', 'selfishly', 'seriously', 'shakily', 'sharply', 'slowly', 'smoothly', 'softly', 'successfully', 'surprisingly', 'sweetly', 'tensely', 'terribly', 'thoughtfully', 'tightly', 'tremendously', 'truthfully', 'selfishly', 'seriously', 'smoothly', 'successfully', 'surprisingly', 'thoughtfully', 'tremendously', 'truthfully', 'unexpectedly', 'unfortunately', 'unnecessarily', 'uselessly', 'usually', 'vaguely', 'very', 'viciously', 'violently', 'warmly', 'weakly', 'wetly', 'wildly', 'wisely', 'wonderfully', 'wrongly']
nonNeutral_emojis = [':COOL_button:', ':FREE_button:', ':Japanese_free_of_charge_button:', ':Japanese_not_free_of_charge_button:', ':Japanese_secret_button:', ':Japanese_secret_button:', ':NEW_button:', ':New_Caledonia:', ':New_Zealand:', ':OK_button:', ':OK_hand:', ':O_button_(blood_type):', ':O_button_(blood_type):', ':P_button:', ':P_button:', ':Papua_New_Guinea:', ':TOP_arrow:', ':alien:', ':alien_monster:', ':anger_symbol:', ':angry_face:', ':angry_face_with_horns:', ':anxious_face_with_sweat:', ':backhand_index_pointing_down:', ':backhand_index_pointing_right:', ':black_cat:', ':black_circle:', ':black_flag:', ':black_heart:', ':black_large_square:', ':black_medium-small_square:', ':black_medium_square:', ':black_medium_square:', ':black_nib:', ':black_nib:', ':black_small_square:', ':black_small_square:', ':black_square_button:', ':bright_button:', ':broken_heart:', ':cat_with_tears_of_joy:', ':cat_with_wry_smile:', ':chicken:', ':closed_book:', ':closed_mailbox_with_lowered_flag:', ':closed_mailbox_with_raised_flag:', ':closed_umbrella:', ':cold_face:', ':confused_face:', ':cow:', ':cow_face:', ':cricket_game:', ':crying_cat:', ':crying_face:', ':dim_button:', ':disappointed_face:', ':down_arrow:', ':down_arrow:', ':empty_nest:', ':face_with_tears_of_joy:', ':fast_down_button:', ':fast_reverse_button:', ':fast_up_button:', ':fearful_face:', ':first_quarter_moon:', ':first_quarter_moon_face:', ':flat_shoe:', ':fly:', ':full_moon:', ':full_moon_face:', ':game_die:', ':green_apple:', ':green_book:', ':green_circle:', ':green_heart:', ':green_salad:', ':green_square:', ':heavy_dollar_sign:', ':heavy_equals_sign:', ':high_voltage:', ':hollow_red_circle:', ':horizontal_traffic_light:', ':hot_beverage:', ':hot_dog:', ':hot_face:', ':hot_pepper:', ':hot_pepper:', ':hot_springs:', ':hot_springs:', ':kissing_face_with_closed_eyes:', ':large_blue_diamond:', ':large_orange_diamond:', ':leafy_green:', ':left_arrow_curving_right:', ':left_arrow_curving_right:', ':light_bulb:', ':light_rail:', ':long_drum:', ':loudly_crying_face:', ':love_hotel:', ':love_letter:', ':magic_wand:', ':magnifying_glass_tilted_right:', ':man_gesturing_OK:', ':man_gesturing_OK:', ':military_helmet:', ':military_medal:', ':military_medal:', ':minus:', ':nauseated_face:', ':new_moon:', ':new_moon_face:', ':old_key:', ':old_key:', ':old_man:', ':old_woman:', ':older_person:', ':orthodox_cross:', ':orthodox_cross:', ':palm_down_hand:', ':person_gesturing_OK:', ':polar_bear:', ':polar_bear:', ':police_car_light:', ':pregnant_man:', ':pregnant_person:', ':pregnant_woman:', ':red_triangle_pointed_down:', ':repeat_single_button:', ':right_anger_bubble:', ':right_anger_bubble:', ':right_arrow:', ':right_arrow:', ':right_arrow_curving_down:', ':right_arrow_curving_down:', ':right_arrow_curving_left:', ':right_arrow_curving_left:', ':right_arrow_curving_up:', ':right_arrow_curving_up:', ':roasted_sweet_potato:', ':rose:', ':round_pushpin:', ':sad_but_relieved_face:', ':shallow_pan_of_food:', ':slightly_frowning_face:', ':slightly_smiling_face:', ':small_airplane:', ':small_airplane:', ':small_blue_diamond:', ':small_orange_diamond:', ':soft_ice_cream:', ':speaker_high_volume:', ':straight_ruler:', ':sun_behind_cloud:', ':sun_behind_large_cloud:', ':sun_behind_large_cloud:', ':sun_behind_rain_cloud:', ':sun_behind_rain_cloud:', ':sun_behind_small_cloud:', ':sun_behind_small_cloud:', ':thumbs_down:', ':tired_face:', ':top_hat:', ':vertical_traffic_light:', ':video_game:', ':white_large_square:', ':white_small_square:', ':white_small_square:', ':woman_gesturing_OK:', ':woman_gesturing_OK:', ':yarn:']

with open('/home/yehaain/Dropbox/Kiko/2022/ICAE/adjective_lexicon.txt') as f:
    adjectives = f.readline()
    
with open('/home/yehaain/Dropbox/Kiko/2022/ICAE/adverb_lexicon.txt') as f:
    adverbs = f.readline()

with open('/home/yehaain/Dropbox/Kiko/2022/ICAE/verb_lexicon.txt') as f:
    verbs = f.readline()

import pickle
with (open('/home/yehaain/Dropbox/Kiko/2022/ICAE/english.pik', "rb")) as openfile:
        dataset = pickle.load(openfile)


######################################################################
# EXPERIMENTO 3 #        

verbs, determiners, nouns, conjunctions, punctuations, interjections = [], [], [], [], [], []
for l in lexicon:
  if l[1] == 'V': verbs.append([l[0], l[2]])
  if l[1] == 'D': determiners.append([l[0], l[2]])
  if l[1] == 'N': nouns.append([l[0], l[2]])
  if l[1] == 'P': conjunctions.append([l[0], l[2]])
  if l[1] == ',': punctuations.append([l[0], l[2]])
  if l[1] == '!': interjections.append([l[0], l[2]])

def gatherSentimentCandidates(source, words):
  candidates = []
  for s in words:
    blob = TextBlob(s[0])
    if source['polarity']-.10 <= blob.polarity <= source['polarity']+.10 \
    and source['subjectivity']-.10 <= blob.subjectivity <= source['subjectivity']+.10:
      candidates.append(s)
  return candidates

verb_candidades = gatherSentimentCandidates(source_tweet, verbs)
sorted(verb_candidades, key=lambda x:x[1], reverse=True)
# [['love', 5366], ['enjoy', 800], ['enjoying', 358], ['secure', 61], ['touching', 49], ['fitting', 19], ['#love', 18], ['ok', 16], ['top', 12], ['cool', 8], ['advanced', 7], ['primary', 2], ['fine', 1], ['love-', 1], ['#secure', 1], ['guarded', 1], ['smooth', 1], ['redeeming', 1], ['interesting', 1], ['acquainted', 1], ['appealing', 1], ['safe', 1]]

determiner_candidades = gatherSentimentCandidates(source_tweet, determiners)
sorted(determiner_candidades, key=lambda x:x[1], reverse=True)
# []

noun_candidades = gatherSentimentCandidates(source_tweet, noun)
sorted(noun_candidades, key=lambda x:x[1], reverse=True)







interjection, adjective, noun, punctuation = [], [], [], []
for l in lexicon:
  if   l[1] == '!': interjection.append([l[0], l[2]])
  elif l[1] == 'A': adjective.append([l[0], l[2]])
  elif l[1] == 'N': noun.append([l[0], l[2]])
  elif l[1] == ',': punctuation.append([l[0], l[2]])

def gatherSentimentCandidates(source, words):
  candidates = []
  for s in words:
    blob = TextBlob(s[0])
    if source['polarity']-.10 <= blob.polarity <= source['polarity']+.10 \
    and source['subjectivity']-.10 <= blob.subjectivity <= source['subjectivity']+.10:
      candidates.append(s)
  return candidates

interjection_candidades = gatherSentimentCandidates(source_tweet, interjection)
sorted(interjection_candidades, key=lambda x:x[1], reverse=True)
#[['ok', 740], ['okay', 227], ['cool', 21], ['ok-', 1], ["s'ok", 1]]

adjective_candidades = gatherSentimentCandidates(source_tweet, adjective)
sorted(adjective_candidades, key=lambda x:x[1], reverse=True)
# [['more', 5937], ['many', 2642], ['better', 2306], ['cool', 1420], ['true', 1337], ['full', 1318], ['top', 1207], ['interesting', 1164], ['able', 949], ['safe', 738], ['most', 667], ['special', 575], ['fine', 535], ['sweet', 504], ['ok', 332], ['healthy', 302], ['okay', 186], ['friendly', 147], ['familiar', 131], ['greater', 130], ['appropriate', 129], ['accurate', 125], ['gay', 117], ['primary', 115], ['secure', 108], ['thoughtful', 78], ['meaningful', 77], ['smooth', 73], ['genuine', 72], ['bizarre', 42], ['enjoyable', 38], ['worthwhile', 31], ['fitting', 26], ['iconic', 22], ['sincere', 20], ['appealing', 19], ['skilled', 16], ['notable', 12], ['safely', 6], ['touching', 5], ['phenomenal', 36], ['advanced', 81], ['plausible', 14], ['energetic', 15], ['more-', 3], ['competent', 25], ['love', 1], ['#thoughtful', 1], ['believable', 11], ['incomparable', 4], ['respectable', 8], ['truthful', 10], ['lovable', 3], ['likable', 3], ['more)', 2], ['securely', 1], ['potent', 8], ['nonviolent', 2], ['-more', 1], ['competent-', 1], ['endearing', 2], ['mostly', 1], ['well-off', 1], ["many's", 1], ['#cool', 1], ["thoughtful!'", 1], ['ecological', 1], ['#gay', 2], ['cool!"\'', 1], ['redeeming', 2], ['risk-free', 3], ['-friendly', 3], ['better`', 1], ['more', 5937], ['many', 2642], ['better', 2306], ['cool', 1420], ['true', 1337], ['full', 1318], ['top', 1207], ['interesting', 1164], ['able', 949], ['safe', 738], ['most', 667], ['special', 575], ['fine', 535], ['sweet', 504], ['ok', 332], ['healthy', 302], ['okay', 186], ['friendly', 147], ['familiar', 131], ['greater', 130], ['appropriate', 129], ['accurate', 125], ['gay', 117], ['primary', 115], ['secure', 108], ['thoughtful', 78], ['meaningful', 77], ['smooth', 73], ['genuine', 72], ['bizarre', 42], ['enjoyable', 38], ['worthwhile', 31], ['fitting', 26], ['iconic', 22], ['sincere', 20], ['appealing', 19], ['skilled', 16], ['notable', 12], ['safely', 6], ['touching', 5], ['phenomenal', 36], ['advanced', 81], ['plausible', 14], ['energetic', 15], ['more-', 3], ['competent', 25], ['love', 1], ['#thoughtful', 1], ['believable', 11], ['incomparable', 4], ['respectable', 8], ['truthful', 10], ['lovable', 3], ['likable', 3], ['more)', 2], ['securely', 1], ['potent', 8], ['nonviolent', 2], ['-more', 1], ['competent-', 1], ['endearing', 2], ['mostly', 1], ['well-off', 1], ["many's", 1], ['#cool', 1], ["thoughtful!'", 1], ['ecological', 1], ['#gay', 2], ['cool!"\'', 1], ['redeeming', 2], ['risk-free', 3], ['-friendly', 3], ['better`', 1]]

noun_candidades = gatherSentimentCandidates(source_tweet, noun)
sorted(noun_candidades, key=lambda x:x[1], reverse=True)
#[['love', 1203], ['top', 331], ['iconic', 24], ['#love', 21], ['cool', 17], ['cool', 17], ['special', 15], ['special', 15], ['primary', 10], ['primary', 10], ['advanced', 6], ['advanced', 6], ['more', 5], ['more', 5], ['safe', 3], ['safe', 3], ['love-', 2], ['many', 2], ['love-', 2], ['many', 2], ['#top', 1], ['"interesting', 1], ['ecological', 1], ['guarded', 1], ['love+', 1], ['enjoy', 1], ['fitting', 1], ['greater', 1], ["s'more", 1], ['touching', 1], ["m'love", 1], ['#top', 1], ['"interesting', 1], ['ecological', 1], ['guarded', 1], ['love+', 1], ['enjoy', 1], ['fitting', 1], ['greater', 1], ["s'more", 1], ['touching', 1], ["m'love", 1]]

punctuation_candidades = gatherSentimentCandidates(source_tweet, punctuation)
sorted(punctuation_candidades, key=lambda x:x[1], reverse=True)
# []
# [['.', 180608], [',', 99757], ['!', 54920], ['"', 36750], ['?', 33422], [':', 25863], ['-', 15299], ['...', 13988], [')', 13061], ['(', 12934], ['.', 180608], [',', 99757], ['!', 54920], ['"', 36750], ['?', 33422], [':', 25863], ['-', 15299], ['...', 13988], [')', 13061], ['(', 12934], ["'", 9144], ['!!', 4412], ['…', 3216], ['*', 2889], ['..', 2698], ['!!!', 2316], ['—', 1702], ['....', 1677], ['--', 1150], ['–', 1106], ['[', 1104], [']', 1044], ['/', 1015], ['??', 795], ['=', 791], ['?!', 716], ['!!!!', 568], ['.....', 383], ['???', 377], ['):', 300], ['//', 224], ['😂', 223], ['!?', 216], ['!!!!!', 188], ['......', 140], ["''", 133], ['•', 129], ['🤣', 105], ['?!?', 104], ['♫', 89], ['!!!!!!', 88], ['🤔', 88], ['.…', 86], ['...?', 82], ['.......', 75], ['🚀', 73], ['????', 68], [']:', 67], ['!...', 65], ['>', 62], ['😎', 60], ['🔥', 55], ['.,', 54], ['😆', 54], ['🙄', 53], ['💯', 52], ['👀', 51], ['👏', 48], ['\'"', 47], ['!!!!!!!', 47], ['|', 46], ['?!?!', 46], ['🥰', 46], ['""', 45], ['….', 43], ['(!)', 38], ['😀', 38], ['✅', 37], ['🙂', 36], ['?!!', 35], ['))', 34], ['🙃', 31], ['.........', 30], ['...!', 29], ['..?', 29], ['🙏🏽', 29], ['😂😂', 29], ['?...', 29], ['💕', 26], ['🥺', 25], ['?????', 24], ['👇', 24], ['✔️', 23], ['.!', 20], ['🤯', 20], ['🙈', 20], ['😋', 17], ['??!', 17], ['🇺🇸', 16], ['!,', 16]]

[('OVDANP^U', 428), ('@!,', 346), ('RVDNU', 306), ('DN#P$,$N&$NV,U', 298),
 ('@AN,', 289), ('@N,', 261), ('@A,', 228), ('@A', 220), ('@VO,', 220), ('@!', 210)]


'@!,'   @sm89 ok.
'@AN,'  @sm89 more love.
'@A'    @sm89 many top
'@!'    @sm89 okay







######################################################################3

# tenho que ver no corpus o que costuma vir antes de adjetivos

######################################################################3

import math
import random
import emoji

highly_nonNeutral = []
for tweet in dataset:
    if tweet['polarity'] > .7 and tweet['subjectivity'] > .7:
        highly_nonNeutral.append(tweet)

sample = random.choices(highly_nonNeutral, k=10)

for s in sample:
    print(s['tweet'].tweet, f"\t ({s['polarity']},{s['subjectivity']})")
    print('> ', reply_itemwize(s['tweet'].tweet), end = '\n\n')

















