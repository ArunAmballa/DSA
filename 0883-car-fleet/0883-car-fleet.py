class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=[]
        for i in range(len(position)):
            l.append([position[i],speed[i]])
        l.sort()
        st=[]
        for i in range(len(l)):
            time=(target-l[i][0])/l[i][1]
            while st and time>=st[-1]:
                st.pop()
            st.append(time)
        return len(st)
        