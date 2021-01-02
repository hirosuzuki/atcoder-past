from typing import List, DefaultDict, Set
from collections import defaultdict

N, M, Q = [int(x) for x in input().split()]
V = [[int(x) for x in input().split()] for _ in range(M)]
C = [int(x) for x in input().split()]
S = [[int(x) for x in input().split()] for _ in range(Q)]

def solve(N: int, M: int, Q: int, V: List[List[int]], C: List[int], S: List[List[int]]):
    cs = C[:]
    ms: DefaultDict[int, Set[int]] = defaultdict(set)
    for v0, v1 in V:
        ms[v0 - 1].add(v1 - 1)
        ms[v1 - 1].add(v0 - 1)
    for s in S:
        if s[0] == 1:
            print(cs[s[1] - 1])
            for x in ms[s[1] - 1]:
                cs[x] = cs[s[1] - 1]
        elif s[0] == 2:
            print(cs[s[1] - 1])
            cs[s[1] - 1] = s[2]

solve(N, M, Q, V, C, S)

