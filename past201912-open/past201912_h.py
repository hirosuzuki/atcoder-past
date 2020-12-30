from typing import List

N = int(input())
C = [int(_) for _ in input().split()]
Q = int(input())
S = [[int(_) for _ in input().split()] for _ in range(Q)]

def solve(N: int, C:List[int], Q:int, S:List[List[int]]):
    result = 0
    even_min = min(C[::2])
    even_bottom = 0
    odd_min = min(C[1::]) if C[1::] else 100000000000000000
    odd_bottom = 0
    for r in S:
        if r[0] == 1:
            i, a = r[1] - 1, r[2]
            if i % 2 == 0:
                if C[i] - even_bottom >= a:
                    result += a
                    C[i] -= a
                    even_min = min(even_min, C[i])
            else:
                if C[i] - odd_bottom >= a:
                    result += a
                    C[i] -= a
                    odd_min = min(odd_min, C[i])
        elif r[0] == 2:
            a = r[1]
            if even_min - even_bottom >= a:
                even_bottom += a
                result += a * ((N + 1) // 2)
        elif r[0] == 3:
            a = r[1]
            if even_min - even_bottom >= a and odd_min - odd_bottom >= a:
                even_bottom += a
                odd_bottom += a
                result += a * N
    print(result)

solve(N, C, Q, S)
