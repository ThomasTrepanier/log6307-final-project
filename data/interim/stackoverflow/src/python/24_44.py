def order_fillers(order,k):
    if len(order)==0 or k==0:
        return 0
    order.sort()
    max_orders=0
    for item in order:
        if k<=0:
            return max_orders
        if item<=k:
            max_orders+=1
            k-=item
    return max_orders
