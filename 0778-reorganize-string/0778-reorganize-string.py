import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        h=[]
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
        for i in d:
            heapq.heappush(h,(-(d[i]),i))
        ans=""
        while len(h)>1:
            firstCount,firstChar=heapq.heappop(h)
            secondCount,secondChar=heapq.heappop(h)
            ans=ans+firstChar+secondChar
            firstCount=abs(firstCount)-1
            secondCount=abs(secondCount)-1
            if firstCount!=0:
                heapq.heappush(h,(-firstCount,firstChar))
            if secondCount!=0:
                heapq.heappush(h,(-secondCount,secondChar))
        if not h:return ans
        if h:
            firstCount,firstChar=heapq.heappop(h)
            if abs(firstCount)==1:
                ans=ans+firstChar
                return ans
        return ""
        