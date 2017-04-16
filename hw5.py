def readDocuments(document_path):
    #documentpath =
    import codecs
    file = codecs.open(document_path, 'r', 'cp437')
    sentences = file.readlines()

    text = ""
    for sentence in sentences:
        #get rid of the '\n'
        sentence = sentence[0:-1]
        if intext= True and sentence[0] != "<":
            #remove newlines?
            text = text+ " " + sentence
        if sentence == "<TEXT>":
            intext == True
        if sentence == "</TEXT>":
            intext == False

    from nltk import ngrams
    n = 10
    tengrams = ngrams(text.split(), n)
    return tengrams

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


def findTopPassages(passages, question):
    scores = [] #Should find a better way to store and retrieve top 10. Maybe priority queue\
?
    for p in passages:
        p_vect = []
        q_vect = []
        for word in question:
            if p.contains(word):
                p_vect.add(1)
            else:
                p_vect.add(0)
            q_vect.add(1)
        left = len(p)-len(q_vect)
        for i in range(0, left):
            p_vect.add(1)
            q_vect.add(0)
        sim = compareVectors(q_vect, p_vect)
        scores.add(sim)

    return scores

    return

def readQuestions(traintest):
    import codecs
    documentpath = "hw5_data/qadata/" + traintest + "/questions.txt"
    file = codecs.open(documentpath, 'r', 'cp437')
    sentences = file.readlines()



def questionProcessing(question):
    #determine what kind of question it is:
    #remove stopwords

    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    q_words= question.split()
    filtered_words = [word for word in q_words if word not in stop_words]
    # filt_q = " ".join(filtered_words)
    # quest = filt_q.lower()

    #stemming
    from nltk.stem.porter import *
    stemmer = PorterStemmer()

    if filtered_words.contains("who") or filtered_words.contains("Who"):
        words = [stemmer.stem(word) for word in filtered_words if "who" not in word and "Who" not in word] # Maybe reformat the rest like this if this syntax works
        # whoquestion(question)
    elif filtered_words.contains("how") or filtered_words.contains("how"):
        words = [stemmer.stem(word) for word in filtered_words if "how" not in word and "How" not in word]

    elif filtered_words.contains("where") or filtered_words.contains("Where"):
        words = [stemmer.stem(word) for word in filtered_words if "where" not in word and "Where" not in word]

    elif filtered_words.contains("when") or filtered_words.contains("When"):
        words = [stemmer.stem(word) for word in filtered_words if "when" not in word and "When" not in word]

    elif filtered_words.contains("what") or filtered_words.contains("What"):
        words = [stemmer.stem(word) for word in filtered_words if "what" not in word and "What" not in word]

    else:
        #Try all cases and return highest confidence

    return;

def whoquestion(question):
    return
def whatquestion(question):
    return
def wherequestion(question):
    
    return

=======
        #how-contains how?
        #which-contains which
    return question
