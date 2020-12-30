from typing import List

N = int(input())
A = [[0] * N for _ in range(N)]
for i in range(N - 1):
    for j, x in enumerate(input().split()):
        A[i][i + j + 1] = int(x)

def solve(N: int, A: List[List[int]]):
    cs: List[int] = [0] * (2**N)    
    for i in range(N):
        for j in range(2**i):
            cs[(1<<i) + j] = cs[j] + sum(A[k][i] for k in range(i) if j & (1<<k))
    result = -10000000000000000
    for i in range(2 ** N):
        for j in range(2 ** N):
            if i & j:
                continue
            k: int = (2**N - 1) - i - j
            r = cs[i] + cs[j] + cs[k]
            # print(i, j, k, r)
            result = max(result, r)
    print(result)

solve(N, A)
