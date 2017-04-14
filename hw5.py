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

    return

def findTopPassages(passages, question):

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
        words = [word for word in filtered_words if "who" not in word and "Who" not in word] # Maybe reformat the rest like this if this syntax works
        # whoquestion(question)
    elif filtered_words.contains("how") or filtered_words.contains("how"):
        words = [word for word in filtered_words if word != "how" and word != "How"]

    elif filtered_words.contains("where") or filtered_words.contains("Where"):
        words = [word for word in filtered_words if word != "where" and word != "Where"]

    elif filtered_words.contains("when") or filtered_words.contains("When"):
        words = [word for word in filtered_words if word != "when" and word != "When"]

    elif filtered_words.contains("what") or filtered_words.contains("What"):
        words = [word for word in filtered_words if word != "what" and word != "What"]

    else:
        #Try all cases and return highest confidence

    return;

def whoquestion(question):
    #my branch
    return
def whatquestion(question):
    return
def wherequestion(question):

    return

=======
        #how-contains how?
        #which-contains which
    return question
