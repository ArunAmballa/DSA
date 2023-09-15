#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b,n,m):
        temp=[]
        i=0
        j=0
      
        while i<n and j<m:
            if a[i]<=b[j]:
                if len(temp)>0 and temp[-1]!=a[i]:
                    temp.append(a[i])
                elif len(temp)==0:
                    temp.append(a[i])
                i=i+1
            else:
                if len(temp)>0 and temp[-1]!=b[j]:
                    temp.append(b[j])
                elif len(temp)==0:
                    temp.append(b[j])
                j=j+1
        while i<n:
            if temp[-1]!=a[i]:
                temp.append(a[i])
            i=i+1
        while j<m:
            if temp[-1]!=b[j]:
                temp.append(b[j])
            j=j+1
        return temp
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends