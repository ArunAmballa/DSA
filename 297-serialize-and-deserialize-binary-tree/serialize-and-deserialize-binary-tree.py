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
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dataList=data.split(",")
        def helper(dataList):
            nonlocal index
            if dataList[index]=="N":
                return None
            root=TreeNode(dataList[index])
            index=index+1
            root.left=helper(dataList)
            index=index+1
            root.right=helper(dataList)
            return root
        index=0
        return helper(dataList)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))