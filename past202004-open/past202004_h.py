from typing import List, Dict, Tuple

N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]

def solve(N: int, M: int, S: List[str]):
    ns: Dict[int, List[Tuple[int, int]]] = dict((i, []) for i in range(11))
    for y in range(N):
        for x in range(M):
            c = "S123456789G".index(S[y][x])
            ns[c].append((y, x))
    ds: Dict[Tuple[int, int], int] = {}
    ds[ns[0][0]] = 0
    LONG_D = 100000000000000000000
    for i in range(1, 11):
        for ty, tx in ns[i]:
            r = LONG_D
            for sy, sx in ns[i - 1]:
                v = abs(ty - sy) + abs(tx - sx) + ds[(sy, sx)]
                r = min(r, v)
            ds[(ty, tx)] = r
    result = ds[ns[10][0]]
    if result == LONG_D:
        print(-1)
        return
    print(result)

solve(N, M, S)
