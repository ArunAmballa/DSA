//{ Driver Code Starts
#include<bits/stdc++.h>
#define MAX 1000
using namespace std;
 
int maxSubsequenceSubstring(string x, string y, int n, int m);
 
// Driver Program
int main()
{
    int t;
    cin>>t;
    while(t--){
        int n,m;
        string x,y;
        cin>>n>>m;
        cin>>x>>y;
        cout<<maxSubsequenceSubstring(x,y,n,m)<<"\n";
    }
    return 0;
}
// } Driver Code Ends


// Return the maximum size of substring of
// X which is substring in Y.
int maxSubsequenceSubstring(string x, string y, int n, int m){
    int dp[MAX][MAX];
 
    // Initialize the dp[][] to 0.
    for (int i = 0; i <= m; i++)
        for (int j = 0; j <= n; j++)
            dp[i][j] = 0;
 
    // Calculating value for each element.
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
 
            // If alphabet of string X and Y are
            // equal make dp[i][j] = 1 + dp[i-1][j-1]
            if (x[j - 1] == y[i - 1])
                dp[i][j] = 1 + dp[i - 1][j - 1];
 
            // Else copy the previous value in the
            // row i.e dp[i-1][j-1]
            else
                dp[i][j] = dp[i][j - 1];
        }
    }
 
    // Finding the maximum length.
    int ans = 0;
    for (int i = 1; i <= m; i++)
        ans = max(ans, dp[i][n]);
 
    return ans;
}