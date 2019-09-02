import re

def getWords(text):
    file = open(text)
    contents = file.read()

    words = re.split(r'\W+', contents, flags=re.IGNORECASE)

    filterWords = list(filter(None, words))

    lowerCaseWords = []

    for x in filterWords:
        lowerCaseWords.append(x.lower())

    lowerCaseWords.sort()

    wordDict = {}

    for word in lowerCaseWords:
        if word not in wordDict:
            patt = r'\b' + word + r'\b'
            wordDict[word.lower()] = len(re.findall(patt, contents, re.IGNORECASE))

    return wordDict


def writeToFile(wordDict):
    file = open("output.txt", "w")
    for word in wordDict:
        file.write("%s %d\n" % (word, wordDict[word]))
    file.close()


def main():
    wd = getWords("declaration.txt")
    print(wd)
    writeToFile(wd)

if __name__ == "__main__":
    main()
