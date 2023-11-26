def print_pyramid(_count = 1):
  if _count < 10:
    print((lambda x:x[::-1] if not _count%2 else x)(''.join(map(str, range(1, _count+1)))))
    print_pyramid(_count+1)


print_pyramid()
