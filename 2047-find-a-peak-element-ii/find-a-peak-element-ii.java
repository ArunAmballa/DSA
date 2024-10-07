class Solution {
    public int findMax(int [][]mat,int col,int rows){
        int maximum=Integer.MIN_VALUE;
        int maxIndex=-1;
        for(int i=0;i<rows;i++){
            if(mat[i][col]>maximum){
                maximum=mat[i][col];
                maxIndex=i;
            }
        }
        return maxIndex;
    }
    public int[] findPeakGrid(int[][] mat) {

        int rows=mat.length;
        int columns=mat[0].length;
        int []ans=new int[2];
        int low=0;
        int high=columns-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            int row=findMax(mat, mid,rows);
            int left= (mid-1>=0) ? mat[row][mid-1] : -1;
            int right= (mid+1<columns) ? mat[row][mid+1] : -1;
            if(mat[row][mid]>left && mat[row][mid]>right){
                ans[0]=row;
                ans[1]=mid;
                return ans;
            }else if (mat[row][mid]>right && mat[row][mid]<left){
                high=mid-1;
            }else{
                low=mid+1;
            }

        }
        return ans;
    }
}