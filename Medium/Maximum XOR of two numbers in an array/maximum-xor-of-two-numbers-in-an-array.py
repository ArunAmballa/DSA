#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children={}
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,number,n):
        curr=self.root
        for i in range(n,-1,-1):
            bit=1 if number&(1<<i)!=0 else 0
            if bit not in curr.children:
                curr.children[bit]=TrieNode()
            curr=curr.children[bit]
    def search(self,number,n):
        curr=self.root
        ans=0
        for i in range(n,-1,-1):
            bit=1 if number&(1<<i)!=0 else 0
            if 1-bit in curr.children:
                ans=ans|(1<<i)
                curr=curr.children[1-bit]
            else:
                curr=curr.children[bit]
        return ans
class Solution:
    def max_xor(self, arr, n):
        obj=Trie()
        n=len(bin(max(arr)))-2
        ans=0
        for i in range(0,len(arr)):
            obj.insert(arr[i],n)
            if i>0:
                ans=max(ans,obj.search(arr[i],n))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = list(map(int,input().split()))
		ob = Solution();
		print(ob.max_xor(arr,n))
	
# } Driver Code Ends