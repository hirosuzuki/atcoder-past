S:str = input()

def solve(S: str) -> str:
    if all("0" <= c <= "9" for c in S):
        return str(int(S) * 2)
    return "error"

print(solve(S))