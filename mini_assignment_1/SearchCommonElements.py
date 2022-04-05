from collections import Counter
from mini_assignment_1.StringClass import StringClass


class SearchCommonElements(StringClass):
    def commonele(self):
        d = dict(Counter(list(self.string)))
        ans = []
        for j in d:
            if d[j] >= 2:
                ans.append(j)
        return ans
