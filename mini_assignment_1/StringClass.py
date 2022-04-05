class StringClass:

    # init method or constructor
    def __init__(self, str):
        self.str = str

    # Sample Method
    def LengthOfString(self):
        counter = 0
        for i in self.str:
            counter += 1
        return counter

    def ConvertStringToCharacters(self):
        return list(self.str)