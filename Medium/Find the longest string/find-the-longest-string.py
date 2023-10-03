#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.endOfWord=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.endOfWord=True
        
    def complete(self,word):
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index]!=None:
                curr=curr.children[index]
                if curr.endOfWord==False:
                    return False
            else:
                return False
        return True
            
class Solution():
    def longestString(self, arr, n):
        obj=Trie()
        for i in range(len(arr)):
            obj.insert(arr[i])
        ans=""
        for i in range(len(arr)):
            if obj.complete(arr[i]):
                if len(arr[i])>len(ans):
                    ans=arr[i]
                elif (len(arr[i])==len(ans)):
                    ans= min(arr[i],ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends