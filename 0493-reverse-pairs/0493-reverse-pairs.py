class Solution:
    def merge(self,nums,lo,mid,hi):
        i=lo
        j=mid+1
        temp=[]
        while i<=mid and j<=hi:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i=i+1
            else:
                temp.append(nums[j])
                j=j+1
            
        while i<=mid:
            temp.append(nums[i])
            i=i+1
        while j<=hi:
            temp.append(nums[j])
            j=j+1
        for i in range(lo,hi+1):
            nums[i]=temp[i-lo]

    def countPairs(self,nums,lo,mid,hi):
        cnt=0
        j=mid+1
        for i in range(lo,mid+1):

            while j<=hi and nums[i]>2*nums[j]:
                j=j+1
            cnt=cnt+(j-(mid+1))
        self.ans=self.ans+cnt
    def mergeSort(self,nums,lo,hi):
        if lo>=hi:
            return 
        mid=(lo+hi)//2
        self.mergeSort(nums,lo,mid)
        self.mergeSort(nums,mid+1,hi)
        self.countPairs(nums,lo,mid,hi)
        self.merge(nums,lo,mid,hi)
    def reversePairs(self, nums: List[int]) -> int:
        self.ans=0
        self.mergeSort(nums,0,len(nums)-1)
        return self.ans

        