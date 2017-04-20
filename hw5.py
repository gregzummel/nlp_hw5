import nltk, collections
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import nltk
from nltk.chunk import conlltags2tree, tree2conlltags
def readDocuments(document_path):
    #documentpath =
    import codecs
    file = codecs.open(document_path, 'r', 'cp437')
    sentences = file.readlines()

    text = ""
    intext = False
    for sentence in sentences:
        #get rid of the '\n'
        sentence = sentence[0:-1]

        if intext== True and len(sentence) > 0 and sentence[0] != "<":
            #remove newlines?
            text = text+ " " + sentence

        if sentence == "<TEXT>":
            intext = True

        if sentence == "</TEXT>":
            intext = False

    dates = []

    from nltk import ngrams
    n = 30
    tengrams = []
    sents = nltk.sent_tokenize(text)

    #returns a generator of tuples
  #  print(dates)
    return sents

def compareVectors(a, b):
    #convert the wordvector (without stopwords) to number vectors
    #how do we want to create these vectors? bag of words/unigrams or colocations?
    #unigrams created.
    x = []
    y = []
    for element in a:
        x.append(1)
        if element in b:
            y.append(1)
        else:
            y.append(0)

    for element in b:
        if element not in a:
            y.append(1)
            x.append(0)

    sim_score = cosineSim(x,y)
    return sim_score

def cosineSim(x,y):
    import math
    #prereq: |x| = |y|
    numerator = 0
    x_square = 0
    y_square = 0
    for i in range(0, len(x)):
        numerator += x[i] * y[i]
        x_square += x[i]**2
        y_square += y[i]**2
    denominator =  math.sqrt(x_square) * math.sqrt(y_square)

    return numerator / denominator

def main(traintest):
    questions = readQuestions(traintest)
    for number in questions.keys():
        question = questions[number]
        guess = questionProcessing(question)
        if guess == "Who":
            continue
       #     print(str(number) + "main")
        #    print()
         #   whoquestion(question, number, traintest)
        elif guess == "Where":
            continue
            #do where
        elif guess == "How":
            continue
            #do how
        elif guess == "When":
            whenquestion(question, number, traintest)
            #do when function
        elif guess == "What":
            continue
            #do what function
        else:
            print("else")

    return


def readQuestions(traintest):
    import codecs
    documentpath = "hw5_data/qadata/" + traintest + "/questions.txt"
    file = codecs.open(documentpath, 'r', 'cp437')
    sentences = file.readlines()
    questions = {}
    for i in range(0, len(sentences)):
        if sentences[i][0:7] == "Number:":
            #create a dictionary of questions, numbered.
            #key is an int.
            questions[int(sentences[i][8:-1])] = sentences[i+1][:-1]

    return questions




def questionProcessing(question):
    #determine what kind of question it is:
    #remove stopwords

        q_words= nltk.word_tokenize(question)
    filtered_words = q_words

    # filt_q = " ".join(filtered_words)
    # quest = filt_q.lower()

    #stemming?

    if "who" in filtered_words  or "Who" in filtered_words:
        words = [stemmer.stem(word) for word in filtered_words if "who" not in word and "Who" not in word] # Maybe reformat the rest like this if this syntax works
        return("Who")
        # whoquestion(question)
    elif "how" in filtered_words  or "How" in filtered_words:
        words = [word for word in filtered_words if word != "how" and word != "How"]
        return("How")
    elif "where" in filtered_words  or "Where" in filtered_words:
        words = [word for word in filtered_words if word != "where" and word != "Where"]
        return("Where")
    elif "when" in filtered_words  or "When" in filtered_words:
        words = [word for word in filtered_words if word != "when" and word != "When"]
        return("When")
    elif "what" in filtered_words  or "What" in filtered_words:
        words = [word for word in filtered_words if word != "what" and word != "What"]
        return("What")
    else:
        return('Else')
        #Try all cases and return highest confidence


    return;

def whenquestion(question, number,traintest):
    from nltk.corpus import wordnet as wn
    import re

    print(question)
    question = nltk.word_tokenize(question)
    keywords = list(set(question) - stop_words - set(['when', "When"]))
    key_synsets=[]
    key_syn=[]
    keywords = [stemmer.stem(k) for k in keywords]
   # print(keywords)
    key = question[len(question)-2]
    print(key)
    syn = []
    synset = wn.synsets(key, 'v')
    for s in synset:
        syn.append(stemmer.stem(k.split(".")[0]))
    
    documentpath = "hw5_data/topdocs/" + traintest + "/top_docs." + str(number)

    sentences = readDocuments(documentpath)
    tengrams= []
    dates=[]
    for s in sentences:
        tengrams.append(nltk.word_tokenize(s))
    
    ranked_passages = {}
    for gram in tengrams:
        words = set(gram) - stop_words
        words = [stemmer.stem(k) for k in words]
        value = compareVectors(words,keywords)

        """"Should we let the words be the keys and the value of the match be the values?
        all we need to do is make sure that when we look at them to find matches, pick
        the highest values first. """

        if value != 0:
            if value in ranked_passages.keys():
                ranked_passages[value].append(" ".join(words))
            else:
                ranked_passages[value] = []
                ranked_passages[value].append(" ".join(words))

    sorted_passages = sortDictionary(ranked_passages)
    counter = 0

    reduced_pass_2=[]
    ne_q = []
    reduced_pass =[]
    for value in reversed(sorted_passages.keys()):
 #       print(value)
        dates=[]
        ne_list =[]
        if counter > 100:
            break

        for word_list in sorted_passages[value]:
            for word in keywords:
                if word in word_list:
                    phrases= re.findall(r'\w+\s\w+\s\d\d\d\d', word_list) #Match on "word word YYYY"
                    phrases = [p for p in phrases if p is not []]
                    days = re.findall(r'\s[A-Z]\w+\s\d{2}\s', word_list) #Match on "Word DDth"
                   # print(phrases)
                    years= re.findall(r'\d\d\d\d+', word_list) # Match on YYYY"
                    years = [y for y in years if not not y]
                    dates.append(phrases)
                    dates.append(years)
                    dates.append(days)
#                    print(dates)
            if not not dates:
                reduced_pass.append(dates)

        counter+=1

        top_answers = collections.OrderedDict()
        for r in reduced_pass:
            if len(top_answers) == 5: break
            for p in r:
                ans = ""
                if not not p:
                    for unit in p:
                        if unit.isnumeric():
                            ans = unit
                        elif len(unit.split())==3:
                            ans = unit.split()[2]
                        else: ans = unit
                        if ans not in top_answers.keys():
                            top_answers[ans] = value
                        else:
                            top_answers[ans] += value
                if len(top_answers) == 10: break
    print(top_answers.keys())

