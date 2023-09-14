class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        ans=""
        n=len(s)
        if n==1 or n==2:
            return s
        for i in range(n):
            if st and st[-1][0]==s[i]:
                st[-1][1]=st[-1][1]+1
                if st[-1][1]==k:
                    st.pop()
            else:
                st.append([s[i],1])
        while st:
            ans=ans+(st[-1][0]*st[-1][1])
            st.pop()
        return ans[::-1]
            
        