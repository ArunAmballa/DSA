class Solution {
    public int countPrimes(int n) {
        if(n<2){
            return 0;
        }
        boolean []numbers=new boolean[n+1];
        Arrays.fill(numbers,false);
        numbers[0]=true;
        numbers[1]=true;
        int count=0;
        for(int i=2;i*i<=n;i++){
            if(numbers[i]==false){
                for(int j=i*i;j<=n;j=j+i){
                    numbers[j]=true;
                }
            }
        }
        for(int i=2;i<n;i++){
            if(numbers[i]==false){
                count++;
            }
        }
        return count;
    }
}