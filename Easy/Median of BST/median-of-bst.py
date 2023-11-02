#User function Template for python3
def morrisTraversal(root):
    if root==None:
        return 0
    curr=root
    cnt=0
    while curr!=None:
        if curr.left==None:
            cnt=cnt+1
            curr=curr.right
        else:
            pred=curr.left
            while pred.right!=None and pred.right!=curr:
                pred=pred.right
            if pred.right==None:
                pred.right=curr
                curr=curr.left
            else:
                pred.right=None
                cnt=cnt+1
                curr=curr.right
    return cnt
def Median(root,n):
    if root==None:
        return 0
    curr=root
    cnt=0
    oddMedian=(n+1)//2
    evenMedian1=(n//2)
    evenMedian2=(n//2)+1
    oddVal=-1
    even1=-1
    even2=-1
    while curr!=None:
        if curr.left==None:
            cnt=cnt+1
            if cnt==oddMedian:
                oddVal=curr.data
            if cnt==evenMedian1:
                even1=curr.data
            if cnt==evenMedian2:
                even2=curr.data
            curr=curr.right
        else:
            pred=curr.left
            while pred.right!=None and pred.right!=curr:
                pred=pred.right
            if pred.right==None:
                pred.right=curr
                curr=curr.left
            else:
                pred.right=None
                cnt=cnt+1
                if cnt==oddMedian:
                    oddVal=curr.data
                if cnt==evenMedian1:
                    even1=curr.data
                if cnt==evenMedian2:
                    even2=curr.data
                curr=curr.right
    if n%2==0:
        median=(even1+even2)/2
        return int(median) if median.is_integer() else median
    return oddVal
            
def findMedian(root):
    n=morrisTraversal(root)
    return Median(root,n)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(findMedian(root))

# } Driver Code Ends