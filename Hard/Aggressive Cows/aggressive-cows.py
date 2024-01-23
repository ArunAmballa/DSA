#User function Template for python3

class Solution:
    def helper(self,stalls,distance,k):
        cows=1
        pos=0
        for i in range(1,len(stalls)):
            if stalls[i]-stalls[pos]>=distance:
                cows=cows+1
                pos=i
                if cows==k:
                    break
        return cows
                
    def solve(self,n,k,stalls):
        stalls.sort()
        lo=1
        hi=max(stalls)-min(stalls)
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(stalls,mid,k)>=k:
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