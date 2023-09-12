class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            lastEnd=ans[-1][1]
            if start<=lastEnd:
                ans[-1][1]=max(ans[-1][1],end)
            else:
                ans.append([start,end])
        return ans
        