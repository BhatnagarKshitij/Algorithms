from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        one=Counter(s)
        two=Counter(t)
        print("ONE: ",one)
        print("TWO: ",two)
        return True if one==two else False

solution=Solution()
print(solution.isAnagram("anagram","nagaram"))