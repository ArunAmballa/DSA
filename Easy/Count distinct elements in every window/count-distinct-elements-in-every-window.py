
class Solution:
    def countDistinct(self, A, N, K):
        ans=[]
        d={}
        for i in range(K):
            d[A[i]]=d.get(A[i],0)+1
        ans.append(len(d))
        for i in range(K,N):
            d[A[i-k]]=d.get(A[i-k],0)-1
            if d[A[i-k]]==0:
                del d[A[i-k]]
            d[A[i]]=d.get(A[i],0)+1
            ans.append(len(d))
        return ans
            
            


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends