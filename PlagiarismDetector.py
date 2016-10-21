import sys
import re

# Not using Built-In Python tuples
# Allows for more flexibility, and our own way of comparing elements


class NTuple:
    def __init__(self, strings, size):
        self.size = size
        self.tuple = strings

    def get(self):
        return self.tuple

    def set(self, strings):
        self.tuple = strings
        self.size = len(strings)
    def equal(self, ntuple):
        pass


def makeTupleList(wordList, tupleSize):
    tuples = []
    for i in range(0, (len(wordList) - tupleSize + 1)):
        words = wordList[i : (i + tupleSize)]
        tup = NTuple(words, tupleSize)
        tuples.append(tup)
    return tuples


def main():
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print "Usage: ..."
        sys.exit(1)

    inputFile = sys.argv[1]
    refFile = sys.argv[2]
    synFile = sys.argv[3]
    if len(sys.argv) == 5: 
        tupleSize = int(sys.argv[4])
    else:
        tupleSize = 3

    with open(inputFile, 'r') as inputFile: inputs = inputFile.read().lower()
    with open(refFile, 'r') as inputFile: reference = inputFile.read().lower()
    with open(synFile, 'r') as inputFile: synonyms = inputFile.readlines()

    inputs = re.findall(r'[^\s!,.?":;0-9]+', inputs)
    reference = re.findall(r'[^\s!,.?":;0-9]+', reference)

    for i in range(len(synonyms)): 
        synonyms[i] = synonyms[i].lower()
        synonyms[i] = re.findall(r'[^\s!,.?":;0-9]+', synonyms[i])

    inputTuples = makeTupleList(tuple(inputs), tupleSize)
    refTuples = makeTupleList(tuple(reference), tupleSize)
    for tupleA in inputTuples:
        for tupleB in refTuples:
            print(tupleA.get(), " VS ", tupleB.get())

    # for tup in inputTuples:
    #     print tup.get()
    # for tup in refTuples:
    #     print tup.get()

main()
