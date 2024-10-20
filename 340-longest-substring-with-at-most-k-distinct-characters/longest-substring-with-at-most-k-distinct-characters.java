class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int left=0;
        int right=0;
        int length=s.length();
        HashMap<Character,Integer> map=new HashMap<>();
        int maxi=0;
        while(right<length){
            map.put(s.charAt(right),map.getOrDefault(s.charAt(right),0)+1);
            while(map.size()>k){
               map.put(s.charAt(left),map.get(s.charAt(left))-1);
               if(map.get(s.charAt(left))==0){
                    map.remove(s.charAt(left));
               } 
               left=left+1;
            }
            if(map.size()<=k){
                maxi=Math.max(maxi,right-left+1);
            }
            right++;
        }
        return maxi;
    }
}