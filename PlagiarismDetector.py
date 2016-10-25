# PlagiarismDetector:
#    Python command line app for testing the extent of similarites between 
#    two files. 
#
#    Chris Anderson - 10-20-16
#

import sys
import re
from similaritycalc import SimilarityCalculator

def main():
    # Naive CLA handling - for larger applications we should switch to get-opt
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print "Usage: plagiarismdetector.py inputtextfile  referencetextfile synonymstextfile [Tuple Size]"
        sys.exit(1)
    if len(sys.argv) == 5: 
        tupleSize = int(sys.argv[4])
    else:
        tupleSize = 3

    # Opens files, parses input into strings, synonyms to list of lists of synonyms
    try: 
        with open(sys.argv[1], 'r') as inputFile: inputs = inputFile.read()
        with open(sys.argv[2], 'r') as inputFile: reference = inputFile.read()
        with open(sys.argv[3], 'r') as inputFile: synonyms = inputFile.readlines()
        for i in range(len(synonyms)): 
            synonyms[i] = synonyms[i].lower()
            synonyms[i] = re.findall(r'[^\s!,.?":;0-9]+', synonyms[i])
    except (IOError, OSError):
        print "Invalid file name or path"
        sys.exit(1)

    # Does the work
    try:
        simCalc = SimilarityCalculator();
        percentage = simCalc.simPercentage(inputs, reference, tupleSize, synonyms)
        print str(int(percentage)) + "%"
    except TypeError:
        print "Provided some None or empty argument to simPercentage"
        sys.exit(1)
    except ValueError:
        print "Provided 0 or negative value for tupleSize, or empty string to" 
        print "SimilarityCalculator. Check for empty Files, and make sure tupleSize exceeds"
        print "the number of words in both input file and reference file."
        sys.exit(1)

if __name__ == '__main__':
    main()
