from typing import List

N, M, Q = [int(x) for x in input().split()]
S = [[int(x) for x in input().split()] for _ in range(Q)]

def solve(N: int, M: int, Q: int, S: List[List[int]]):
    xs: List[int] = [N] * (M + 1)
    ss: List[List[int]] = [[] for _ in range(N + 1)]
    for r in S:
        if r[0] == 1:
            print(sum(xs[x] for x in ss[r[1]]))
        elif r[0] == 2:
            ss[r[1]].append(r[2])
            xs[r[2]] -= 1
            #print("*", ss, xs)

solve(N, M, Q, S)

