A, R, N = [int(x) for x in input().split()]

def solve(A: int, R: int, N: int):
    INF = 10**9
    x = A
    y = N - 1
    z = R
    while y:
        if y & 1:
            x *= z
            if x > INF:
                print("large")
                return
        y >>= 1
        z *= z
    print(x)

solve(A, R, N)
