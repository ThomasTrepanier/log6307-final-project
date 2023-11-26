A = [1,2,3,41,10,5,3,100]
B = [10,21,22,4,18,1,2,9]

odd_lst = []
even_lst = []


def is_even_odd(item):
    if int(item) % 2 == 0:
        even_lst.append(item)
    else:
        odd_lst.append(item)

for a_item, b_item in zip(A,B):
    is_even_odd(a_item)
    is_even_odd(b_item)


print([item for tup in zip(odd_lst, even_lst) for item in tup])
