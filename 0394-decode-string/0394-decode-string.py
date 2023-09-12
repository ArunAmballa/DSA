
class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch=="]":
                tempString=""
                while st and st[-1]!="[":
                    tempString+=st[-1]
                    st.pop()
                st.pop()
                numberString=""
                while st and st[-1].isdigit():
                    numberString=numberString+st[-1]
                    st.pop()
                number=int(numberString[::-1])
                ansString=tempString*number
                st.append(ansString)
            else:
                st.append(ch)
        ans=""
        while st:
            ans=ans+st[-1]
            st.pop()
        return ans[::-1]
        
        