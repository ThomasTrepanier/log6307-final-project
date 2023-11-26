A = [100,200,300,200,400,500,600,400,700,200,500,800]
B = [100,200,200,500,600,200,500]

def get_indices(A, B):
    a_it = enumerate(A)
    for n in B:
        for i, an in a_it:
            if n == an:
                yield i
                break
            
list(get_indices(A, B))
# [0, 1, 3, 5, 6, 9, 10]
