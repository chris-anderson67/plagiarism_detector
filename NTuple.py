# Wrapper for built in tuples
# Does not extend the original tuple, although that
# functionality could be added at a later date

class NTuple:
    def __init__(self, items_list, size):
        self.size = size
        self.tup = items_list

    # ntuple: Another NTuple object
    # equivMap: A dictionary object which defines
    #           possible equivilancies (e.g. all synonymous words)
    def equals(self, ntuple, equivMap):
        listB = ntuple.tup
        listA = self.tup
        if self.size != len(listB): return False
        # print self.tup, " VS ", listB
        for i in range(0, self.size):
            print i
            print listA[i], listB[i]
            if listA[i] != listB[i]:
                if listA[i] not in equivMap:
                    return False
                if listB[i] not in equivMap[listA[i]]:
                    return False
        return True
