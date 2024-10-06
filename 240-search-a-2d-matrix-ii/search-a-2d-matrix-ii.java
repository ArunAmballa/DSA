class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int rows=matrix.length;
        int columns=matrix[0].length;
        int i=0;
        int j=columns-1;
        while(i>=0 && i<rows && j>=0 && j<columns){
            if(matrix[i][j]==target){
                return true;
            }else if (target>matrix[i][j]){
                i=i+1;
            }else{
                j=j-1;
            }
        }

        return false;
        
    }
}