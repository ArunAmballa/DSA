class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for i in range(len(operations)):
            if operations[i]=="+" and len(score)>=2:
                valSum=score[-1]+score[-2]
                score.append(valSum)
            elif operations[i]=="C" and len(score)>0:
                score.pop()
            elif operations[i]=="D" and len(score)>0:
                valSum=score[-1]
                score.append(2*valSum)
            else:
                score.append(int(operations[i]))
        return sum(score)
        