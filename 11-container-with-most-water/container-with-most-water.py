class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        ans=-(1<<31)
        while i<j:
            h=min(height[i],height[j])
            w=j-i
            ans=max(ans,h*w)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return ans
            
