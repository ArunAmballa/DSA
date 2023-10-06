#User function Template for python3
class Solution:

    def partition(self, arr, lo, hi):
        pivot = arr[lo]
        i = lo
        j = hi
        while i < j:
            while arr[i] <= pivot and i < hi:
                i += 1
            while arr[j] > pivot and j > lo:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[lo], arr[j] = arr[j], arr[lo]
        return j

    def QuickSelect(self, arr, lo, hi, k):
        pIndex = self.partition(arr, lo, hi)
        if pIndex == k:
            return
        elif k < pIndex:
            return self.QuickSelect(arr, lo, pIndex - 1, k)
        else:
            return self.QuickSelect(arr, pIndex + 1, hi, k)

    def kLargest(self, arr, n, k):
        self.QuickSelect(arr, 0, n - 1, n - k)
        ans = []
        for i in range(n - 1, n - k - 1, -1):
            ans.append(arr[i])
        ans.sort(reverse=True)  # Reverse the list to get elements in descending order
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends