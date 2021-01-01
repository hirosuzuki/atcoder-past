from typing import List, Tuple, DefaultDict, Deque
from collections import defaultdict, deque

N = int(input())
Q = [input().split() for _ in range(N)]

def solve(N: int, Q: List[List[str]]):
    ss: Deque[Tuple[str, int]] = deque()
    for q in Q:
        if q[0] == "1":
            ss.append((q[1], int(q[2])))
        elif q[0] == "2":            
            d = int(q[1])
            cs: DefaultDict[str, int] = defaultdict(int)
            while d > 0 and ss:
                e = ss.popleft()
                r = min(d, e[1])
                cs[e[0]] += r
                d -= r
                if e[1] > r:
                    ss.appendleft((e[0], e[1] - r))
            print(sum(cs[c]**2 for c in cs))

solve(N, Q)
