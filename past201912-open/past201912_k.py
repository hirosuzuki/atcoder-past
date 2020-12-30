from typing import List, DefaultDict, Set
from collections import defaultdict

import sys
sys.setrecursionlimit(200000)

N = int(input())
P = [int(input()) for _ in range(N)]
Q = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(Q)]

def solve(N: int, P: List[int], Q: int, AB: List[List[int]]):
    ps: DefaultDict[int, Set[int]] = defaultdict(set)
    boss: int = 0
    for i, x in enumerate(P):
        if x == -1:
            boss = i + 1
        else:
            ps[x].add(i + 1)

    i = 0
    pos1 = [0] * (N + 1)
    pos2 = [0] * (N + 1)
    def dfs(ps: DefaultDict[int, Set[int]], p: int):
        nonlocal i
        pos1[p] = i
        i += 1
        for x in ps[p]:
            dfs(ps, x)
        pos2[p] = i

    dfs(ps, boss)

    for a, b in AB:
        if pos1[b] <= pos1[a] < pos2[b]:
            print("Yes")
        else:
            print("No")

solve(N, P, Q, AB)
