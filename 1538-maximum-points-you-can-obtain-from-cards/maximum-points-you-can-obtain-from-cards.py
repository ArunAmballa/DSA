class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        k=len(cardPoints)-k
        ans=1<<31
        preSum=0
        for i in range(k):
            preSum=preSum+cardPoints[i]
        ans=min(ans,preSum)
        for i in range(k,len(cardPoints)):
            preSum=preSum-cardPoints[i-k]
            preSum=preSum+cardPoints[i]
            ans=min(ans,preSum)
        return sum(cardPoints)-ans
        