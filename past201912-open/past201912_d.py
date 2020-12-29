from typing import List

N: int = int(input())
A: List[int] = [int(input()) for _ in range(N)]

def solve(N: int, A: List[int]):
    cs: List[int] = [0] * (N + 1)
    i: int
    result: int = -1
    for i in range(N):
        cs[A[i]] += 1
        if cs[A[i]] >= 2:
            result = A[i]
    for i in range(1, N + 1):
        if cs[i] == 0:
            print(result, i)
            return
    print("Correct")

solve(N, A)
