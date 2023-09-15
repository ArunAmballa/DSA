def longestSubarrayWithSumK(a: [int], k: int) -> int:
    valSum=a[0]
    maxLen=0
    i=0
    j=0
    while j<len(a):
        while valSum>k and i<=j:
            valSum=valSum-a[i]
            i=i+1
        if valSum==k:
            maxLen=max(maxLen,j-i+1)
        j=j+1
        if j<len(a):
            valSum=valSum+a[j]
    return maxLen
