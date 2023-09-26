#User function Template for python3
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        h=[]
        for i in range(0,k):
            heapq.heappush(h,-arr[i])
        for i in range(k,len(arr)):
            if arr[i]<abs(h[0]):
                heapq.heapreplace(h,-arr[i])
        return abs(h[0])
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends