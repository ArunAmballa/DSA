class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def insert(self,s,temp):
        if len(s)==0:
            s.append(temp)
            return s
        if s[-1]<=temp:
            s.append(temp)
            return s
        used=s.pop()
        self.insert(s,temp)
        s.append(used)
    def Sorted(self, s):
        if len(s)==0:
            return s
        temp=s.pop()
        self.Sorted(s)
        return self.insert(s,temp)
        



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends