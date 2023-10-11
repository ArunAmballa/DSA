def check(rotations):
    n=len(rotations)
    for i in range(0,(1<<n)):
        ans=0
        for j in range(0,n):
            if i&(1<<j)!=0:
                ans=ans+rotations[j]
            else:
                ans=ans-rotations[j]
        if ans==0:
            print("Yes")
    print("NO")
rotations=int(input())
l=[]
for i in range(rotations):
    n=int(input())
    l.append(n)
check(l)