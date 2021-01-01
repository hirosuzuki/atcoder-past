from typing import List

N = int(input())
A = [int(x) for x in input().split()]

def solve(N: int, A: List[int]):
    rs = [1] * (2**N)
    def calc(A: List[int], i: int, j: int) -> int:
        if i + 2 == j:
            if A[i] > A[j - 1]:
                rs[i] += 1
                return i
            rs[j - 1] += 1
            return j - 1
        else:
            x = calc(A, i, (i + j) // 2)
            y = calc(A, (i + j) // 2, j)
            if A[x] > A[y]:
                rs[x] += 1
                return x
            rs[y] += 1
            return y            
    if N >= 2:
        calc(A, 0, 2**(N-1))
        calc(A, 2**(N-1), 2**N)
    print(*rs, sep="\n")

solve(N, A)
