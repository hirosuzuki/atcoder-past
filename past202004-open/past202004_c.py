from typing import List

N = int(input())
S = [input() for _ in range(N)]

def solve(N: int, S: List[str]):
    cs: List[List[str]] = [[]] * N
    for i in range(N):
        y = N - i - 1
        cs[y] = list(S[y])
        if i > 0:
            for x in range(i, 2 * N - 1 - i):
                if "X" in cs[y + 1][x - 1: x + 2]:
                    cs[y][x] = "X"
    for row in cs:
        print(*row, sep="")

solve(N, S)
