"""Placement of the mandatory ``42`` glyph.

The glyph is made of fully closed cells.  Its position is chosen as close
as possible to the centre of the maze while respecting the entry, the
exit, the four corners and the central cell or cells.  If no valid
position exists, the pattern is omitted and a Spanish warning is returned.
"""

from __future__ import annotations

from dataclasses import dataclass

GLYPH_ROWS: tuple[str, ...] = (
    "1010111",
    "1010001",
    "1110111",
    "0010100",
    "0010111",
)
GLYPH_WIDTH: int = 7
GLYPH_HEIGHT: int = 5
MIN_WIDTH: int = GLYPH_WIDTH + 2
MIN_HEIGHT: int = GLYPH_HEIGHT + 2
MARGIN: int = 1
SEARCH_RADIUS: int = 3

Warning = str | None
Position = tuple[int, int]


@dataclass(frozen=True)
class Pattern42Placement:
    """Result of trying to place the ``42`` pattern.

    Attributes:
        cells: Coordinates occupied by the glyph.
        present: Whether the pattern was placed.
        warning: Spanish warning when the pattern is omitted.
    """

    cells: frozenset[Position]
    present: bool
    warning: Warning = None


def corner_cells(width: int, height: int) -> set[Position]:
    """Return the four corner cells of a maze."""
    return {
        (0, 0),
        (width - 1, 0),
        (0, height - 1),
        (width - 1, height - 1),
    }


def central_cells(width: int, height: int) -> set[Position]:
    """Return the central cell or cells of a maze.

    Odd axes have one central coordinate.  Even axes have two, because
    neither of them can be considered more central than the other.
    """
    xs: tuple[int, ...]
    ys: tuple[int, ...]
    if width % 2 == 1:
        xs = (width // 2,)
    else:
        xs = (width // 2 - 1, width // 2)
    if height % 2 == 1:
        ys = (height // 2,)
    else:
        ys = (height // 2 - 1, height // 2)
    return {(x, y) for x in xs for y in ys}


def _glyph_cells(left: int, top: int) -> frozenset[Position]:
    cells = {
        (left + column, top + row)
        for row, glyph_row in enumerate(GLYPH_ROWS)
        for column, value in enumerate(glyph_row)
        if value == "1"
    }
    return frozenset(cells)


def _candidate_origins(width: int, height: int) -> list[Position]:
    base_left = (width - GLYPH_WIDTH) // 2
    base_top = (height - GLYPH_HEIGHT) // 2
    candidates: set[Position] = set()
    for delta_y in range(-SEARCH_RADIUS, SEARCH_RADIUS + 1):
        for delta_x in range(-SEARCH_RADIUS, SEARCH_RADIUS + 1):
            left = base_left + delta_x
            top = base_top + delta_y
            if not (MARGIN <= left <= width - GLYPH_WIDTH - MARGIN):
                continue
            if not (MARGIN <= top <= height - GLYPH_HEIGHT - MARGIN):
                continue
            candidates.add((left, top))

    def score(origin: Position) -> tuple[int, int, int]:
        left, top = origin
        horizontal = abs(2 * left - (width - GLYPH_WIDTH))
        vertical = abs(2 * top - (height - GLYPH_HEIGHT))
        return (horizontal + vertical, top, left)

    return sorted(candidates, key=score)


def _complement_is_connected(
    width: int,
    height: int,
    blocked: frozenset[Position],
) -> bool:
    total = width * height - len(blocked)
    start: Position | None = None
    for y in range(height):
        for x in range(width):
            if (x, y) not in blocked:
                start = (x, y)
                break
        if start is not None:
            break
    if start is None:
        return False

    seen: set[Position] = {start}
    pending: list[Position] = [start]
    offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while pending:
        x, y = pending.pop()
        for delta_x, delta_y in offsets:
            neighbor = (x + delta_x, y + delta_y)
            if not (0 <= neighbor[0] < width):
                continue
            if not (0 <= neighbor[1] < height):
                continue
            if neighbor in blocked or neighbor in seen:
                continue
            seen.add(neighbor)
            pending.append(neighbor)
    return len(seen) == total


def _try_placement(
    width: int,
    height: int,
    protected: set[Position],
) -> frozenset[Position] | None:
    for left, top in _candidate_origins(width, height):
        cells = _glyph_cells(left, top)
        if cells & protected:
            continue
        if _complement_is_connected(width, height, cells):
            return cells
    return None


def place_pattern42(
    width: int,
    height: int,
    entry: Position,
    exit: Position,
    enabled: bool = True,
) -> Pattern42Placement:
    """Try to place the ``42`` pattern inside a maze.

    The glyph is centred when possible.  It is omitted when the maze is
    too small, when every candidate position collides with a protected
    cell, or when the remaining cells would not be connected.

    Args:
        width: Maze width in cells.
        height: Maze height in cells.
        entry: Entry coordinates as ``(x, y)``.
        exit: Exit coordinates as ``(x, y)``.
        enabled: Whether the caller wants the pattern.

    Returns:
        A placement describing the selected cells and the result.
    """
    if not enabled:
        return Pattern42Placement(frozenset(), False, None)
    if width < MIN_WIDTH or height < MIN_HEIGHT:
        return Pattern42Placement(
            frozenset(),
            False,
            "El patrón 42 se omite: el laberinto debe medir al menos "
            "9x7 celdas.",
        )

    base_protected = corner_cells(width, height) | {entry, exit}
    all_centres = central_cells(width, height)
    primary_centre = {(width // 2, height // 2)}

    cells = _try_placement(
        width,
        height,
        base_protected | all_centres,
    )
    if cells is not None:
        return Pattern42Placement(cells, True, None)

    if all_centres != primary_centre:
        cells = _try_placement(
            width,
            height,
            base_protected | primary_centre,
        )
        if cells is not None:
            return Pattern42Placement(cells, True, None)

    message = (
        "El patrón 42 se omite: no existe una posición centrada que "
        "evite la entrada, la salida, las esquinas y el centro sin "
        "desconectar el resto del laberinto."
    )
    return Pattern42Placement(frozenset(), False, message)
