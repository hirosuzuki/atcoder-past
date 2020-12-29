from typing import List

N: List[int] = [int(_) for _ in input().split()]

def solve(N: List[int]):
    result: int = sorted(N)[-3]
    print(result)

solve(N)
