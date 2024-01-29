#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, K):
    ans=[]
    q=deque()
    for i in range(K):
        if A[i]<0:
            q.append(i)
    if not q:
        ans.append(0)
    else:
        ans.append(A[q[0]])
    for i in range(K,N):
        if q and i-q[0]>=K:
            q.popleft()
        if A[i]<0:
            q.append(i)
        if not q:
            ans.append(0)
        else:
            ans.append(A[q[0]])
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends