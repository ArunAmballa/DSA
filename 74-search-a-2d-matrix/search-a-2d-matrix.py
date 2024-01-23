class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        lo=0
        hi=(n*m)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            row=mid//m
            col=mid%m
            if matrix[row][col]==target:
                return True
            elif target>matrix[row][col]:
                lo=mid+1
            else:
                hi=mid-1
        return False
        