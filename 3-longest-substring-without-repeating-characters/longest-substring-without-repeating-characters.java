class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length=s.length();
        int left=0;
        int right=0;
        int []hash=new int[256];
        Arrays.fill(hash,-1);
        int maxi=0;
        while(right<length){
            if(hash[s.charAt(right)]!=-1){
                left=Math.max(left,hash[s.charAt(right)]+1);
            }
            maxi=Math.max(maxi,right-left+1);
            hash[s.charAt(right)]=right;
            right++;
        }
        return maxi;
    }
}