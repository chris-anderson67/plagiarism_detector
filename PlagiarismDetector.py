import sys
import re
from SimilarityCalculator import SimilarityCalculator
# Not using Built-In Python tuples
# Allows for more flexibility, and our own way of comparing elements






def main():
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print "Usage: ..."
        sys.exit(1)
    if len(sys.argv) == 5: 
        tupleSize = int(sys.argv[4])
    else:
        tupleSize = 3

    # Open files, parse input into strings, synonyms to list of lists
    try: 
        with open(sys.argv[1], 'r') as inputFile: inputs = inputFile.read().lower()
        with open(sys.argv[2], 'r') as inputFile: reference = inputFile.read().lower()
        with open(sys.argv[3], 'r') as inputFile: synonyms = inputFile.readlines()
        inputs = re.findall(r'[^\s!,.?":;0-9]+', inputs)
        reference = re.findall(r'[^\s!,.?":;0-9]+', reference)
        for i in range(len(synonyms)): 
            synonyms[i] = synonyms[i].lower()
            synonyms[i] = re.findall(r'[^\s!,.?":;0-9]+', synonyms[i])
    except (IOError, OSError):
        print "Invalid file name or path"
        sys.exit(1)

    # Do the work
    simCalc = SimilarityCalculator();
    percentage = simCalc.simPercentage(inputs, reference, tupleSize, synonyms)
    print "FINALPERCENT: ",  percentage

main()
