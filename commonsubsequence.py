def count_common_sequence(X,Y):
    m, n=len(X),len(Y)
    dp=[[0] * (n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                dp[i][j]=1 + dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
    return dp[m][n]
str1="abc"
str2="ac"
print(count_common_sequence(str1,str2))
