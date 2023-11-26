def filledOrders(order, k):
  total = 0
  for i, v in enumerate(sorted(order)):
    if total + v <= k:
      total += v       # total stays <= k
    else:
      return i         # provides the count
  else:
    return len(order)  # was able to place all orders

print(filledOrders([3, 2, 1], 3))  # Out: 2
print(filledOrders([3, 2, 1], 1))  # Out: 1
print(filledOrders([3, 2, 1], 10)) # Out: 3
print(filledOrders([3, 2, 1], 0))  # Out: 0
