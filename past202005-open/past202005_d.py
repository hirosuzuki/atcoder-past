from typing import List
N = int(input())
S = [input() for _ in range(5)]


Pattern = """
.###..#..###.###.#.#.###.###.###.###.###.
.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.
.#.#..#..###.###.###.###.###...#.###.###.
.#.#..#..#.....#...#...#.#.#...#.#.#...#.
.###.###.###.###...#.###.###...#.###.###.
""".strip().split()

def solve(N: int, S: List[str]):
    P = ["".join(Pattern[j][i*4+1:i*4+4] for j in range(5)) for i in range(10)]
    xs = ["".join(S[j][i*4+1:i*4+4] for j in range(5)) for i in range(N)]
    print(*[P.index(x) for x in xs], sep="")

solve(N, S)
