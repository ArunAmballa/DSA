class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        d={}
        for i in range(len(hand)):
            d[hand[i]]=d.get(hand[i],0)+1
        h=list(d.keys())
        heapq.heapify(h)
        while h:
            smallest=h[0]
            for num in range(smallest,smallest+groupSize):
                if num not in d:
                    return False
                d[num]=d[num]-1
                if d[num]==0:
                    del d[num]
                    if num!=h[0]:
                        return False
                    heapq.heappop(h)
        return True


        