"""
Author: Samarah Jorgensen
Last Edited: 9/1/19
A program that counts the number of occurences of each word in a file. 

"""
import re
import sys
def getWords(text):
    file = open(text)
    contents = file.read()

    words = re.split(r'\W+', contents, flags=re.IGNORECASE)
    
    #Takes off empty string
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
    wd = getWords(text)
    writeToFile(wd)

if __name__ == "__main__":
    main()

