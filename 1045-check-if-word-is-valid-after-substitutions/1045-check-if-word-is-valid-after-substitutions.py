class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        n=len(s)
        if n%3!=0:
            return False
        for i in range(n):
            if s[i]=="a" or s[i]=="b":
                st.append(s[i])
            elif s[i]=="c":
                if st and st[-1]=="b":
                    st.pop()
                    if st and st[-1]=="a":
                        st.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(st)==0 else False
        
        