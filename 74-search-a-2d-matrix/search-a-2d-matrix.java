class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows=matrix.length;
        int columns=matrix[0].length;
        int low=0;
        int high=(rows*columns)-1;
        while (low<=high){
            int mid=low+(high-low)/2;
            int col=mid%columns;
            int row=(int) Math.floor((double) mid/columns);
            if(matrix[row][col]==target){
                return true;
            }else if(target>matrix[row][col]){
                low=mid+1;
            }else{
                high=mid-1;
            }
        }

        return false;
        
    }
}