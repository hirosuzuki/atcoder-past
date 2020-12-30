from typing import List, Dict

N, M = [int(_) for _ in input().split()]
S: List[str] = []
C: List[int] = []
for _ in range(M):
    xs = input().split()
    S.append(xs[0])
    C.append(int(xs[1]))

def solve(N: int, M: int, S: List[str], C: List[int]):
    ss: List[int] = []
    for i in range(M):
        ss.append(int(S[i].replace("Y", "1").replace("N", "0"), 2))
    rs: Dict[int, int] = {0: 0}
    for j in range(M):
        for k, v in list(rs.items()):
            nk = k | ss[j]
            if nk in rs:
                rs[nk] = min(rs[nk], v + C[j])
            else:
                rs[nk] = v + C[j]
    k = 2**N-1
    if k in rs:
        print(rs[k])
    else:
        print(-1)

solve(N, M, S, C)
