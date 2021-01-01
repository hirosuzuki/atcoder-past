from typing import List, Tuple

N, W, C = [int(_) for _ in input().split()]
LRP = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, W: int, C: int, LRP: List[List[int]]):
    vs: List[Tuple[int, int]] = []
    MH: int = 10000000000000000000000000000
    h: int = 0
    for l, r, p in LRP:
        if l - C < 0:
            h += p
        else:
            vs.append((l - C, p))
        vs.append((r, -p))
    vs.append((W - C, MH))
    vs.sort()
    result = h
    for _, v in vs:
        if v == MH:
            break
        h += v
        result = min(result, h)
    print(result)

solve(N, W, C, LRP)
