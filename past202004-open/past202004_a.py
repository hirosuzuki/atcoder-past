S, T = input().split()

def solve(S: str, T: str):
    def calc(x: str) -> int:
        if x[0] == "B":
            return -int(x[1]) + 1
        return int(x[0])
    print(abs(calc(T) - calc(S)))

solve(S, T)
