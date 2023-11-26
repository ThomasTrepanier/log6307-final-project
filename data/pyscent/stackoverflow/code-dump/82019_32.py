def valid(num, count=None):
    if count is None:
        count = int(num==0)
    num, r = divmod(num, 10)
    if num == 0:
        return count%2==0
    else:
        return valid(num, count=count+int(r==0))
