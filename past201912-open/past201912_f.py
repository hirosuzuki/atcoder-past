from typing import List

S = input()

def solve(S: str):
    xs: List[str] = []
    i: int = 0
    si: int = -1
    while i < len(S):
        c = S[i]
        if "A" <= c <= "Z":
            if si < 0:
                si = i
            else:
                xs.append(S[si:i + 1])
                si = -1
        i += 1
    print(*sorted(xs, key=lambda x:x.upper()), sep="")

solve(S)