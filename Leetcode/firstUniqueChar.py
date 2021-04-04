'''
Question link: https://leetcode.com/problems/first-unique-character-in-a-string

Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
#        if len(s)==0:
#            return -1
#        cnt=Counter(s)
#        for index,ch in enumerate(s):
#            if cnt[ch]==1:
#                return index
#        return -1

        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
