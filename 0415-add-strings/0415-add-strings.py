class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=""
        carry=0
        n1=len(num1)
        n2=len(num2)
        p1=n1-1
        p2=n2-1
        while p1>=0 or p2>=0 or carry==1:
            number1=ord(num1[p1])-ord('0') if p1>=0 else 0
            number2=ord(num2[p2])-ord('0') if p2>=0 else 0
            valSum=number1+number2+carry
            ans=ans+str(valSum%10)
            carry=valSum//10
            p1=p1-1
            p2=p2-1
        return ans[::-1]

            
            
            
        