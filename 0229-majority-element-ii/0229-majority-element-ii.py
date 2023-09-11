class Solution:
    def check(self,ele,nums,minCount):
        cnt=0
        for i in range(0,len(nums)):
            if nums[i]==ele:
                cnt=cnt+1
        return True if cnt>minCount else False
    def majorityElement(self, nums: List[int]) -> List[int]:
        minCount=math.floor(len(nums)/3)
        el1=-(1<<31)
        cnt1=0
        el2=-(1<<31)
        cnt2=0
        l=[]
        for i in range(0,len(nums)):
            if cnt1==0 and nums[i]!=el2:
                cnt1=cnt1+1
                el1=nums[i]
            elif cnt2==0 and nums[i]!=el1:
                cnt2=cnt2+1
                el2=nums[i]
            elif nums[i]==el1:
                cnt1=cnt1+1
            elif nums[i]==el2:
                cnt2=cnt2+1
            else:
                cnt1=cnt1-1
                cnt2=cnt2-1
        elans1=self.check(el1,nums,minCount)
        if elans1 is True:
            l.append(el1)
        elans2=self.check(el2,nums,minCount)
        if elans2 is True:
            l.append(el2)
        return l
        

        