
import random

BIT = {"N": 1, "E": 2, "S": 4, "W": 8}
OPPOSITE = {"N": "S", "S": "N", "E": "W", "W": "E"}
DELTA = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def ft_hunt(
        seen: set[tuple[int, int]], width: int, height: int,
        grid: list[list[int]], rng: random.Random, logo: list[tuple[int, int]]
        )-> tuple[int, int] | None:
    for y in range(height):
        for x in range(width):
            if (x, y) in seen:
                continue
            dirs = neighbours((x, y), seen, width, height, True, logo)
            if (dirs):
                carve((x, y), rng.choice(dirs), grid, logo)
                return (x, y)
    return None


def inbounds(x: int, y: int, width: int, height: int) -> bool:
    return(0 <= x < width and 0 <= y < height)


def carve(position: tuple[int, int], d: str, grid: list[list[int]], logo: list[tuple[int, int]]) -> None:
    x, y = position
    dx, dy = DELTA[d]
    nx, ny = x + dx, y + dy
    if((nx, ny) in logo): return
    grid[y][x] &= ~BIT[d]
    grid[ny][nx] &= ~BIT[OPPOSITE[d]]


def neighbours(
        position: tuple[int, int], seen: set[tuple[int, int]], width: int,
        height: int, visited: bool, logo: list[tuple[int ,int]]):
    x, y = position
    if ((x, y) in logo): return None
    res = []
    for dir, (dx, dy) in DELTA.items():
        nx = x + dx
        ny = y + dy
        if (inbounds(nx, ny, width, height) and ((nx, ny) in seen) == visited):
            res.append(dir)
    return res
    

def search_square(x: int, y: int, grid: list[list[int]]) -> bool:
    for l in range(x, x + 2):
        for c in range(y, y + 2):
            if (grid[c][l] & BIT["E"] or grid[c][l] & BIT["S"]): return True
    return False


def makes_3_square(x: int, y: int, nx: int, ny: int, width: int, height: int, grid: list[list[int]], d: str, logo: list[tuple[int, int]]) -> bool:
    if ((nx, ny) in logo): return
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


def hunt_and_kill(width: int, height: int, start: tuple[int, int], seed: int | None, perfect: bool, logo: list[tuple[int, int]]) -> list[list[int]]:
    rng = random.Random(seed)
    grid = [[15] * width for _ in range(height)]
    seen = {start} | set(logo)
    if start in logo:
        raise ValueError("El punto de entrada (ENTRY) no puede estar dentro del logo.")
    x, y = start
    while True:
        dirs = neighbours((x, y), seen, width, height, False, logo)
        if (dirs):
            d = rng.choice(dirs)
            carve((x, y), d, grid, logo)
            dx, dy = DELTA[d]
            x, y = x + dx, y + dy
            seen.add((x, y))
        else:
            cell = ft_hunt(seen, width, height, grid, rng, logo)
            if cell is None:
                break
            x, y = cell
            seen.add((x, y))

#3 anidados, igual se puede hacer a la vez qye se genera o quitar el tercer for cogiendo solamente una direccion
    if not (perfect):
        for cy in range(height):
            for cx in range(width):
                if (rng.random() < 0.15):
                    dirs = list(DELTA)
                    rng.shuffle(dirs)
                    for d in dirs:
                        dx, dy = DELTA[d]
                        nx, ny = cx + dx, cy + dy
                        if ((nx, ny) in logo): continue
                        if (inbounds(nx, ny, width, height) and (grid[cy][cx] & BIT[d]) and not makes_3_square(cx, cy, nx, ny, width, height, grid, d, logo)):
                            grid[cy][cx] &= ~BIT[d]
                            grid[ny][nx] &= ~BIT[OPPOSITE[d]]
    return grid
