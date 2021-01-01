S = input()

def solve(S: str):
    i: int = 0
    def calc() -> str:
        nonlocal i
        s = ""
        while i < len(S):
            c = S[i]
            i += 1
            if c == "(":
                s += calc()
            elif c == ")":
                return s + s[::-1]
            else:
                s += c
        return s
    print(calc())

solve(S)
