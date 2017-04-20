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

def inQuotes(question):
    words_in_quotes = []
    grab = False
    for word in question:
        if word == '``':
            grab = True
            continue
        elif grab:
            if word == "''":
                grab = False

            else:
                words_in_quotes.append(word)
    return words_in_quotes


def TopPassages(tengrams, question):
    question_tagged = nltk.pos_tag(question)
    stop_words = set(stopwords.words('english'))

    inquotes = inQuotes(question)

    keywords = list(set(question) - stop_words - set(['who', "Who", "?"]))
    for word in keywords:
        print(synonyms(word))

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
            #whoquestion(question, number, traintest)
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
            print(str(number) + "what is")
            whatisquestion(question)
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
    if "what is" in filtered_words  or "What is" in filtered_words:
        words = [word for word in filtered_words if "what is" not in word and "What is" not in word] # Maybe reformat the rest like this if this syntax works
        return("What is")
    elif "who" in filtered_words  or "Who" in filtered_words:
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
    # question = nltk.word_tokenize(question)
    # question_tagged = nltk.pos_tag(question)
    # stop_words = set(stopwords.words('english'))
    # keywords = list(set(question) - stop_words - set(['who', "Who", "?"]))
    # #read associated document-- get 10grams
    # documentpath = "hw5_data/topdocs/" + traintest + "/top_docs." + str(number)
    # print(number)
    # tengrams = readDocuments(documentpath)
    # sorted_passages = TopPassages(tengrams, question)
    #
    # counter = 0
    # ne_list = []
    # for value in reversed(sorted_passages.keys()):
    #     print(value)
    #     if counter > 25:
    #         break
    #
    #     for word_list in sorted_passages[value]:
    #         pos_list = nltk.pos_tag(word_list)
    #         tree = (nltk.ne_chunk(pos_list, binary=True))
    #         for element in tree:
    #             try:
    #                 ne = element.label()
    #                 if ne == "NE":
    #                     leaves = element.leaves()
    #                     for leaf in leaves:
    #                         if leaf[0] not in question:
    #                             ne_list.append(leaf)
    #
    #             except AttributeError:
    #                 continue
    #
    #             counter+=1
    #
    # print(word_list)
    # print(pos_list)
    # print(tree)
    # print(ne_list)
    # print(counter)

    #process question.
    named_entity = "PERSON"
    stop_words = set(stopwords.words('english')) + set(["Who", "who"])
    ix = readWhoosh(traintest, number)



    question =

    return guesses

def whatisquestion(question):
    #looking for descriptors
    #also who is
    question = nltk.word_tokenize(question)
    question_tagged = nltk.pos_tag(question)
    stop_words = set(stopwords.words('english'))
    keywords = list(set(question) - stop_words - set(['what', "What", "?"]))
    syns = []
    for word in keywords:
        syns.append(synonyms(word))


    #read associated document-- get 10grams
    documentpath = "hw5_data/topdocs/" + traintest + "/top_docs." + str(number)
    print(number)
    tengrams = readDocuments(documentpath)
    sorted_passages = TopPassages(tengrams, question)
    counter = 0
    for entry in sorted_passages.keys():
        print(sorted_passages[entry])
    ##pattern matching.
    return answer
def whatquestion(question):
    #looking for noun

    return answer
    #
def wherequestion(question):

    return

        #how-contains how?
        #which-contains which
def synonyms(word):
    from PyDictionary import PyDictionary
    dictionary = PyDictionary()
    synonyms = dictionary.synonym(word, "lxml")
    return synonyms[word]



def readWhoosh(traintest, number):

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
            print(idnumber)
            print(score)
            print(text)
            writer.add_document(title=idnumber, rank=score, content=text)
            text = ""

    writer.commit()
    ix=open_dir("index")
    return ix

def joining(traintest, number, query, ne, neBinary):
    ix = readWhoosh(traintest, number)
    z = queryunigramWhoosh(query, ix)
    y = (querybigramWhoosh(query, ix))
    x = (queryneWhoosh(query, ix, "ORGANIZATION", neBinary))

def queryunigramWhoosh(query, open_dir):
    ix = open_dir
    from whoosh.qparser import QueryParser
    from whoosh import qparser, scoring
    #query = QueryParser("content", ix.schema, group=qparser.OrGroup).parse('question ~ 5')
    qp = QueryParser('content', ix.schema, group=qparser.OrGroup)
    qp2 = QueryParser('content', ix.schema)
    q = qp.parse(query)
    q2 = qp2.parse(query)
    print("SEARCHING unigrams")

    with ix.searcher() as searcher:
        from whoosh import highlight
        results = searcher.search(q)
        results.formatter = highlight.UppercaseFormatter()
        results.fragmenter = highlight.SentenceFragmenter()
        results2 = searcher.search(q2)
        results2.formatter = highlight.UppercaseFormatter()
        results2.fragmenter = highlight.SentenceFragmenter()
        enum_tokens = {}
        stop_words = set(stopwords.words('english'))
        stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
        for result in results:
            print(result['title'])
            tokens = nltk.word_tokenize(result.highlights("content"))
            tag_tokens = nltk.pos_tag(tokens)
            for token in tag_tokens:
                if token in enum_tokens.keys() and token not in stop_words:
                    enum_tokens[token] += 1 * float(result['rank'])
                else:
                    enum_tokens[token] = 1 * float(result['rank'])
        print(enum_tokens)
        enum_tokens2 = {}
        for result in results2:
            print(result['title'])
            print(result['title'])
            tokens = nltk.word_tokenize(result.highlights("content"))
            for token in tokens:
                if token in enum_tokens2.keys() and token not in stop_words:
                    enum_tokens2[token] += 1
                else:
                    enum_tokens2[token] = 1
        return enum_tokens, enum_tokens2

def querybigramWhoosh(query, open_dir):
    ix = open_dir
    from whoosh.qparser import QueryParser
    from whoosh import qparser, scoring
    qp = QueryParser('content', ix.schema, group=qparser.OrGroup)
    qp2 = QueryParser('content', ix.schema)
    q = qp.parse(query)
    q2 = qp2.parse(query)
    print("SEARCHING bigrams")
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    with ix.searcher() as searcher:
        from whoosh import highlight
        results = searcher.search(q)
        results.formatter = highlight.UppercaseFormatter()
        results.fragmenter = highlight.SentenceFragmenter()
        results2 = searcher.search(q2)
        results2.formatter = highlight.UppercaseFormatter()
        results2.fragmenter = highlight.SentenceFragmenter()
        enum_tokens = {}
        for result in results:
            print(result['title'])
            unprocessedtokens = nltk.word_tokenize(result.highlights("content"))
            tokens = [token for token in unprocessedtokens if token not in stop_words]
            for bigram in nltk.ngrams(tokens, 2):
                if bigram in enum_tokens.keys():
                    enum_tokens[bigram] += 1 * float(result['rank'])
                else:
                    enum_tokens[bigram] = 1 * float(result['rank'])
        print(enum_tokens)
        enum_tokens2 = {}
        for result in results2:
            print(result['title'])
            print(result['title'])
            unprocessedtokens = nltk.word_tokenize(result.highlights("content"))
            tokens = [token for token in unprocessedtokens if token not in stop_words]
            for token in tokens:
                if token in enum_tokens2.keys() and token not in set(stopwords.words('english')):
                    enum_tokens2[token] += 1
                else:
                    enum_tokens2[token] = 1
        return enum_tokens, enum_tokens2

def queryneWhoosh(query, open_dir, ne, neBinary):
    ix = open_dir
    from whoosh.qparser import QueryParser
    from whoosh import qparser, scoring
    qp = QueryParser('content', ix.schema, group=qparser.OrGroup)
    qp2 = QueryParser('content', ix.schema)
    q = qp.parse(query)
    q2 = qp2.parse(query)
    print("SEARCHING ne")

    with ix.searcher() as searcher:
        from whoosh import highlight
        results = searcher.search(q)
        results.formatter = highlight.UppercaseFormatter()
        results.fragmenter = highlight.SentenceFragmenter()
        results2 = searcher.search(q2)
        results2.formatter = highlight.UppercaseFormatter()
        results2.fragmenter = highlight.SentenceFragmenter()
        enum_tokens = {}
        for result in results:
            print(result['title'])
            tokens = nltk.word_tokenize(result.highlights("content"))
            tagged_tokens = nltk.pos_tag(tokens)
            if neBinary == True:
                ne_tree = (nltk.ne_chunk(tagged_tokens, binary=True))
            else:
                ne_tree = (nltk.ne_chunk(tagged_tokens))
            for subtree in ne_tree.subtrees(filter =lambda t: t.label() == ne):
                netuple = tuple([a for (a,b) in subtree.leaves()])
                if netuple in enum_tokens.keys():
                    enum_tokens[netuple] += 1 * float(result['rank'])
                else:
                    enum_tokens[netuple] = 1 * float(result['rank'])
        enum_tokens2 = {}
        for result in results2:
            print(result['title'])
            tokens = nltk.word_tokenize(result.highlights("content"))
            tagged_tokens = nltk.pos_tag(tokens)
            if neBinary == True:
                ne_tree = (nltk.ne_chunk(tagged_tokens, binary=True))
            else:
                ne_tree = (nltk.ne_chunk(tagged_tokens))
            for subtree in ne_tree.subtrees(filter =lambda t: t.label() == ne):
                netuple = tuple([a for (a,b) in subtree.leaves()])
                if netuple in enum_tokens2.keys():
                    enum_tokens2[netuple] += 1 * float(result['rank'])
                else:
                    enum_tokens2[netuple] = 1 * float(result['rank'])
        return enum_tokens, enum_tokens2
