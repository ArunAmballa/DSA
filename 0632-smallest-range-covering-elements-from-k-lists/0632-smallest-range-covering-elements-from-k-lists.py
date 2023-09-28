import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h=[]
        k=len(nums)
        maxi=-(1<<31)
        mini=1<<31
        for i in range(len(nums)):
            heapq.heappush(h,(nums[i][0],i,0))
            maxi=max(maxi,nums[i][0])
            mini=min(mini,nums[i][0])
        ansStart=mini
        ansEnd=maxi
        ansRange=ansEnd-ansStart

        while len(h)>=k:
            mini,row,col=heapq.heappop(h)
            currStart=mini
            currEnd=maxi
            currRange=currEnd-currStart
            ansRange=ansEnd-ansStart
            if currRange<ansRange:
                ansStart=currStart
                ansEnd=currEnd
            if col+1<len(nums[row]):
                heapq.heappush(h,(nums[row][col+1],row,col+1))
                maxi=max(maxi,nums[row][col+1])
        return [ansStart,ansEnd]


        