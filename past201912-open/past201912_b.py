from typing import List

N: int = int(input())
A: List[int] = [int(input()) for _ in range(N)]

def solve(N: int, A: List[int]):
    i: int
    for i in range(1, N):
        if A[i - 1] < A[i]:
            print("up", A[i] - A[i - 1])
        elif A[i - 1] > A[i]:
            print("down", A[i - 1] - A[i])
        else:
            print("stay")

solve(N, A)
