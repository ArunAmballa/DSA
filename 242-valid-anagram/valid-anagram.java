class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        int []arr1=new int[26];
        int []arr2=new int[26];
        for(int i=0;i<s.length();i++){
            char ch1=s.charAt(i);
            char ch2=t.charAt(i);
            int a=(int) ch1;
            int b=(int) ch2;
            arr1[a-97]=arr1[a-97]+1;
            arr2[b-97]=arr2[b-97]+1;
        }
        for(int i=0;i<26;i++){
            if(arr1[i]!=arr2[i]){
                return false;
            }
        }

        return true;
        
    }
}