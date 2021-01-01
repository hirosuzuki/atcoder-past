S = input()

def solve(S: str):
    rs = set([])
    for i in range(3):
        for j in range(len(S) - i):
            r = S[j:j+i+1]
            for k in range(2<<i):
                rr = list(r)
                for l in range(i + 1):
                    if k & (1 << l):
                        rr[l] = "."
                rs.add("".join(rr))
    print(len(rs))

solve(S)
