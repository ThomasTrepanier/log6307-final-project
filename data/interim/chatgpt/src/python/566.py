def Zero_One_Knapsack(n, wt, vals, W):
    # make a matrix of size W+1 x n+1
    K = [["." for _ in range(W+1)] for _ in range(n+1)]
    # initialize the first row and column to 0
    for i in range(n+1):
        K[i][0] = 0
    for j in range(W+1):
        K[0][j] = 0
    # fill in the rest of the matrix
    for i in range(1, n+1):  # Iterate through items
        for w in range(1, W+1):  # Iterate through weight capacity
            if wt[i-1] <= w:
                K[i][w] = max(vals[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    # print the matrix
    for row in K:
        print(row)
    # return the last element of the matrix
    return K[n][W]
