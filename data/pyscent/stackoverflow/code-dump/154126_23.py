import math
def words_stats(list1, n1, list2, n2):
    # return total amount of words per partition + print to screen info
    bin_prod = math.comb(len(list1), n1) * math.comb(len(list2), n2)
    fact = math.factorial(n1 + n2)
    tot = bin_prod * fact
    print(f'{len(list1)}C{n1} x {len(list2)}C{n2}  x ({n1+n2})! = {bin_prod} x {fact} = {tot}')
    return tot

print('Info:')
amount_of_possibilities = 0
for k1, k2 in partitions:
    amount_of_possibilities += words_stats(list1, k1, list2, k2)
print(f'Total possible words: {amount_of_possibilities}')
