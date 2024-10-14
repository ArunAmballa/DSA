class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> hs=new HashSet<>();
        int low=0;
        int high=0;
        int length=s.length();
        int maxi=0;
        while(high<length){
            if(!hs.contains(s.charAt(high))){
                hs.add(s.charAt(high));
                high=high+1;
                maxi=Math.max(maxi,hs.size());
            }else{
                while(hs.contains(s.charAt(high)) && low<high){
                    hs.remove(s.charAt(low));
                    low=low+1;
                }
                hs.add(s.charAt(high));
                high=high+1;
                maxi=Math.max(maxi,hs.size());
            }
        }
        return maxi;
    }
}