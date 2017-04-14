import nltk
from nltk.corpus import stopwords
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


    from nltk import ngrams
    n = 10
    tengrams = ngrams(nltk.word_tokenize(text), n)
    #returns a generator of tuples
    return tengrams

def compareVectors(a, b):

    return

def findTopPassages(passages, question):
    #compareVectors for all vectors.
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



def main(traintest):
    questions = readQuestions(traintest)
    for number in questions.keys():
        question = questions[number]
        guess = questionProcessing(question)
        if guess == "Who":
            print(str(number) + "main")
            print()
            whoquestion(question, number, traintest)
        elif guess == "Where":
            continue
            #do where
        elif guess == "How":
            continue
            #do how
        elif guess == "When":
            continue
            #do when function
        elif guess == "What":
            continue
            #do what function
        else:
            print("else")

    return




def questionProcessing(question):
    #determine what kind of question it is:
    #remove stopwords
    """'what', 'which' etc are included in stopwords, we can either remove it from the stopwords or not do stopwords yet"""
    #from nltk.corpus import stopwords
    #stop_words = set(stopwords.words('english'))
    import nltk
    q_words= nltk.word_tokenize(question)
    filtered_words = q_words
    #[word for word in q_words if word not in stop_words]

    # filt_q = " ".join(filtered_words)
    # quest = filt_q.lower()

    #stemming?

    if "who" in filtered_words  or "Who" in filtered_words:
        words = [word for word in filtered_words if "who" not in word and "Who" not in word] # Maybe reformat the rest like this if this syntax works
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

def whoquestion(question, number, traintest):
    #have a who question. --- LOOKING FOR A PERSON
    #take out stopwords from question
    stop_words = set(stopwords.words('english'))
    keywords = list(set(question) - stop_words - set(['who', "Who"]))
    #read associated document-- get 10grams
    documentpath = "hw5_data/topdocs/" + traintest + "/top_docs." + str(number)
    print(number)
    tengrams = readDocuments(documentpath)
    for gram in tengrams:
        #for each ngram, compute a similarity.
        #compareVectors(list(gram), question)

        #when do we want to do named entity recognition?
        #

        #give pos tags



    """Two types of who questions"""
    #how to distiguish between them.
    """Who is ...."""
    sent = "who is XXX's friend and biographer."



    """Who did ..."""


    #take passage 10-grams, and find the one with the best match.


    return
def whatquestion(question):

    return
def wherequestion(question):

    return

        #how-contains how?
        #which-contains which
    return question
