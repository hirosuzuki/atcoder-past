from typing import List

N, Q = [int(_) for _ in input().split()]
S: List[List[int]] = [[int(e) for e in input().split()] for _ in range(Q)]

def solve(N: int, Q: int, S: List[List[int]]):
    result: List[List[bool]] = [[False] * N for _ in range(N)]
    for s in S:
        if s[0] == 1:
            result[s[1] - 1][s[2] - 1] = True
        elif s[0] == 2:
            xs: List[int] = [i for i in range(N) if result[i][s[1] - 1]]
            for x in xs:
                if s[1] - 1 != x:
                    result[s[1] - 1][x] = True
        elif s[0] == 3:
            i: int
            for i, b in enumerate(result[s[1] - 1][:]):
                if b:
                    j: int
                    for j in range(N):
                        if result[i][j]:
                            if s[1] - 1 != j:
                                result[s[1] - 1][j] = True
    for row in result:
            print(*["NY"[c] for c in row], sep="")

solve(N, Q, S)
