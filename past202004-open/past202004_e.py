from typing import List

N = int(input())
A = [int(x) for x in input().split()]

def solve(N: int, A: List[int]):
    rs = []
    for i in range(N):
        x = i + 1
        r = 1
        while i + 1 != A[x - 1]:
            x = A[x - 1]
            r += 1
        rs.append(r)
    print(*rs)

solve(N, A)
