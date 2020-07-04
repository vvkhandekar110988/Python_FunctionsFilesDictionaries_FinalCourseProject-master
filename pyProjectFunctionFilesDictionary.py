import functools

projectTwitterDataFile = open("files/project_twitter_data.csv", "r")
resultingDataFile = open("files/resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

positive_words_a = []
positive_words_a = list(filter(lambda x: x.startswith('a'), positive_words))

# print(positive_words_a)


def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()

    count = 0
    listStrSentences_sort = sorted(listStrSentences)
    positive_words.sort()

    for item in listStrSentences_sort:
        item.lower()
        for i in range(97, 123):
            if chr(i) == item[0]:
                for p in list(filter(lambda x: x.startswith(chr(i)), positive_words)):
                    if item == p:
                        count += 1

    return count


negative_words = []
with open("files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()

    count = 0
    listStrSentences_sort = sorted(listStrSentences)
    negative_words.sort()


    count = 0
    for item in listStrSentences_sort:
        item.lower()
        for i in range(97, 123):
            if chr(i) == item[0]:
                for p in list(filter(lambda x: x.startswith(chr(i)), negative_words)):
                    if item == p:
                        count += 1

    return count


def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord


def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF = projectTwitterDataFile.readlines()
    headerDontUsed = linesPTDF.pop(0)
    for linesTD in linesPTDF[1:]:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write(
            "{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]),
                                        (get_pos(listTD[0]) - get_neg(listTD[0]))))
        resultingDataFile.write("\n")


writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()
