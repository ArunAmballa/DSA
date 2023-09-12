def findMissingRepeatingNumbers(a: [int]) -> [int]:
    S=0
    S2=0
    n=len(a)
    SN=(n*(n+1))//2
    S2N=(n*(n+1)*(2*n+1))//6
    for i in range(len(a)):
        S=S+a[i]
        S2=S2+(a[i]*a[i])
    val1=S-SN
    val2=S2-S2N
    val2=val2//val1
    x=(val1+val2)//2
    y=x-val1
    return [x,y]


   
