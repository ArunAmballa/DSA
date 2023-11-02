import math
class Solution:
    def constructTree(self,post,n):
        if len(post)==0:
            return None
        def helper(post,lo,hi):
            nonlocal index
            if index<0 or post[index]<lo or post[index]>hi:
                return None
            root=Node(post[index])
            index=index-1
            root.right=helper(post,root.val,hi)
            root.left=helper(post,lo,root.val)
            return root
        index=n-1
        return helper(post,-math.inf,math.inf)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
   def __init__(self,val):
       self.val=val
       self.left=None
       self.right=None
class BST:
   size=0
   def inorder(self,tmp,size=0):
       if tmp:
           self.inorder(tmp.left,self.size)
           print(tmp.val,end=" ")
           self.inorder(tmp.right,self.size)
     
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        obj=Solution()
        b=BST()
        pt=obj.constructTree(arr,n)
        b.inorder(pt)
        print()

# } Driver Code Ends