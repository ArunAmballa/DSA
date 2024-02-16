class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            start,end=intervals[i]
            lastEnd=intervals[i-1][1]
            if start<lastEnd:
                return False
        return True
        