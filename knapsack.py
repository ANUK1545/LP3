def knapsack(profit,weights,capacity):
    n=len(profit)
    dp=[[0 for w in range(capacity+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if(weights[i-1]<=w):
                dp[i][w]=max(profit[i-1]+dp[i-1][w-weights[i-1]],
                dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
profit=[1,2,5,6]
weights=[2,3,4,5]
capacity=8
knapsack(profit,weights,capacity)

