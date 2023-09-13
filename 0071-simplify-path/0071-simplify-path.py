from queue import LifoQueue
class Solution:
    def reverse(self,st):
        if st.empty():
            return 
        minpath=st.get()
        self.reverse(st)
        self.ans+=minpath

    def simplifyPath(self, path: str) -> str:
        st=LifoQueue()
        i=0
        n=len(path)
        while i<n:
            start=i
            end=i+1
            while end<n and path[end]!="/":
                end=end+1
            i=end
            minPath=path[start:end]
            if minPath=="/" or minPath=="/.":
                continue
            elif minPath=="/.." and not st.empty():
                st.get()
            elif minPath!="/..":
                st.put(minPath)
        if st.empty():
            return "/"
        self.ans=""
        self.reverse(st)
        return self.ans


        