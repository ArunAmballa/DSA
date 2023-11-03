# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root==None:
            return "N"
        leftEncode=self.serialize(root.left)
        rightEncode=self.serialize(root.right)
        currEncode=str(root.val)+","+leftEncode+","+rightEncode
        return currEncode

    def helper(self,dataList): 
            curr=dataList.pop(0)
            if curr=="N":
                return None
            root=TreeNode(curr)
            root.left=self.helper(dataList)
            root.right=self.helper(dataList)
            return root
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        dataList=data.split(",")
        return self.helper(dataList)

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans