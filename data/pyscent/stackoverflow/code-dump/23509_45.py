# h(n) = 2 * h(n - 1) + 1
# h(1) = 1

def get_h_series(n):
    if n == 1:
        # h(1) = 1
        return [1]
    else:
        # ans = [h(0), h(1), ..., h(n - 1)]
        ans = get_h_series(n-1)
        # Append h(n) which is 2 * h(n - 1) + 1.
        ans.append(2 * ans[-1] + 1)
        # [h(0), h(1), ..., h(n - 1), h(n)]
        return ans

print(get_h_series(5))
