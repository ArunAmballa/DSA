#User function Template for python3
import math
class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        if root==None:
            return 0
        def helper(node):
            nonlocal max_size
            if node is None:
                return [True, 0, math.inf, -math.inf]

            left_info = helper(node.left)
            right_info = helper(node.right)

            if (
                left_info[0] and right_info[0] and
                left_info[3] < node.data < right_info[2]
            ):
                # The current subtree is a valid BST
                size = left_info[1] + right_info[1] + 1
                max_size = max(max_size, size)
                return [True, size, min(left_info[2], node.data), max(right_info[3], node.data)]
            else:
                return [False, max(left_info[1], right_info[1]), None, None]
        max_size = 0
        helper(root)
        return max_size


#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(1000000)

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root



if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()

        root = buildTree(s)
        ob = Solution()
        print(ob.largestBst(root))

# } Driver Code Ends