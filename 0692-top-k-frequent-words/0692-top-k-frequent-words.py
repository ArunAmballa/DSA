import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        d={}
        for i in range(len(words)):
            d[words[i]]=d.get(words[i],0)+1
        ind=0
        h=[]
        for i in d:
            heapq.heappush(h,(-d[i],i))
        ans=[]
        while len(ans)!=k:
            count,word=heapq.heappop(h)
            ans.append(word)
        return ans

