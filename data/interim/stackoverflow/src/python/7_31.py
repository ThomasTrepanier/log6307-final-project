def rec_sum(n):
    sn = str(n)
    # base case - return the number
    if len(sn)==1:
        return n

    # not the base case,return whatever the recursive output returns
    return rec_sum(sum(map(int,sn)))


for n in range(1,71):
    print(f"{n:3}=>{rec_sum(n):3}", end = "|")
    if n%7 == 0:
        print()
