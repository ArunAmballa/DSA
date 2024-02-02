class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)==0 or len(fruits)==1:
            return len(fruits)
        d={}
        s=0
        e=0
        ans=-(1<<31)
        while e<len(fruits):
            d[fruits[e]]=d.get(fruits[e],0)+1
            if len(d) <= 2:
                ans=max(ans,e-s+1)
                e=e+1
            else:
                while len(d)>2 and s<=e:
                    d[fruits[s]]=d.get(fruits[s],0)-1
                    if d[fruits[s]]==0:
                        del d[fruits[s]]
                    s=s+1
                if len(d)==2:
                    ans=max(ans,e-s+1)
                e=e+1
        return ans
        