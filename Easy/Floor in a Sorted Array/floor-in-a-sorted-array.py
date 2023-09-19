class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,n,x):
        ans=-1
        lo=0
        hi=n-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if arr[mid]<=x:
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends