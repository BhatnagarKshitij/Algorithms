class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        negitive=[]
        positive=[]
        zeros=[]

        for num in nums:
            if num>0:
                positive.append(num)
            elif num<0:
                negitive.append(num)
            else:
                zeros.append(num)

        negitiveSet=set(negitive)
        positiveSet=set(positive)

        if zeros:
            for number in positiveSet:
                if -number in negitiveSet:
                    result.add((-number,0,number))

        if len(zeros)>=3:
            result.add((0,0,0))

        if not negitiveSet or not positiveSet:
            return result

        for i in range(len(negitive)):
            for j in range(i+1,len(negitive)):
                target=-(negitive[i]+negitive[j])
                if target in positiveSet:
                    result.add(tuple(sorted([negitive[i],negitive[j],target])))

        for i in range(len(positive)):
            for j in range(i+1,len(positive)):
                target=-(positive[i]+positive[j])
                if target in negitiveSet:
                    result.add(tuple(sorted([positive[i],positive[j],target])))

        return result
