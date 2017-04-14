import nltk
from nltk.corpus import stopwords
def readDocuments(document_path):
    #documentpath =
    import codecs
    file = codecs.open(document_path, 'r', 'cp437')
    sentences = file.readlines()

    text = ""
    for sentence in sentences:
        #get rid of the '\n'
        sentence = sentence[0:-1]
        if intext== True and sentence[0] != "<":
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
        if guess[0] == "Who":
            print(guess)
            print(question)

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
        return("Who", filtered_words)
        # whoquestion(question)
    elif "how" in filtered_words  or "How" in filtered_words:
        words = [word for word in filtered_words if word != "how" and word != "How"]
        return("how", filtered_words)
    elif "where" in filtered_words  or "Where" in filtered_words:
        words = [word for word in filtered_words if word != "where" and word != "Where"]
        return("where", filtered_words)
    elif "when" in filtered_words  or "When" in filtered_words:
        words = [word for word in filtered_words if word != "when" and word != "When"]
        return("when", filtered_words)
    elif "what" in filtered_words  or "What" in filtered_words:
        words = [word for word in filtered_words if word != "what" and word != "What"]
        return("what", filtered_words)
    else:
        return('else', filtered_words)
        #Try all cases and return highest confidence


    return;

def whoquestion(question):
    #have a who question. --- LOOKING FOR A PERSON

    #take out stopwords from question
    stop_words = set(stopwords.words('english'))

    #read associated document-- get 10grams
    #preproccess 10-grams for question

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
    #

    return

        #how-contains how?
        #which-contains which
    return question
