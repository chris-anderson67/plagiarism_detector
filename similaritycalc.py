#
# SimilarityCalc: 
# Module for finding the extent to which two pieces of text are similar
#
# Chris Anderson, 10-20-2016
# 
# Alternatively, this module could be implemented without a class, or in the
# future be abstracted to support taking a comparison function instead of just
# synonyms. In addition to taking a comparison function, this module could be
# further abstracted to allow for N-Tuple based comparison of any data type
#

from ntuple import NTuple
import re
class SimilarityCalculator:
    def __init__(self):
        pass

    # inputs: string, series of words to compare
    # reference: string, series of words to compare
    # synonyms: list of lists where each sublist contains a set of
    #           synonymous words
    # rasies: TypeError for None arguments, ValueError for 0, negative, or empty arguments, or if
    #         tupleSize is greater than the number of words in either input or reference.
    def simPercentage(self, inputs, reference, tupleSize, synonyms):
        if inputs is None or reference is None or tupleSize is None or synonyms is None:
            raise(TypeError)
        if (tupleSize < 1 or inputs == "" or inputs == [] or reference == [] 
                or reference == "" or synonyms == [] or synonyms == ""):
            raise(ValueError)

        # Makes data structures
        inputs = inputs.lower()
        reference = reference.lower()
        inputs = re.findall(r'[^\s!,.?":;0-9]+', inputs)
        reference = re.findall(r'[^\s!,.?":;0-9]+', reference)
        inputTuples = self.makeTupleList(tuple(inputs), tupleSize)
        refTuples = self.makeTupleList(tuple(reference), tupleSize)
        if len(inputTuples) < 1 or len(refTuples) < 1: raise(ValueError)
        synonymMap = {}
        for line in synonyms:
            for word in line:
                synonymMap[word] = line

        # Finds percentage
        count = 0
        for tupleA in inputTuples:
            for tupleB in refTuples:
                if tupleA.equals(tupleB, synonymMap):
                    count += 1
        return (count / float(len(inputTuples))) * 100


    # Returns: List of N-Tuples given a
    # list of strings wordList and tupleSize
    def makeTupleList(self, wordList, tupleSize):
        tuples = []
        for i in range(0, (len(wordList) - tupleSize + 1)):
            words = wordList[i : (i + tupleSize)]
            tup = NTuple(words, tupleSize)
            tuples.append(tup)
        return tuples
