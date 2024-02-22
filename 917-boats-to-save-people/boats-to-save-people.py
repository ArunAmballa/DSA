class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt=0
        l=0
        r=len(people)-1
        while l<=r:
            if people[l]+people[r]<=limit:
                l=l+1
            cnt=cnt+1
            r=r-1
        return cnt
        