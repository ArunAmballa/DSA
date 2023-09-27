#User function Template for python3

class Solution:
    #Function to merge k sorted arrays.
    def merge(self,arr1,arr2):
        temp=[]
        i=0
        j=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<=arr2[j]:
                temp.append(arr1[i])
                i=i+1
            else:
                temp.append(arr2[j])
                j=j+1
        while i<len(arr1):
            temp.append(arr1[i])
            i=i+1
        while j<len(arr2):
            temp.append(arr2[j])
            j=j+1
        return temp
    def helper(self,arr,last):
        if last==0:
            return arr[0]
        i=0
        j=last
        while i<j:
            arr[i]=self.merge(arr[i],arr[j])
            i=i+1
            j=j-1
        return self.helper(arr,j)
    def mergeKArrays(self, arr, K):
        if not arr:return None
        return self.helper(arr,K-1)
        
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends