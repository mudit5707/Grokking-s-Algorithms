def LCS(X, Y):
    lcs = ""
    dp = [[0]*len(X) for _ in range(len(Y))]
    for i in range(len(Y)):
        for j in range(len(X)):
            if X[j] == Y[i] :
                if i==0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
            else:
                top = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                dp[i][j] = max(top, left)
    return dp[-1][-1]


print(LCS("ABAB","BABA"))