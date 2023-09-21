#User function Template for python3

class Solution:
    def possible(self,stalls,k,mid):
        cntCows=1
        last=stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i]-last>=mid:
                cntCows=cntCows+1
                last=stalls[i]
            if cntCows>=k:
                return True
        return False
    def solve(self,n,k,stalls):
        stalls.sort()
        lo=1
        hi=max(stalls)-min(stalls)
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            
            if self.possible(stalls,k,mid)==True:
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends