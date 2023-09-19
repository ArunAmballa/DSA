def lowerBound(arr: [int], n: int, x: int) -> int:
    ans=n
    lo=0
    hi=n-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]>=x:
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    return ans
    
