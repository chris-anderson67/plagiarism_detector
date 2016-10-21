# Plagiarism Detector
#### Python Command Line app for checking similarity between two text files.

## Usage:
  - python PlagiarismDetector.py inputtextfile  referencetextfile synonymstextfile [Tuple Size]
  - Python 2.7 Recommended

## Modules:
  - similaritycalc
    - Reusable module that gives the percentage similarity of two strings
    - This is intended only for string comparisons using a list of synonym sets,
      and would have to be extended and further abstracted to support client implemented
      comparison functions, or similarity percentages of types other than strings.
      Rather, this module is intended to be used in any other application where 
      similarity of strings is required.
  - ntuple
    - Model of N-Tuple object used for this comparison algorithm
    - Type independed, and could be reused with a different equivilancy map
      or different data type to produce different results in different situations.

## Design Assumptions:
  - Input is assumed to be case insensitive, and punctuation and linebreaks are ignored.
  - Providing mpty or nonexistant files is a checked runtime error.
  - Providing a tuple size greater than the number of words in either the input or reference
    file is also a C.R.E.
  - Command line arguments are assumed to only be entered in the order specified.
