class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length=s.length();
        int left=0;
        int right=0;
        HashMap<Character,Integer> map=new HashMap<>();
        int maxi=0;
        while(right<length){
            map.put(s.charAt(right),map.getOrDefault(s.charAt(right),0)+1);
            while(map.size()<right-left+1){
                map.put(s.charAt(left),map.get(s.charAt(left))-1);
                if(map.get(s.charAt(left))==0){
                    map.remove(s.charAt(left));
                }
                left=left+1;
            }
            if(map.size()==right-left+1){
                maxi=Math.max(maxi,right-left+1);
            }
            right++;
        }
        return maxi;
    }
}