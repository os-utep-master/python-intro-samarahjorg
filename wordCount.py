import re
import sys
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
            wordDict.update({word.lower() : len(re.findall(patt, contents, re.IGNORECASE))})

    return wordDict


def writeToFile(wordDict):
    file = open("output.txt", "w")
    for key,value in sorted(wordDict.items()):
        file.write("%s %d\n" % (key, value))
    file.close()



def main():
    text = sys.argv[1]
    print(text)
    wd = getWords(text)
    writeToFile(wd)

if __name__ == "__main__":
    main()

