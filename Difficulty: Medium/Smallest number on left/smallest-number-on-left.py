# User function Template for Python3

class Solution:
    def leftSmaller(self, n, arr):
        st=[]
        ans=[0]*n
        for i in range(0,n):
            ele=arr[i]
            while st and ele<=st[-1]:
                st.pop()
            if(len(st)!=0):
                ans[i]=st[-1]
            else:
                ans[i]=-1
            st.append(ele)
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends