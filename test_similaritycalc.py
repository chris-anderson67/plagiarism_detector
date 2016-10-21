from similaritycalc import SimilarityCalculator

def test_null_arguments():
    simcalc = SimilarityCalculator()
    simcalc.simPercentage(None, None, None, None)

def test_empty_strings_lists():
    simcalc = SimilarityCalculator()
    simcalc.simPercentage("", "", 0, [])

def test_single_words():
    simcalc = SimilarityCalculator()
    simcalc.simPercentage("hello world", "world hello", 2, [["hello", "world"]])

def larger_tuple_size_than_input():
    simcalc = SimilarityCalculator()
    simcalc.simPercentage("go for a jog", "go for a run", 5, [["run", "jog"]])

def run_tests():
        test_null_arguments()
        test_empty_strings_lists()
        test_single_words()
        larger_tuple_size_than_input()

run_tests()
