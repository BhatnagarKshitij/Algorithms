class Solution:
    def isPalindrome(self, s: str):
        s=''.join(filter(str.isalnum,s)).lower()
        divide=int(len(s)/2)
        return True if s[:divide:]==s[::-1][:divide] else False
        

solution=Solution()
print(solution.isPalindrome("aab"))