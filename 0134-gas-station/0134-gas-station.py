class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        balance=0
        deficit=0
        start=0
        for i in range(len(gas)):
            balance=balance+(gas[i]-cost[i])
            if balance<0:
                deficit=deficit+balance
                start=i+1
                balance=0
        return start if balance>=abs(deficit) else -1
        