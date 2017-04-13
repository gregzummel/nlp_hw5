def readDocuments(document_path):
    import codecs
    file = codecs.open(document_path, 'r', 'cp437'):
    sentences = file.readlines()

    text = ""
    for sentence in sentences:
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


def questionProcessing(question):
    #determine what kind of question it is:
    #remove stopwords

        #who
            #look for person.

        #what
            #more difficult. Noun Phrase
        #when
            #look for time
        #where
            #look for location
        #how
        #which
    return question

def whoquestion(question):

    return
def whatquestion(question):
    return
def wherequestion(question):
    return
