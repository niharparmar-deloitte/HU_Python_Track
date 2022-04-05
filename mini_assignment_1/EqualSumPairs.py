from mini_assignment_1.StringClass import StringClass
from mini_assignment_1.PairsPossible import PairsPossible
from mini_assignment_1.SearchCommonElements import SearchCommonElements






userinput=input()
objstringclass=StringClass(userinput)
print("Length of string is: ",objstringclass.printlength())
print("String converted to list: ",objstringclass.converttolist())
objpairspossible=PairsPossible(userinput)
print("All possible pairs are: ")
objpairspossible.pair()
objsearchcommonelements=SearchCommonElements(userinput)
print()
print("Common elements are: ",objsearchcommonelements.commonele())