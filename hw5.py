def readDocuments(document_path):
    import codecs
    with codecs.open("corpus.txt", 'r', 'cp437') as file:
        sentences = file.readlines()

    intext = False
    text = ""
    for sentence in sentences:
        if intext:
            text += sentence + " "
        elif sentence == "<TEXT>":
            intext == True
        elif sentence == "</TEXT>":
            intext == False


    # from nltk import ngrams
    # text = ""
    # n = 10
    # tengrams = ngrams(text.split(), n)
    # return tengrams

def compareVectors(a, b):
    #comparing two vectors to one another.

def findTopPassages():
    return #something
    return #somethingelse
    return #evenmore
