from typing import List, Tuple
from math import sqrt

N, M = [int(_) for _ in input().split()]
XYC = [[int(_) for _ in input().split()] for _ in range(N)]
SXYC = [[int(_) for _ in input().split()] for _ in range(M)]


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x


def solve(N: int, M: int, XYC: List[List[int]], SXYC: List[List[int]]):

    def calc(XYC: List[List[int]]):
        N = len(XYC)
        vs: List[Tuple[int, int, float]] = []
        for i in range(N):
            for j in range(i + 1, N):
                d = sqrt((XYC[i][0] - XYC[j][0])**2 + (XYC[i][1] - XYC[j][1])**2)
                if XYC[i][2] != XYC[j][2]:
                    d *= 10
                vs.append((i, j, d))
        uf = UnionFind(N + 1)
        r: float = 0
        for i, j, d in sorted(vs, key=lambda x:x[2]):
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                r += d
        return r

    result = 10000000000000000000000000000

    for i in range(2**M):
        xyc = XYC[:]
        for j in range(M):
            if i & (1<<j):
                xyc.append(SXYC[j])
        r = calc(xyc)
        result = min(result, r)

    print(result)

solve(N, M, XYC, SXYC)
