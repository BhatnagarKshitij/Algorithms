class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower=True
        upper=True
        isFirstCapital=True if word[0].isupper() else False
        if not isFirstCapital:
            upper=False


        for i in range(1,len(word)):
            if lower or upper:
                if word[i].islower():
                    upper=False
                elif word[i].isupper():
                    lower=False
            else:
                return False

        if not upper and not lower:
            return False
        else:
            return True     
        
        
#        if word.isupper():
#            return True
#        elif word.islower():
#            return True 
#        elif word[0].isupper() and word[1:].islower():
#            return True
#
#        return False
