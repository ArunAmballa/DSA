class Solution {
    public boolean compare(int []str1,int []str2){
        for(int i=0;i<26;i++){
            if(str1[i]!=str2[i]){
                return false;
            }
        }
        return true;
    }
    public List<Integer> findAnagrams(String s, String p) {
        if(s.length()<p.length()){
            return new ArrayList<>();
        }
        List<Integer> ans=new ArrayList<>();
        int []pIndex=new int[26];
        int []sIndex=new int[26];
        int k=p.length();
        int length=s.length();
        for(int i=0;i<p.length();i++){
            pIndex[p.charAt(i)-'a']=pIndex[p.charAt(i)-'a']+1;
        }
        for(int i=0;i<k;i++){
            sIndex[s.charAt(i)-'a']=sIndex[s.charAt(i)-'a']+1;
        }
        boolean flag=compare(pIndex,sIndex);
        if(flag==true){
            ans.add(0);
        }
        for(int i=k;i<length;i++){
            sIndex[s.charAt(i-k)-'a']=sIndex[s.charAt(i-k)-'a']-1;
            sIndex[s.charAt(i)-'a']=sIndex[s.charAt(i)-'a']+1;
            boolean comparedValue=compare(pIndex,sIndex);
            if(comparedValue){
                ans.add(i-k+1);
            }
        }
        return ans;
    }
}