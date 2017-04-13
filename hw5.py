def readDocuments(document):

    #for every line:
        #text == false
        #if line == <TEXT>
            #text == true
        #if text and != beginning character != "<":
            #add to doc
        #elif text == "</TEXT"
            #text == false

    from nltk import ngrams
    text = ""
    n = 10
    tengrams = ngrams(text.split(), n)
    return tengrams

def compareVectors(a, b):
    #comparing two vectors to one another.

def findTopPassages():
    return #something
    return #somethingelse
    return #evenmore
