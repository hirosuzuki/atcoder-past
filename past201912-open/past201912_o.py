from typing import List, Dict

N = int(input())
A = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, A: List[List[int]]):
    xs: List[int] = [0]
    dice_of_x: Dict[int, int] = {}
    for i in range(N):
        for x in A[i]:
            xs.append(x)
            dice_of_x[x] = i
    xs.sort()
    rank_of_x: Dict[int, int] = dict((y, i) for i, y in enumerate(xs))

    dp: List[float] = [0.0] * (N * 6 + 1)
    r = 0.0

    for i in reversed(range(N * 6)):
        v = xs[i]
        dice_no = dice_of_x[xs[i + 1]]
        r = max(r, sum((dp[rank_of_x[n]] + 1) / 6 for n in A[dice_no] if n > v))
        dp[i] = r

    print(dp[0] + 1)
    return

solve(N, A)
