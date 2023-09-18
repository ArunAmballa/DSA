class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        maxi=0
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            start=nums[i]
            if start-1 not in d:
                cnt=1
                check=start+1
                while check in d:
                    cnt=cnt+1
                    check=check+1
                maxi=max(maxi,cnt)
        return maxi
        
        