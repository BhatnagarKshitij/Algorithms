class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def sortIntervals(intervall):
            return intervall[0]
        intervals.sort(key=sortIntervals)
        newIntervals=[intervals[0]]
        pointer=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<=newIntervals[pointer][1] :
                newIntervals[pointer][0]=min(intervals[i][0],newIntervals[pointer][0])
                newIntervals[pointer][1]=max(intervals[i][1],newIntervals[pointer][1])

            else:
                newIntervals.append(intervals[i])
                pointer+=1
        return newIntervals
