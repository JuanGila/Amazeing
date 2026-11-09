from collections import deque
import random
#from core.MazeDirections import MazeDirection
# from core.MazeCell import MazeCell

BIT = {"N": 1, "E": 2, "S": 4, "W": 8}
OPPOSITE = {"N": "S", "E": "W", "S": "N", "W": "E"}
DELTA = {"N" : (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def all_visited(x: int, y: int, visited: set[tuple[int, int]]) -> bool:
    dirs = list(DELTA)
    for d in dirs:
        dx, dy = DELTA[d]
        nx, ny = x + dx, y +dy
        if ((nx, ny) not in visited): return False
    return True


def search_square(x: int, y: int, grid: list[list[int]]) -> bool:
    for l in range(x, x + 2):
        for c in range(y, y + 2):
            if (grid[c][l] & BIT["E"] or grid[c][l] & BIT["S"]): return True
    return False


def makes_3_square(x: int, y: int, nx: int, ny: int, width: int, height: int, grid: list[list[int]], d: str) -> bool:
    min_x = max(0, min(x, nx) - 2)
    min_y = max(0, min(y, ny) - 2)
    max_x = min(width - 3, max(x ,nx))
    max_y = min(height - 3, max(y, ny))
    orig_val = grid[y][x]
    orig_nval = grid[ny][nx]
    grid[y][x] &= ~BIT[d]
    grid[ny][nx] &= ~BIT[OPPOSITE[d]]
    creates = False
    for sy in range(min_y, max_y + 1):
        for sx in range(min_x, max_x + 1):
            if not search_square(sx, sy, grid):
                creates = True
                break
        if creates: break
    grid[y][x] = orig_val
    grid[ny][nx] = orig_nval
    return creates


def bfs(width: int, height: int, start: tuple[int, int], seed: int | None, perfect: bool, logo: list[tuple[int, int]]) -> list[list[int]]:
    rng = random.Random(seed)
    queue = deque([start])
    visited = {start}
    grid = [[15] * width for _ in range(height)]
    if start in logo:
        raise ValueError("The start point (ENTRY) can not be on the logo.")
    while queue:
        dirs = list(DELTA)
        node = queue.pop()
        x, y = node
        rng.shuffle(dirs)
        visited.add(node)
        for d in dirs:
            dx, dy = DELTA[d]
            nx, ny = x + dx, y + dy
            if ((nx, ny) in logo): continue
            if (all_visited(x, y, visited) and not perfect):
                if (rng.random() < 0.25 and not makes_3_square(x, y, nx, ny, width, height, grid, d)):
                    grid[y][x] &= ~BIT[d]
                    grid[ny][nx] &= ~BIT[OPPOSITE[d]]
                    continue
            if ((nx ,ny) in visited): continue
            if not (0 <= nx < width and 0 <= ny < height): continue
            grid[y][x] &= ~BIT[d]
            grid[ny][nx] &= ~BIT[OPPOSITE[d]]
            queue.append((nx, ny))
            visited.add((nx, ny))
    return grid
