# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return "N"
        leftEncode=self.serialize(root.left)
        rightEncode=self.serialize(root.right)
        currEncode=str(root.val)+","+leftEncode+","+rightEncode
        return currEncode
        
    def helper(self,dataList):
        if len(dataList)==0:
            return root
        curr=dataList.pop(0)
        if curr=="N":
            return None
        root=TreeNode(curr)
        root.left=self.helper(dataList)
        root.right=self.helper(dataList)
        return root
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dataList=data.split(",")
        return self.helper(dataList)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))