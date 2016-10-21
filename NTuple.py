# N-Tuple:
# Wrapper for built in tuples
# Does not extend the original tuple, although that
# functionality could be added at a later date
#
# Chris Anderson 10-20-16
#
# Client can instantiate this class with either a tuple or a list
# and can theoretically use any equivilance map such that the map
# maps every possible alternative equivilance to a list of
# values equivilant to that key.
#

class NTuple:
    def __init__(self, items_list, size):
        self.size = size
        self.tup = items_list

    # ntuple: Another NTuple object
    # equivMap: A dictionary object which defines
    #           possible equivilancies (e.g. all synonymous words
    #           mapped to their synonymous matching sets partners)
    def equals(self, ntuple, equivMap):
        listB = ntuple.tup
        listA = self.tup
        if self.size != len(listB): return False
        for i in range(0, self.size):
            if listA[i] != listB[i]:
                if listA[i] not in equivMap:
                    return False
                if listB[i] not in equivMap[listA[i]]:
                    return False
        return True
