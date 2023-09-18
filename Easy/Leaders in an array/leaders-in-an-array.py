class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, arr, N):
        l=[]
        maxi=arr[-1]
        l.append(arr[-1])
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>=maxi:
                l.append(arr[i])
                maxi=arr[i]
            else:
                pass
        return l[::-1]
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends