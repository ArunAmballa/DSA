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
            bit =1 if number&(1<<i)!=0 else 0
            if bit not in curr.children:
                curr.children[bit]=TrieNode()
            curr=curr.children[bit]
            
    def search(self,number,n):
        ans=0
        curr=self.root
        for i in range(n,-1,-1):
            bit=1 if number&(1<<i)!=0 else 0
            if bit in curr.children:
                curr=curr.children[bit]
            else:
                ans=ans|(1<<i)
                curr=curr.children[1-bit]
        return ans
class Solution:
    def minxorpair (self, N, arr):
        if N==0:
            return 0
        if N==1:
            return 1
        obj=Trie()
        n=len(bin(max(arr)))-2
        ans=1<<31
        for i in range(0,len(arr)):
            if i==0:
                obj.insert(arr[i],n)
            if i>0:
                ans=min(ans,obj.search(arr[i],n))
                obj.insert(arr[i],n)
        return ans
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        print(ob.minxorpair(N,arr))
        

# } Driver Code Ends