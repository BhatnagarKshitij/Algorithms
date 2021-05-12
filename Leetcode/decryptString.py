'''
Question link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/


Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 


'''


class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = 'abcdefghijklmnopqrstuvwxyz'
        sol = ''
        while s != '':
            if '#' in s[0:3]:
                sol += mapping[int(s[0:2])-1]
                s = s[3:]
            else:
                sol += mapping[int(s[0])-1]
                s = s[1:]

        return sol
