class Solution:
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        d={}
        for i in range(len(hand)):
            d[hand[i]]=d.get(hand[i],0)+1
        minHeap=list(d.keys())
        heapq.heapify(minHeap)
        while minHeap:
            smallest=minHeap[0]
            for i in range(smallest,smallest+groupSize):
                if i not in d:
                    return False
                d[i]=d[i]-1
                if d[i]==0:
                    if i!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
        