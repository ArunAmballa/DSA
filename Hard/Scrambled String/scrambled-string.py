#User function Template for python3

class Solution:
    def helper(self,a,b):
        if a==b:
            return True
        if len(a)!=len(b):
            return False
        if a+" "+b in self.map:
            return self.map[a+" "+b]
        flag=False
        n=len(a)
        for k in range(1,n):
            if (self.helper(a[:k],b[n-k:]) and self.helper(a[k:],b[:n-k])):
                flag=True
                break
            elif (self.helper(a[:k],b[:k])and self.helper(a[k:],b[k:])):
                flag=True
                break
        self.map[a+" "+b]=flag
        return self.map[a+" "+b]
    def isScramble(self,S1: str, S2: str):
        self.map={}
        return self.helper(S1,S2)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        S1,S2=input().split()
        if(Solution().isScramble( S1 , S2)):
            print("Yes")
        
        else:
            print("No")


# } Driver Code Ends