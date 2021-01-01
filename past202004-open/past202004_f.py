from typing import List, DefaultDict
from collections import defaultdict
from heapq import heappop, heappush

N = int(input())
AB = [[int(x) for x in input().split()] for _ in range(N)]

def solve(N: int, AB: List[List[int]]):
    ts: DefaultDict[int, List[int]] = defaultdict(list)
    for a, b in AB:
        ts[a].append(b)
    h = []
    r = 0
    for i in range(N):
        for b in ts[i + 1]:
            heappush(h, -b)
        if h:
            r += -heappop(h)
        print(r)

solve(N, AB)
