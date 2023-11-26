def list_h_results(n):
    h_results = []
    for i in range(1, n+1):
        h_results.append(2 * h_results[-1] + 1)
    return h_results
