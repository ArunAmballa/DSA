class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt=0
        preSum=0
        for i in range(k):
            preSum=preSum+arr[i]
        if (preSum/k)>=threshold:
            cnt=cnt+1
        for i in range(k,len(arr)):
            preSum=preSum-arr[i-k]
            preSum=preSum+arr[i]
            if (preSum/k)>=threshold:
                cnt=cnt+1
        return cnt
        