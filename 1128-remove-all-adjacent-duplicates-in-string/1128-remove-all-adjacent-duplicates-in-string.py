class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if st and st[-1]==s[i]:
                st.pop()
            else:
                st.append(s[i])
        ans=""
        while st:
            ans=ans+ st.pop()
        return ans[::-1]

        