from queue import LifoQueue
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=LifoQueue()
        ans=''
        for i in range(len(s)):
            if st.empty():
                st.put(s[i])
            else:
                if st.queue[-1]==s[i]:
                    st.get()
                else:
                    st.put(s[i])
        while not st.empty():
            ans=ans+st.get()
        return ans[::-1]

        