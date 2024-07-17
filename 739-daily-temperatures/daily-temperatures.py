class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            ele=temperatures[i]
            while st and ele>=st[-1][0]:
                st.pop()
            if(len(st)!=0):
                ans[i]=st[-1][-1]-i
            else:
                ans[i]=0
            st.append([ele,i])
        return ans
        