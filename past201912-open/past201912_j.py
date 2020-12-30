from typing import List
from heapq import heappush, heappop

H, W = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for _ in range(H)]

def solve(H: int, W: int, A: List[List[int]]):
    def calc(H: int, W: int, A: List[List[int]], y: int, x: int) -> List[List[int]]:
        MD = 1000000000
        rs = [[MD] * W for _ in range(H)]
        h = []
        heappush(h, (0, x, y))
        while h:
            d, x, y = heappop(h)
            if rs[y][x] != MD:
                continue
            rs[y][x] = d
            for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H:
                    nd = d + A[ny][nx]
                    if rs[ny][nx] == MD:
                        heappush(h, (nd, nx, ny))
        return rs
    rs0 = calc(H, W, A, H - 1, 0)
    rs1 = calc(H, W, A, H - 1, W - 1)
    rs2 = calc(H, W, A, 0, W - 1)
    result = 100000000000000
    for y in range(H):
        for x in range(W):
            r = rs0[y][x] + rs1[y][x] + rs2[y][x] - A[y][x] * 2
            result = min(result, r)
    print(result)

solve(H, W, A)
