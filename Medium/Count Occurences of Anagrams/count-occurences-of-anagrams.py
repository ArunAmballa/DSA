#User function Template for python3
class Solution:
	def search(self,pat, txt):
	    d={}
	    for i in range(len(pat)):
	        d[pat[i]]=d.get(pat[i],0)+1
	    m={}
	    cnt=0
	    k=len(pat)
	    for i in range(k):
	        m[txt[i]]=m.get(txt[i],0)+1
	    if m==d:
	        cnt=cnt+1
	    for i in range(k,len(txt)):
	        m[txt[i-k]]=m.get(txt[i-k],0)-1
	        if m[txt[i-k]]==0:
	            del m[txt[i-k]]
	        m[txt[i]]=m.get(txt[i],0)+1
	        if m==d:
	            cnt=cnt+1
	    return cnt
	        
	    
	   
	   


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends