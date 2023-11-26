def solve(A):
            x = ['a', 'e','i','o', 'u', 'A', 'E', 'I', 'O', 'U']
            ans = 0

            for i in range(len(A)):
                if A[i] in x:
                    ans = (ans + len(A)-i)%10003
            return ans
