from typing import List, DefaultDict
from collections import defaultdict

N = int(input())
S = input()
C = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

def solve(N: int, S: str, C: List[int], D: List[int]):
    M = 10000000000000
    ns: DefaultDict[int, int] = defaultdict(lambda :M)
    ns[0] = 0
    for s, c, d in zip(S, C, D):
        nns: DefaultDict[int, int] = defaultdict(lambda :M)
        for x, y in ns.items():
            nns[x] = y + d
        if s == "(":
            for x, y in ns.items():
                nns[x + 1] = min(nns[x + 1], y)
                if x - 1 >= 0:
                    nns[x - 1] = min(nns[x - 1], y + c)
        elif s == ")":
            for x, y in ns.items():
                nns[x + 1] = min(nns[x + 1], y + c)
                if x - 1 >= 0:
                    nns[x - 1] = min(nns[x - 1], y)
        ns = nns
    print(ns[0])

solve(N, S, C, D)
