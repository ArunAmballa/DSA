#User function Template for python3

def isSubset( a1, a2, n, m):
    d={}
    for i in range(len(a1)):
        d[a1[i]]=d.get(a1[i],0)+1
    for i in range(len(a2)):
        if a2[i] not in d:
            return "No"
        if a2[i] in d:
            d[a2[i]]=d[a2[i]]-1
            if d[a2[i]]==0:
                del d[a2[i]]
        
    return "Yes"
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends