class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        finalArray=[]
        last=[]

        for i in range(1, numRows+1):
            tempArray=[]
            for j in range(1,i+1):
                if j==1 or j==i:
                    tempArray.append(1)
                else:
                    tempArray.append(last[j-2]+last[j-1])
            finalArray.append(tempArray)
            last=tempArray
        return finalArray
