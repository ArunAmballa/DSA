from queue import LifoQueue
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in range(0,len(s)):
            if not st:
                st.append(s[i])
            elif s[i]==st[-1]:
                st.pop()
            else:
                st.append(s[i])
        s=''
        while st:
            s=s+st[-1]
            st.pop()
        return s[::-1]

        