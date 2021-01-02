S = input()
T = input()

def solve(S: str, T: str):
    if S == T:
        print("same")
    elif S.upper() == T.upper():
        print("case-insensitive")
    else:
        print("different")

solve(S, T)
