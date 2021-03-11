class Solution:
    def longestCommonPrefix(self, strs):
        returnString=""
        for index in range(len(min(strs))):
            data=strs[0][index]
            for string in strs:
                if string[index]!=data:
                    return returnString
            returnString+=strs[0][index]
        return returnString
    
solution=Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))