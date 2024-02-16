class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=[intervals[i][0] for i in range(len(intervals))]
        end=[intervals[i][1] for i in range(len(intervals))]
        start.sort()
        end.sort()
        s=0
        e=0
        cnt=0
        res=0
        while s<len(start):
            if start[s]<end[e]:
                cnt=cnt+1
                s=s+1
            else:
                cnt=cnt-1
                e=e+1
            res=max(res,cnt)
        return res


        