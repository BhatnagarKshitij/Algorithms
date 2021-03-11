'''
QUESTOIN LINK: https://leetcode.com/problems/count-and-say/

To determine how you "say" a digit string, split it into the minimal number of groups
so that each group is a contiguous section all of the same character. Then for each group,
say the number of characters, then say the character.
To convert the saying into a digit string, replace the counts with a number and concatenate
every saying.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        n=str(n)
        if n=="1":
            return"1"
        elif n=="2":
            return "11"
        else:
            outputString="11"
        for i in range(3,int(n)+1):
            count=0
            prev=outputString[0]
            temp=""
            for j in range(len(outputString)):
                if prev==outputString[j]:
                    count+=1
                else:
                    temp+=str(count)+str(outputString[j-1])
                    count=1
                    prev=outputString[j]
            else:
                temp+=str(count)+str(outputString[j])
            outputString=temp
        return outputString

        
solution=Solution()
print(solution.countAndSay(4))