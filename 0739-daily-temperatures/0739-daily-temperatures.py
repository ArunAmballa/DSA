class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        ans=[]
        for i in range(len(temperatures)-1,-1,-1):
            
            while st and temperatures[i]>=temperatures[st[-1]]:
                st.pop()
            if not st:
                ans.insert(0,0)
            else:
                ans.insert(0,st[-1]-i)
            st.append(i)
        return ans
        