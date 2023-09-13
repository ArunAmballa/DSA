# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from queue import LifoQueue
class Solution:
    def findCelebrity(self, n: int) -> int:
        st=LifoQueue()
        for i in range(n):
            st.put(i)
        while st.qsize()!=1:
            a=st.get()
            b=st.get()
            if knows(a,b)==True:
                st.put(b)
            else:
                st.put(a)
        celebrity=st.get()
        print(celebrity)
        for i in range(0,n):
            if knows(celebrity,i)==True and i!=celebrity:
                return -1
        for i in range(0,n):
            if knows(i,celebrity)==False and i!=celebrity:
                return -1
        return celebrity



        