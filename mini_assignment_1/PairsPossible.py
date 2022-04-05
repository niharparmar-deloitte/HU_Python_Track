from itertools import combinations

from mini_assignment_1.StringClass import StringClass


class PairsPossible(StringClass):
    def __init__(self, str1):
        self.str1 = str1

    def AllPossiblePairs(self):
        res = list(combinations(self.str1, 2))

        print("All possible pairs : " + str(res))

Obj1 = PairsPossible('12314532')
print(Obj1.AllPossiblePairs())