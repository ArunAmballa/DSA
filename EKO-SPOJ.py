def possible(l,mid):
    cnt=0
    for i in range(len(l)):
        k=l[i]-mid
        if k>=0:
            cnt=cnt+k 
    return cnt
def check(l,m):
    lo=0
    hi=max(l)
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if possible(l,mid)>=m:
            ans=mid
            lo=mid+1 
        else:
            hi=mid-1
    return ans
n,m=[int(x) for x in input().split( )]
l=[int(x) for x in input().split( )]
print(check(l,m))