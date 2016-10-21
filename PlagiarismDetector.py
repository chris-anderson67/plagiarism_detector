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

def main():
    if (len(sys.argv) < 4 or len(sys.argv) > 5):
        print "Usage: ..."
        sys.exit(1)

    inputFile = sys.argv[1]
    refFile = sys.argv[2]
    synFile = sys.argv[3]
    tupleSize = 3

    with open(inputFile, 'r') as inputFile: inputs = inputFile.read()
    with open(refFile, 'r') as inputFile: reference = inputFile.read()
    with open(synFile, 'r') as inputFile: synonyms = inputFile.readlines()

    inputs = re.findall(r'[^\s!,.?":;0-9]+', inputs)
    reference = re.findall(r'[^\s!,.?":;0-9]+', reference)

    for i, line in enumerate(synonyms): 
        synonyms[i] = re.findall(r'[^\s!,.?":;0-9]+', line)

    inputTuples = []

    print "Tupling:"
    for i in range(0, (len(inputs) - tupleSize + 1)):
        strings = inputs[i : (i + tupleSize)]
        tup = NTuple(strings, tupleSize)
        inputTuples.append(tup)

    for tup in inputTuples:
        print tup.get()

main()
