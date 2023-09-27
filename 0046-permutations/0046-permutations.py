class Solution:
    def generate(self,nums,l,d,ans):
        if len(l)==len(nums):
            ans.append(l.copy())
            return 
        for i in range(0,len(nums)):
            if d[i]==-1:
                d[i]=1
                l=l+[nums[i]]
                self.generate(nums,l,d,ans)
                d[i]=-1
                l.pop()
        return ans


    def permute(self, nums: List[int]) -> List[List[int]]:
        d={i:-1 for i in range(0,len(nums))}
        return self.generate(nums,[],d,[])
        