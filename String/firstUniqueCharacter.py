from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
#         if len(s)==0:
#             return -1
#         
#         unique=dict()
#         for i in range(len(s)):
#             unique[s[i]]=unique.get(s[i],0)+1
#         index=-1
#         for item in unique:
#             index+=1
#             if unique.get(item)==1:
#                 return s.index(item)
#         else:
#             return -1
#



#
#         if len(s)==0:
#             return -1
#         data=[0]*26
#         for char in s:
#             data[ord(char)-97]+=1
#         for i in range(len(s)):
#             if data[ord(s[i])-97]==1:
#                 return i
#         return -1


        cnt=Counter(s)
        index=0
        print("CNT: ", cnt)
        for ch in s:
            if cnt.get(ch)==1:
                return index
            index+=1
        else:
            return -1
            
        return cnt
solution=Solution()
print(solution.firstUniqChar("leetcode"))