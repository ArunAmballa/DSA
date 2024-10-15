class Solution {
    public List<List<Integer>> generate(int numRows) {

        List<List<Integer>> ansList=new ArrayList<>();

        List<Integer> firstRow=new ArrayList<>();

        firstRow.add(1);
        ansList.add(firstRow);
        for(int i=1;i<numRows;i++){
            List<Integer> newList=new ArrayList<>();
            newList.add(1);
            for(int j=1;j<i;j++){
                newList.add(ansList.get(i-1).get(j-1)+ansList.get(i-1).get(j));
            }
            newList.add(1);
            ansList.add(newList);
        }

        return ansList;
        
    }
}