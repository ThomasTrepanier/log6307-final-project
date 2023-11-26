import os, sys

def max_fulfilled_orders(order_arr, k):
    
    # track the max no.of orders in the arr.
    max_num = 0
    # order count, can be fulfilled.
    order_count = 0
    
    # iter over order array
    for i in range(0, len(order_arr)):
        # if remain value < 0 then
        if k - order_arr[i] < 0:
            # add the max no.of orders to total
            k += max_num
            if order_count > 0:
                # decrease order_count
                order_count -= 1
                
        # if the remain value >= 0
        if(k - order_arr[i] >= 0):
            # subtract the current no.of orders from total.
            k -= order_arr[i]
            # increase the order count.
            order_count += 1
            # track the max no.of orders till the point.
            if order_arr[i] > max_num:
                max_num = order_arr[i]

    return order_count


print(max_fulfilled_orders([3, 2, 1], 0))  # Out: 0
print(max_fulfilled_orders([3, 2, 1], 1))  # Out: 1
print(max_fulfilled_orders([3, 1, 1], 2))  # Out: 2
print(max_fulfilled_orders([3, 2, 4], 9)) # Out: 3
print(max_fulfilled_orders([3, 2, 1, 4], 10)) # Out: 4
