# Module to calculate the similarity of two strings using
# a by-word n-tuple comparison algorithm.

from NTuple import NTuple

class SimilarityCalculator:
    def __init__(self):
        pass

    def makeTupleList(self, wordList, tupleSize):
        tuples = []
        for i in range(0, (len(wordList) - tupleSize + 1)):
            words = wordList[i : (i + tupleSize)]
            tup = NTuple(words, tupleSize)
            tuples.append(tup)
        return tuples

    # inputs: string, series of words to compare
    # reference: string, series of words to compare
    # synonyms: list of lists where each sublist contains a set of
    #           synonymous words
    def simPercentage(self, inputs, reference, tupleSize, synonyms):
        inputTuples = self.makeTupleList(tuple(inputs), tupleSize)
        refTuples = self.makeTupleList(tuple(reference), tupleSize)
        synonymMap = {}
        for line in synonyms:
            for word in line:
                synonymMap[word] = line

        count = 0
        for tupleA in inputTuples:
            for tupleB in refTuples:
                # print(tupleA.get(), " VS ", tupleB.get())
                if tupleA.equals(tupleB, synonymMap):
                    print "EQUAL"
                    count += 1
        print "INPUT LENGTH: ", len(inputs)
        print "TOTAL #TUPLES: ", len(inputTuples)
        print "COUNT MATCHES: ", count
        print "PERCENTAGE: ", count / float(len(inputTuples)), "%"
        return count / float(len(inputTuples))
