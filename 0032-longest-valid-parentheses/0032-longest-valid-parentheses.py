class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[]
        if len(s)==0:
            return 0
        st.append(-1)
        maxLen=0
        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    maxLen=max(maxLen,i-st[-1])
        return maxLen
        