# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def helper_serialize(self,root):
        if root==None:
            return "N"
        leftEncode=self.helper_serialize(root.left)
        rightEncode=self.helper_serialize(root.right)
        currEncode=str(root.val)+","+leftEncode+","+rightEncode
        return currEncode
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.helper_serialize(root)
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'N':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))