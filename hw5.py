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

def findTopPassages():
    return #something
    return #somethingelse
    return #evenmore
    #take question
    
