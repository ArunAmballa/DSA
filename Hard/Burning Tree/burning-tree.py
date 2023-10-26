#User function Template for python3
from queue import Queue
class Solution:
    def parentMapping(self,root,target,parentMap):
        targetNode=None
        q=Queue()
        q.put(root)
        while not q.empty():
            curr=q.get()
            if curr.data==target:
                targetNode=curr
            if curr.left!=None:
                q.put(curr.left)
                parentMap[curr.left]=curr
            if curr.right!=None:
                q.put(curr.right)
                parentMap[curr.right]=curr
        return targetNode
        
                
    def burningTime(self,targetNode,parentMap):
        time=0
        m=Queue()
        m.put(targetNode)
        isBurnt={targetNode:1}
        while not m.empty():
            size=m.qsize()
            fireSpreaded=False
            for i in range(0,size):
                curr=m.get()
                if curr.left!=None and isBurnt.get(curr.left,0)!=1:
                    m.put(curr.left)
                    isBurnt[curr.left]=1
                    fireSpreaded=True
                if curr.right!=None and isBurnt.get(curr.right,0)!=1:
                    m.put(curr.right)
                    isBurnt[curr.right]=1
                    fireSpreaded=1
                if parentMap[curr]!=None and isBurnt.get(parentMap[curr],0)!=1:
                    m.put(parentMap[curr])
                    isBurnt[parentMap[curr]]=1
                    fireSpreaded=True
            if fireSpreaded==True:
                time=time+1
        return time
    
    def minTime(self, root,target):
        if root==None:
            return 0
        parentMap={root:None}
        targetNode=self.parentMapping(root,target,parentMap)
        if targetNode==None:
            return 0
        return self.burningTime(targetNode,parentMap)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
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
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends