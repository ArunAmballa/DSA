class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if(len(intervals))>0:
            lastEnd=intervals[0][1]
        for i in range(1,len(intervals)):
            start,end=intervals[i]
            if start<lastEnd:
                return False
            else:
                lastEnd=end
        return True
        