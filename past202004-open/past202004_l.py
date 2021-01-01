from typing import List, Callable

N, K, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

class SegmentTree:
    def __init__(self, values: List[int], func: Callable[[int, int], int], default_value: int):
        l = len(values)
        self.func = func
        self.default_value = default_value
        self.num = 1 << (l - 1).bit_length()
        self.tree = [default_value] * 2 * self.num
        for i in range(l):
            self.tree[self.num + i] = values[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    def update(self, i: int, value: int):
        i += self.num
        self.tree[i] = value
        while i > 1:
            self.tree[i >> 1] = self.func(self.tree[i], self.tree[i ^ 1])
            i >>= 1
    def query(self, l: int, r: int):
        result = self.default_value
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                result = self.func(result, self.tree[l])
                l += 1
            if r & 1:
                result = self.func(result, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return result

def solve(N: int, K: int, D: int, A: List[int]):
    if N < D * (K - 1) + 1:
        print(-1)
        return
    st = SegmentTree(A, min, 10000000000000000)
    si = 0
    rs: List[int] = []
    for i in range(K):
        l = N - D * (K - 1 - i)
        m = st.query(si, l)
        rs.append(m)
        while A[si] != m:
            si += 1
        si += D
    print(*rs)

solve(N, K, D, A)
