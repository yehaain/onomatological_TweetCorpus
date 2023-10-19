import csv
import random
import itertools
import math
import time


with open('externalDatasets/firstNames(Filtered).csv') as csv_file:
    name_file = list(csv.DictReader(csv_file))    
    firstNames = [(name_file[j]['Name'],name_file[j]['Gender']) for j in range(0,len(name_file))]
    firstNames = list(set(firstNames))
# print('First Name:',len(firstNames)) #104110

with open('externalDatasets/lastNames.csv') as csv_file:
    name_file = list(csv.DictReader(csv_file))    
    lastNames = [name_file[j]['name'] for j in range(0,len(name_file))]
    lastNames = list(set(lastNames))
# print('Last Name:',len(lastNames)) #162254

#######################################################################################################
# This is a proprietary dataset that cannot be freely distributed yet free for research purposes.     #
# Therefore, for running the following code excerpt, request the American English Nickname Collection #
# on https://catalog.ldc.upenn.edu/LDC2012T11.                                                        #
#                                                                                                     #    
nickNames = []                                                                                        #
with open('externalDatasets/American_English_Nicknames.csv') as csv_file:                             #
    name_file = list(csv.DictReader(csv_file, delimiter=','))                                         #
for name in name_file:                                                                                #
    nickName = {'given': '', 'nick' : []}                                                             #
    nickName['given'] = name['\ufeffNAME'].upper().strip()                                            #
    nickName['nick'].append([name['ALIAS'].upper().strip()])                                          #
    nickName['nick']  = list(itertools.chain(*nickName['nick']))                                      #
    nickNames.append(nickName)                                                                        #
#######################################################################################################

with open("externalDatasets/badWords(2018_07_30).txt") as badword_file:
    blacklist = [badword.strip() for badword in badword_file]

def _matchGender(gender):
    firstName = random.choice(firstNames)
    while firstName[1] != gender:
        firstName = random.choice(firstNames)
    return firstName

def _avoidRepetition(firstname):
    compundname = random.choice(firstNames)
    while compundname[1] == firstname:
        compundname = random.choice(firstNames)
    return compundname
    
def generateName(gender, compoundName, surnames):
    name = {}    
    firstName = _matchGender(gender)
    compound  = _avoidRepetition(firstName)
    
    name['firstName']    = (firstName[0].capitalize() if firstName[1] == gender else None)
    name['compoundName'] = (compound[0].capitalize() if compoundName else '')    
    name['middleName1']  = (random.choice(lastNames).capitalize() if surnames == 3 else '')
    name['middleName2']  = (random.choice(lastNames).capitalize() if surnames >= 2 else '')
    name['lastName']     =  random.choice(lastNames).capitalize()
    name['fullname'] = ' '.join(' '.join(name.values()).split()).strip()         
    name['setup']    = ('Male' if gender == 'M' else 'Female',              \
                        'Compound Name' if compoundName else 'Single Name', \
                        str(surnames) + ' surnames')
    return name

def filterBadWords(candidates):
    return [i for i in candidates if i.lower() not in blacklist]

vowel = ['a','e','i','o','u','y','A','E','I','O','U','Y']

def _isConsonant(letter):
    return True if letter not in vowel else False

def _isVowel(letter):
    return True if letter in vowel else False

def _isCCC(trinomial):
    assert len(trinomial) == 3
    return True if _isConsonant(trinomial[0]) and _isConsonant(trinomial[1])          \
                                              and _isConsonant(trinomial[2]) else False
def _isCCV(trinomial):
    assert len(trinomial) == 3
    return True if _isConsonant(trinomial[0]) and _isConsonant(trinomial[1])          \
                                              and     _isVowel(trinomial[2]) else False
def _isCVC(trinomial):
    assert len(trinomial) == 3
    return True if _isConsonant(trinomial[0]) and     _isVowel(trinomial[1])          \
                                              and _isConsonant(trinomial[2]) else False
def _isCVV(trinomial):
    assert len(trinomial) == 3
    return True if _isConsonant(trinomial[0]) and _isVowel(trinomial[1])          \
                                              and _isVowel(trinomial[2]) else False    
def _isVCC(trinomial):
    assert len(trinomial) == 3
    return True if _isVowel(trinomial[0]) and _isConsonant(trinomial[1])          \
                                          and _isConsonant(trinomial[2]) else False        
def _isVCV(trinomial):
    assert len(trinomial) == 3
    return True if _isVowel(trinomial[0]) and _isConsonant(trinomial[1])          \
                                          and     _isVowel(trinomial[2]) else False        
def _isVVC(trinomial):
    assert len(trinomial) == 3
    return True if _isVowel(trinomial[0]) and     _isVowel(trinomial[1])          \
                                          and _isConsonant(trinomial[2]) else False     
def _isVVV(trinomial):
    assert len(trinomial) == 3
    return True if _isVowel(trinomial[0]) and _isVowel(trinomial[1])          \
                                          and _isVowel(trinomial[2]) else False     


def applySeparation(name):
    innerNames = {'firstName': [], 'compoundName': [], 'middleName1': [], 'middleName2': [], 'lastName': [],}   

    for n in firstNames:
        if n[0] in name['firstName']    and n[0] != name['firstName']   : innerNames['firstName'].append(n[0])
        if n[0] in name['compoundName'] and n[0] != name['compoundName']: innerNames['compoundName'].append(n[0])
        if n[0] in name['middleName1']  and n[0] != name['middleName1'] : innerNames['middleName1'].append(n[0])        
        if n[0] in name['middleName2']  and n[0] != name['middleName2'] : innerNames['middleName2'].append(n[0])                
        if n[0] in name['lastName']     and n[0] != name['lastName']    : innerNames['lastName'].append(n[0])

    for n in lastNames:
        if n.capitalize() in name['firstName']    and n.capitalize() != name['firstName']   : innerNames['firstName'].append(n.capitalize())
        if n.capitalize() in name['compoundName'] and n.capitalize() != name['compoundName']: innerNames['compoundName'].append(n.capitalize())
        if n.capitalize() in name['middleName1']  and n.capitalize() != name['middleName1'] : innerNames['middleName1'].append(n.capitalize())
        if n.capitalize() in name['middleName2']  and n.capitalize() != name['middleName2'] : innerNames['middleName2'].append(n.capitalize())        
        if n.capitalize() in name['lastName']     and n.capitalize() != name['lastName']    : innerNames['lastName'].append(n.capitalize())

    innerNames['firstName']    = sorted(list(set(innerNames['firstName'])))
    innerNames['compoundName'] = sorted(list(set(innerNames['compoundName'])))
    innerNames['middleName1']  = sorted(list(set(innerNames['middleName1'])))
    innerNames['middleName2']  = sorted(list(set(innerNames['middleName2'])))
    innerNames['lastName']     = sorted(list(set(innerNames['lastName'])))
    return innerNames

def applyInitials(name):
    initials = {'firstName'    : [], 'compoundName' : [], 'middleName1'  : [], 'middleName2'  : [], 'lastName'     : [],}    

    initials['firstName'].append(name['firstName'][0] if len(name['firstName']) > 1 else '')
    initials['compoundName'].append(name['compoundName'][0] if len(name['compoundName']) > 1 else '')
    initials['middleName1'].append(name['middleName1'][0] if len(name['middleName1']) > 1 else '')
    initials['middleName2'].append(name['middleName2'][0] if len(name['middleName2']) > 1 else '')
    initials['lastName'].append(name['lastName'][0] if len(name['lastName']) > 1 else '')

    return initials

def _forTheFrontPortion(name):
    candidates = []
    if len(name) >= 3:
        trinomial = name[:3]
      
        if _isCVV(trinomial): 
            candidates.append(('01:',name[:2]))                                            # JO[an]
    #        candidates.append(('29:',name[:3]))                                            # JOA[n]        

        if _isVCC(trinomial): 
            candidates.append(('02:',name[:2]))                                           # AB[ner]
            candidates.append(('03:',name[:3]))                                           # ELW[yn]
            if len(name) > 3:
                if _isVowel(name[3]): candidates.append(('04:',name[:4]))                 # Alli[sson}   
                if name[1] == name[2]: candidates.append(('05:',name[:2]+name[3]))   

        if _isCVC(trinomial): 
            candidates.append(('06:',name[:2]))                                            # DA[niel]        
            candidates.append(('07:',name[:3]))                                            # DAN[iel]
            candidates.append(('08:',name[:4]))                                            # DANI[el]            

        if _isCCV(trinomial): 
            candidates.append(('09:', name[:3]))                                             # CHA[rles]
            if len(name) > 3: candidates.append(('10:',name[:4]))                          # FRED[erick]
            if len(name) > 4 and _isConsonant(name[:4]): candidates.append(('11:',name[:5])) # FRANC[isco]
                
        if _isCCC(trinomial):   
            if len(name) > 4 and _isVowel(name[4]): candidates.append(('12:',name[:5]))    #CHRIS[tine]
                
        if _isVVC(trinomial): 
            if name[0] != name[1]:
                candidates.append(('13:',name[:2]))                                            #AU[drey]
                candidates.append(('14:',name[:3]))                                            #AUD[rey]

        if _isVCV(trinomial): 
            candidates.append(('15:',name[:2]))                                            #AL[aysa]
            candidates.append(('16:',name[:3]))                                            #ALA[ysa]
            if len(name) > 3: candidates.append(('17:',name[:4]))                          #ALAY[sa]       

    #    if _isVVV(trinomial):         
    return candidates

def _forTheBackPortion(name):
    candidates = []
    if len(name) >= 3:
        trinomial = name[-3:]

        if _isCVV(trinomial): 
            candidates.append(('18:',name[-3:]))                                              #[anta]SIA      
            if name[-2] != name[-1]:
                candidates.append(('19:',name[-2:]))                     #[antas]IA
            # if len(name) > 3 and name[-2] != name[-4]: candidates.append(('04:',name[-4:]))   #[ant]ASIA                 

        if _isVCC(trinomial): 
            candidates.append(('20:',name[-3:]))                                              #[suz]ETH
            if len(name) > 3 and name[-2] != name[-4]: candidates.append(('21:',name[-4:]))   #[su]ZETH        

        if _isCVC(trinomial):    
            candidates.append(('22:',name[-2:]))                                              #[kee]LY
            candidates.append(('23:',name[-3:]))                                              #[ke]ELY
            if len(name) > 3 and name[-2] != name[-4]: candidates.append(('24:',name[-4:]))   #mel[FRED]   

        if _isCCV(trinomial): 
            candidates.append(('25:',name[-2:]))                                              #[aubrean]NA
    #        if name[-3] != name[-2]: candidates.append(('26:',name[-3:]))                     #
            if len(name) > 3 and _isVowel(name[-4]): 
                candidates.append(('26:',name[-4:]))                                          #[aubre]ANNA        

#        if _isCCC(trinomial):                                                               
 
        if _isVVC(trinomial): 
            candidates.append(('27:',name[-2:]))                                              #buny[AN]
            candidates.append(('28:',name[-3:]))                                              #bun[YAN]
            if len(name) > 3 and _isConsonant(name[-4]): candidates.append(('52:',name[-4:])) #bu[NYAN]

        if _isVCV(trinomial): 
            candidates.append(('29:',name[-2:]))                                              #[nicoli]NE
            candidates.append(('30:',name[-3:]))                                              #[nicol]INE
            if len(name) > 3 and _isConsonant(name[-4]): candidates.append(('57:',name[-4:])) #[nico]LINE

        if _isVVV(trinomial): 
            candidates.append(('31:',name[-2:]))                                              #[ro]EY
            candidates.append(('32:',name[-3:]))                                              #[ro]EY

    return [(n[0], n[1].capitalize()) for n in candidates]

def _forTheMiddlePortion(name): pass
#        trinomial = name[]: acho que vou excluindo a primeira letra ate chegar na ultima vice-versa

def applyPortion(name):
    portion = {'firstName'    : [], 'compoundName' : [], 'middleName1'  : [], 'middleName2'  : [], 'lastName'     : [],}    
  
    portion['firstName'].append(_forTheFrontPortion(name['firstName']))
    portion['compoundName'].append(_forTheFrontPortion(name['compoundName']))
    portion['middleName1'].append(_forTheFrontPortion(name['middleName1']))
    portion['middleName2'].append(_forTheFrontPortion(name['middleName2']))
    portion['lastName'].append(_forTheFrontPortion(name['lastName']))

#     portion['firstName'].append(_forTheMiddlePortion(name['firstName']))
#     portion['compoundName'].append(_forTheMiddlePortion(name['compoundName']))
#     portion['middleName1'].append(_forTheMiddlePortion(name['middleName1']))
#     portion['middleName2'].append(_forTheMiddlePortion(name['middleName2']))
#     portion['lastName'].append(_forTheMiddlePortion(name['lastName']))

    portion['firstName'].append(_forTheBackPortion(name['firstName']))
    portion['compoundName'].append(_forTheBackPortion(name['compoundName']))
    portion['middleName1'].append(_forTheBackPortion(name['middleName1']))
    portion['middleName2'].append(_forTheBackPortion(name['middleName2']))
    portion['lastName'].append(_forTheBackPortion(name['lastName']))
    
    return portion

def _retrieveFromDataset(name):
    candidates = []
    name = name.upper()
    for n in nickNames:
        if name == n['given']:
            filtered = []
            for i in [i.strip() for i in n['nick'] if i != name]:
                if ' ' in i: i = i.replace(' ', '_')
                filtered.append(i)
            candidates.append(filtered)
    return [n.capitalize() for n in list(itertools.chain(*candidates))]

def applyContraction(name):
    contractions = {'firstName'    : [], 'compoundName' : [], 'middleName1'  : [], 'middleName2'  : [], 'lastName'     : [],}    

    contractions['firstName']    = _retrieveFromDataset(name['firstName'])
    contractions['compoundName'] = _retrieveFromDataset(name['compoundName'])
    contractions['middleName1']  = _retrieveFromDataset(name['middleName1'])
    contractions['middleName2']  = _retrieveFromDataset(name['middleName2'])
    contractions['lastName']     = _retrieveFromDataset(name['lastName'])

    return contractions

def cleanName(name):
  return name['fullname'].split()

def cleanSeparation(separation):
  return list(itertools.chain(*[separation[s] for s in separation.keys()]))

def cleanInitials(initials):
  return list(itertools.chain(*[initials[s] for s in initials.keys()]))

def cleanPortions(portions):
  portions = list(itertools.chain(*[portions[s] for s in portions.keys()]))
  portions = list(itertools.chain(*[s for s in portions]))
  return [s[1] for s in portions]

def cleanContraction(contraction):
  return list(itertools.chain(*[contraction[s] for s in contraction.keys()]))

def sole(name):
  candidates = [n for n in name if 3 < len(n) < 16]
  return candidates

def bind(part1, part2):
  #part1 = separation
  #part2 = initials
  part1 = [i for i in part1 if i != '']
  part2 = [i for i in part2 if i != '']

  candidates = []
  candidates.append(list(itertools.product(part1, part2)))
  candidates.append(list(itertools.product(part2, part1)))
  candidates = list(itertools.chain(*candidates))
  candidates = [''.join(c) for c in candidates]
  candidates  = [n for n in candidates if 3 < len(n) < 16]
  candidates = list(set(candidates))
  return candidates

def generateHandle():
  name = generateName(random.choice(['M','F']), random.choice([True,False]), random.randint(1,3))
  separation   = cleanSeparation(applySeparation(name))
  initials     = cleanInitials(applyInitials(name))
  portions     = cleanPortions(applyPortion(name))
  contraction  = cleanContraction(applyContraction(name))
  name         = cleanName(name)
  generators = [bind(separation, initials), sole(name), bind(initials, portions), sole(separation), bind(contraction, initials)]
  handle_list = random.choice(generators)
  while not (len(handle_list) > 1): handle_list = random.choice(generators)
  handle = random.choice(handle_list)
  return handle
