import twint
import urllib.request
from datetime import datetime, timedelta
from nltk import regexp_tokenize
from selenium import webdriver
import pickle


def isEnglish(bom):
  if type(bom) == type({}) and  bom['user']      \
     and bom['user']['majority_lang'] == 'en': return True
  else                                      : return False

def scrap(handle, tweet_sample):
  c = twint.Config()
  c.Username = handle
  c.Limit = tweet_sample
  c.Store_object = True
  c.Hide_output  = True
  c.Hide_output  = True
  twint.run.Search(c)
  return twint.output.tweets_list

def getPopulation(handle):   
  try:  
      wb.get('https://twitter.com/'+handle)
      name        = wb.find_element_by_xpath('//h2')
      tweet_count = str(name.find_element_by_xpath("./following-sibling::div").text)
  except Exception as e:
      print(e)
      tweet_count = None
  return tweet_count

def parse(number_of_tweets):
  valor = regexp_tokenize(number_of_tweets, '\d+\.\d+|\w') 
  multiplicador = 1
  if   valor[1] == 'K': multiplicador = 1000
  elif valor[1] == 'M': multiplicador = 1000000
  else: 'ERRO'
  return int(float(valor[0])*multiplicador)

def sample_size(n, z, p, e): 
  return (n * (pow(z, 2) * p * (1-p)/pow(e, 2))) / (n - 1 + (pow(z, 2) * p * (1-p)/pow(e, 2)))

def isSilence(handle, periodo, twint_output):
  until = datetime.today() - timedelta(days=periodo)

  tweet_number = 0
  for t in twint_output:
    if datetime.fromisoformat(t.datestamp) >= until: tweet_number += 1
    else                                           : break
  volume = tweet_number/periodo
  return False if volume >= 0.5 else True

sample_file   = open('sample.pik', 'wb')
faillog_file  = open('fail_log.pik', 'wb')
checklog_file = open('check_log.csv', 'w') #open(file_name, 'a+', newline='') 

checklog_writter = csv.writer(checklog_file)
checklog_writter.writerow(['Handle', 'Shadowban', 'Botometer', 'Silence'])

sample_lenght, i = 0, 1
while sample_lenght <= 1: #385
    candidate = {} 
    # 1. gerar um handle automaticmanete
    handle = generateHandle()
    candidate['handle'] = handle
    print(i, handle, end=',', flush=True)
    i += 1
        
    # 2. verificar o handle para silencio
    passed_silence = None
    n = getPopulation(handle)
    if n: 
        n = parse(n)
        print(' Population Got', end=',', flush=True)
        
        z, p, e = 1.96, 0.5, 0.05                   # confidence: .95, error: .05
        limit = math.ceil(sample_size(n, z, p, e))

        twint_output = scrap(handle, limit)
        candidate['silence'] = twint_output

        periodo = 30
        if isSilence(handle, periodo, twint_output) == False: 
            passed_silence = True
            print(' Passed Silence', flush=True)
        else:
            passed_silence = False
            print(' Fail Silence', flush=True)
    else:
        passed_silence = None
        print(' Fail Silence', flush=True)
        
    # 3. Include in the sample
    checklog_writter.writerow([handle, str(passed_shadowban), str(passed_botometer), str(passed_silence)])
    
    if passed_silence: 
        sample_lenght += 1
        pickle.dump(candidate, sample_file)
    else                                                       : 
        pickle.dump(candidate, faillog_file)

checklog_file.close()
sample_file.close()
faillog_file.close()
wb.close()
