from typing import List, Tuple

N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(N)]
CD = [[int(_) for _ in input().split()] for _ in range(M)]

def solve(N: int, M: int, AB: List[List[int]], CD: List[List[int]]):

    def calc(k: float) -> List[Tuple[float, int, int]]:
        sab = sorted([(b - k * a, a, b) for a, b in AB])
        scd = sorted([(d - k * c, c, d) for c, d in CD])
        if sum(x[0] for x in sab[-5:]) >= 0:
            return sab[-5:]
        if sum(x[0] for x in sab[-4:]) + scd[-1][0] >= 0:
            return sab[-4:] + scd[-1:]
        return []

    maxv: float = 100000
    minv: float = 1/100000
    last_result: List[Tuple[float, int, int]] = []
    for _ in range(30):
        v = (maxv + minv) / 2
        r = calc(v)
        if r:
            minv = v
            last_result = r
        else:
            maxv = v

    result = sum(x for _, _, x in last_result) / sum(x for _, x, _ in last_result)
    print(result)

solve(N, M, AB, CD)
