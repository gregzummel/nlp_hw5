import nltk, collections
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

def TopPassages(tengrams, question):
    question_tagged = nltk.pos_tag(question)
    stop_words = set(stopwords.words('english'))
    keywords = list(set(question) - stop_words - set(['who', "Who", "?"]))

    ranked_passages = {}
    for gram in tengrams:
        words = set(gram) - stop_words
        #use fuzzy matching?
        #value = compareVectors(words,keywords)
        from fuzzywuzzy import fuzz
        #value = compareVectors(words,keywords)
        value = fuzz.ratio(gram, question)
        """"Should we let the words be the keys and the value of the match be the values?
        all we need to do is make sure that when we look at them to find matches, pick
        the highest values first. """

        if value != 0:
            if value in ranked_passages.keys():
                ##add gram instead?
                ranked_passages[value].append(gram)
            else:
                #add gram instead?
                ranked_passages[value] = []
                ranked_passages[value].append(gram)

    sorted_passages = sortDictionary(ranked_passages)
    return sorted_passages

def sortDictionary(dictionary):
    return collections.OrderedDict(sorted(dictionary.items()))



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
        elif guess == "What is":
            continue
        elif guess == "Can":
            continue
        elif guess == "Who is":
            continue
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
    question = nltk.word_tokenize(question)
    question_tagged = nltk.pos_tag(question)
    stop_words = set(stopwords.words('english'))
    keywords = list(set(question) - stop_words - set(['who', "Who", "?"]))
    #read associated document-- get 10grams
    documentpath = "hw5_data/topdocs/" + traintest + "/top_docs." + str(number)
    print(number)
    tengrams = readDocuments(documentpath)
    sorted_passages = TopPassages(tengrams, question)
    # ranked_passages = {}
    # for gram in tengrams:
    #     words = set(gram) - stop_words
    #     #use fuzzy matching?
    #     from fuzzywuzzy import fuzz
    #     #value = compareVectors(words,keywords)
    #     value = fuzz.ratio(gram, keywords)
    #     """"Should we let the words be the keys and the value of the match be the values?
    #     all we need to do is make sure that when we look at them to find matches, pick
    #     the highest values first. """
    #
    #     if value != 0:
    #         if value in ranked_passages.keys():
    #             ##add gram instead?
    #             ranked_passages[value].append(gram)
    #         else:
    #             #add gram instead?
    #             ranked_passages[value] = []
    #             ranked_passages[value].append(gram)


    counter = 0
    ne_list = []
    for value in reversed(sorted_passages.keys()):
        print(value)
        if counter > 25:
            break

        for word_list in sorted_passages[value]:
            pos_list = nltk.pos_tag(word_list)
            tree = (nltk.ne_chunk(pos_list, binary=True))
            for element in tree:
                try:
                    ne = element.label()
                    if ne == "NE":
                        leaves = element.leaves()
                        for leaf in leaves:
                            if leaf[0] not in question:
                                ne_list.append(leaf)

                except AttributeError:
                    continue

                counter+=1

    print(word_list)
    print(pos_list)
    print(tree)
    print(ne_list)
    print(counter)



    #Using top x passage, indentify named entities.
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
    """
    http://www.nltk.org/book/ch05.html
    http://www.nltk.org/book/ch07.html
    """

    return

def whatis(question, tengrams):
    #question is an unprocessed string.
    quesiton_tokens = nltk.word_tokenize(question)
    question_tags = nltk.pos_tag(question_tokens)
    #a X is...#
    #

def wherequestion(question):

    return

        #how-contains how?
        #which-contains which
def synonyms(word):
    from PyDictionary import PyDictionary
    dictionary = PyDictionary()
    synonyms = dictionary.synonym('blue', "lxml")
    return synonyms


def readWhoosh(documentpath, number, question):
    traintest = 'train'
    document_path = "hw5_data/topdocs/" + traintest + "/top_docs." + str(number)

    from whoosh.index import create_in
    from whoosh.fields import Schema, STORED, NUMERIC, TEXT
    schema = Schema(title=STORED, rank=STORED, content=TEXT(stored = True))
    import os.path
    if not os.path.exists("index"):
        os.mkdir("index")
    ix = create_in("index", schema)

    from whoosh.index import open_dir
    ix = open_dir("index")

    writer = ix.writer()

    import codecs
    file = codecs.open(document_path, 'r', 'cp437')
    sentences = file.readlines()

    text = ""
    intext = False
    for i in range(0, len(sentences)):
        #get rid of the '\n'
        sentence = sentences[i]
        sentence = sentence[0:-1]

        if intext== True and len(sentence) > 0 and sentence[0] != "<":

            text = text+ " " + sentence

        elif sentence[0:4] == "Qid:":
            scoreix = sentence.index("Score:") + 7
            score = sentence[int(scoreix):]


        elif sentence[0:7] == "<DOCNO>":
            try:
                #get index from the next
                end = sentence.index("</") - 1
                idnumber = sentence[8:end]
            except ValueError:
                idnumber = sentences[i+1][:-1]
                #get the value from the next line.

        elif sentence == "<TEXT>":
            intext = True

        elif sentence == "</TEXT>":
            intext = False

            #write to the document.
            writer.add_document(title=idnumber, rank=score, content=text)


            text = ""

    writer.commit()
    ix=open_dir("index")
    from whoosh.qparser import QueryParser
    from whoosh import qparser, scoring
    #query = QueryParser("content", ix.schema, group=qparser.OrGroup).parse('question ~ 5')
    qp = QueryParser('content', ix.schema, group=qparser.OrGroup)
    q = qp.parse('wrote the "Grinch who Stole Christmas"')
    with ix.searcher() as searcher:
        results = searcher.search(q)
        for result in results:
            print(result["title"])


    # results = searcher.search(query)
    # for result in results:
    #     print(result['title'])
