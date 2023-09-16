class Solution:
    def nextSmallest(self,heights):
        l=[]
        st=[]
        for i in range(len(heights)-1,-1,-1):
            while st and heights[i]<=heights[st[-1]]:
                st.pop()
            if not st:
                l.insert(0,-1)
            else:
                l.insert(0,st[-1])
            st.append(i)
        return l
    def prevSmallest(self,heights):
        l=[]
        st=[]
        for i in range(len(heights)):
            while st and heights[i]<=heights[st[-1]]:
                st.pop()
            if not st:
                l.append(-1)
            else:
                l.append(st[-1])
            st.append(i)
        return l
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev=self.prevSmallest(heights)
        next=self.nextSmallest(heights)
        maxi=-(1<<31)
        for i in range(len(heights)):
            previ=prev[i]
            if next[i]==-1:
                nexti=len(heights)
            else:
                nexti=next[i]
            width=nexti-previ-1
            maxi=max(maxi,heights[i]*width)
        return maxi
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=int(matrix[i][j])
        maxarea=self.largestRectangleArea(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==1:
                    matrix[i][j]=matrix[i][j]+matrix[i-1][j]
                else:
                    matrix[i][j]=0
            maxarea=max(maxarea,self.largestRectangleArea(matrix[i]))
        return maxarea

        
        