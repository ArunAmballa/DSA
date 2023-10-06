class Solution:
    def partition(self,nums,lo,hi,d):
        pivot=nums[lo]
        i=lo
        j=hi
        while i<j:
            while d[nums[i]]<=d[pivot] and i<hi:
                i=i+1
            while d[nums[j]]>d[pivot] and j>lo:
                j=j-1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        nums[lo],nums[j]=nums[j],nums[lo]
        return j
    def QuickSelect(self,nums,lo,hi,k,d):
        pIndex=self.partition(nums,lo,hi,d)
        if pIndex==k:
            return nums[k:]
        elif k<pIndex:
            return self.QuickSelect(nums,lo,pIndex-1,k,d)
        else:
            return self.QuickSelect(nums,pIndex+1,hi,k,d)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        nums=list(d.keys())
        return self.QuickSelect(nums,0,len(nums)-1,len(nums)-k,d)
        