class Solution {


    public boolean isPalindrome(String s) {
        
        String s1=s.toLowerCase();
        String newString="";
        for(int i=0;i<s1.length();i++){
            char ch=s1.charAt(i);
            int asciiValue=(int) ch;
            if((asciiValue>=97 && asciiValue<=122) || (asciiValue>=48 && asciiValue<=57)){
                newString=newString.concat(String.valueOf(ch));
            }
        }

        int low=0;
        int high=newString.length()-1;
        while(low<=high){
            if(newString.charAt(low)!=newString.charAt(high)){
                return false;
            }
            low=low+1;
            high=high-1;
        }
        return true;
    }
}