class Solution {
    public int maxVowels(String s, int k) {
        if(s.length()<k){
            return 0;
        }
        HashSet<Character> hs=new HashSet<>();
        hs.add('a');
        hs.add('e');
        hs.add('i');
        hs.add('o');
        hs.add('u');
        int maxi=0;
        int countVowels=0;
        for(int i=0;i<k;i++){
            if(hs.contains(s.charAt(i))){
                countVowels++;
            }
        }
        maxi=Math.max(maxi,countVowels);
        for(int i=k;i<s.length();i++){
            if(hs.contains(s.charAt(i-k))){
                countVowels--;
            }
            if(hs.contains(s.charAt(i))){
                countVowels++;
            }
            maxi=Math.max(maxi,countVowels);
        }
        return maxi;
    }
}