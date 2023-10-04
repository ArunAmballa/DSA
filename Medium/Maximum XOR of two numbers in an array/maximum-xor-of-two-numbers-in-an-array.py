#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children=[None]*2
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,n,maxLen):
        curr=self.root
        for i in range(maxLen,-1,-1):
            index=1 if n&(1<<i)!=0 else 0
            if curr.children[index]==None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
    def getMax(self,number,maxLen):
        curr=self.root
        maxNumber=0
        for i in range(maxLen,-1,-1):
            bit=1 if number&(1<<i)!=0 else 0
            if curr.children[1-bit]!=None:
                maxNumber=maxNumber|(1<<i)
                curr=curr.children[1-bit]
            else:
                curr=curr.children[bit]
        return maxNumber
class Solution:
    def max_xor(self, arr, n):
        maxLen=len(bin(max(arr)))-2
        obj=Trie()
        for i in range(len(arr)):
            obj.insert(arr[i],maxLen)
        ans=0
        for i in range(len(arr)):
            ans=max(ans,obj.getMax(arr[i],maxLen))
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