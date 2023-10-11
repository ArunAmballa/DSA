import math
def check(n):
    a=1 
    b=1 
    c=1 
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a=i 
            break
    n=n//a 
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0 and i!=a:
            b=i 
            break
    c=n//b 
    if (a!=b and b!=c and a!=1 and b!=1 and c!=1):
        print("Yes")
        print(a,b,c,sep=" ")
    else:
        print("No")
t=int(input())
for i in range(t):
    n=int(input())
    check(n)