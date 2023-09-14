def countRev (s):
    n=len(s)
    if n%2!=0:
        return -1
    st=[]
    cnt=0
    for i in range(len(s)):
        if not st and s[i]=="}":
            st.append("{")
            cnt=cnt+1
        else:
            if s[i]=="{":
                st.append("{")
            else:
                st.pop()
    cnt=cnt+(len(st)//2)
    return cnt
                


#{ 
 # Driver Code Starts
t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends