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

    def mergeSort(self,nums,lo,hi):
        if lo>=hi:
            return 
        mid=(lo+hi)//2
        self.mergeSort(nums,lo,mid)
        self.mergeSort(nums,mid+1,hi)
        self.merge(nums,lo,mid,hi)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums