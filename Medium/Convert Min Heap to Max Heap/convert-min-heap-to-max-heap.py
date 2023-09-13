#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def heapify(self,arr,i,n):
        index=i
        left=2*index+1
        right=2*index+2
        largest=index
        if left<n and arr[largest]<arr[left]:
            largest=left
        if right<n and arr[largest]<arr[right]:
            largest=right
        if index!=largest:
            arr[index],arr[largest]=arr[largest],arr[index]
            self.heapify(arr,largest,n)
        if index==largest:
            return arr
        return arr
        
    def buildheap(self,arr,n):
        n=(n//2)-1
        for i in range(n,-1,-1):
            self.heapify(arr,i,len(arr))
        return arr
    def convertMinToMaxHeap(self, N, arr):
        return self.buildheap(arr,N)


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.convertMinToMaxHeap(N, arr)
        for val in arr:
            print(val, end = ' ')
        print()
# } Driver Code Ends