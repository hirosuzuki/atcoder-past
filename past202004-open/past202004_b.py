S = input()

def solve(S: str):
    vs = {"a": 0, "b": 0, "c": 0}
    for c in S:
        vs[c] += 1
    result = sorted("abc", key=lambda x:vs[x])[-1]
    print(result)

solve(S)
