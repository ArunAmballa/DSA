class Solution:
    def sumOfSquares(self,n):
        output=0
        while n!=0:
            digit=n%10
            output=output+(digit**2)
            n=n//10
        return output
    def isHappy(self, n: int) -> bool:
        visited=set()
        while n not in visited:
            visited.add(n)
            n=self.sumOfSquares(n) 
            if n==1:
                return True
        return False



        