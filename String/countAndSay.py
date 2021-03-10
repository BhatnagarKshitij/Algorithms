class Solution:
    def countAndSay(self, n: int) -> str:
        od=dict()
        for data in n:
            od[data]=od.get(data,0)+1
        data="" 
        for number,count in od.items():
            data+=str(count)+str(number)
        return data

                
solution=Solution()
print(solution.countAndSay("3322251"))