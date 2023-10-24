# Your task is to complete this function
# Function should print postorder traversal of Tree
def CBT(preorder,inorder,lo,hi,d,ans):
    if lo>hi:
        return 
    ele=preorder[0]
    preorder.pop(0)
    index=d[ele]
    CBT(preorder,inorder,lo,index-1,d,ans)
    CBT(preorder,inorder,index+1,hi,d,ans)
    ans.append(ele)
    return ans
def printPostOrder(inorder, preorder, n):
    d={}
    for i in range(len(inorder)):
        d[inorder[i]]=i
    ans=CBT(preorder,inorder,0,len(preorder)-1,d,[])
    for i in range(len(ans)):
        print(ans[i],end=" ")



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ino = list(map(int, input().strip().split()))
        pre = list(map(int, input().strip().split()))
        printPostOrder(ino, pre, n)
        print('')
# contributed by: Harshit Sidhwa
# } Driver Code Ends