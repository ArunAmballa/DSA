class Solution():

    def checkRedundancy(self, s):
        st=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="+" or s[i]=="-" or s[i]=='*' or s[i]=="/":
                st.append(s[i])
            elif s[i]==")":
                operator=False
                while st and st[-1]!="(":
                    if st[-1]=='+' or st[-1]=="-" or st[-1]=="*" or st[-1]=="/":
                        operator=True
                        st.pop()
                st.pop()
                if operator==False:
                    return 1
            else:
                pass
        return 0


#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().checkRedundancy(s))

# } Driver Code Ends