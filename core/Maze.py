""" IV.4 Maze Requirements
    •The maze must be randomly generated, but reproducibility via a seed is required.
    •Each cell of the maze has between 0 and 4 walls, at each cardinal point (North, East, South, West).
    •The maze must be valid, meaning:
        ◦Entry and exit exist and are different, inside the maze bounds.
        ◦The structure ensures full connectivity and no isolated cells (except the ’42’ pattern, see below).
        ◦As entry and exit are specific cells, there must be walls at the external borders.
        ◦Your generated data must be coherent: each neighbouring cell must have the
            same wall if any. E.g., it is forbidden to have a first cell with a wall on the
            east side, and the second cell behind that wall without a wall on the west side.
    •The maze can’t have large open areas. Corridors can’t be wider than 2 cells.
        For example, you can have 2x3 or 3x2 open area, but never a 3x3 open area.
    •When visually represented (see below), the maze must contain
        a visible “42” drawn by several fully closed cells.
    •If the PERFECT flag is activated, the maze must contain exactly one path between
        the entry and the exit (i.e., it must be a perfect maze: no loops at all).
    •If the PERFECT flag is not activated (the default), the maze must instead be a board
    directly usable by a Pac-Man-like game. Concretely:
        ◦every corridor is reachable (full connectivity), so the whole board can be filled
        with pac-gums and remains winnable;
        ◦the four corners and the centre are open corridors (the ghosts and super-pac-
        gums sit in the corners, the player starts in the centre);
        ◦it offers at least two independent routes (loops), so that a chased player
        always has an alternative (a perfect maze, or a perfect maze with merely one
        wall removed (a single loop), is therefore not acceptable in this mode);
        ◦dead-ends should stay rare (a couple are tolerated); a board with no dead-end
        at all is the ideal and is rewarded as a bonus (see the Bonuses chapter)

    INFO: The “42” pattern may be omitted in case the maze size does not allow
        it (i.e. too small). Print an error message on the console in that case.

The two generation modes on the same grid: PERFECT=True forces a single winding path (every other
corridor is a dead-end), while the default PERFECT=False keeps at least two independent routes open so
a chased player always has an alternative. The shortest path is highlighted in both.


                    Maze
                    │
        ┌───────────┴───────────┐
        │                       │
       Grid                    API
        │                       │
    ┌────┴────┐          ┌───────┴────────┐
    │         │          │                │
Cell      Cell      get_cell()     get_neighbor()
    │                    │                │
    ├── walls            │          open_wall()
    └── visited          │          close_wall()
                        │          has_wall()
                        │
                    to_hex()
"""


from pathlib import Path
from enum import IntEnum
from dataclasses import dataclass
from config import MazeConfig
from themes import MazeTheme


class MazeError(Exception):
    """Raised when a maze cannot be built, generated or solved."""


class MazeDirection(IntEnum):
    """Represent the four cardinal directions as wall bits.
    Esto es muy interesante porque
        el valor del enum es directamente el bit de la pared.
    """
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    @property
    def delta(self) -> tuple[int, int]:
        """Return the (x, y) movement delta for this direction."""
        # si falla probar con [self] a secas
        return {
            1: (0, -1),
            2: (1, 0),
            4: (0, 1),
            8: (-1, 0),
        }[self.value]
    @property
    def delta_claudia(self) -> tuple[int, int]:
        """Return the ``(dx, dy)`` offset for this direction."""
        if self == MazeDirection.NORTH:
            return (0, -1)
        if self == MazeDirection.EAST:
            return (1, 0)
        if self == MazeDirection.SOUTH:
            return (0, 1)
        if self == MazeDirection.WEST:
            return (-1, 0)
        raise MazeError(f"Dirección no válida: {self!r}")

    @property
    def opposite(self) -> "MazeDirection":
        """Return the opposite direction.
        Return the direction seen from the neighbouring cell.
        """
        if self == MazeDirection.NORTH:
            return MazeDirection.SOUTH
        if self == MazeDirection.EAST:
            return MazeDirection.WEST
        if self == MazeDirection.SOUTH:
            return MazeDirection.NORTH
        if self == MazeDirection.WEST:
            return MazeDirection.EAST
        raise MazeError(f"Dirección no válida: {self!r}")
        return MazeDirection((self.value << 2) % 15 or 1)


CARDINAL_DIRECTIONS: tuple[MazeDirection, ...] = (
    MazeDirection.NORTH,
    MazeDirection.EAST,
    MazeDirection.SOUTH,
    MazeDirection.WEST,
)


@dataclass
class MazeCell:
    """Represent a single cell of the maze.

    Attributes:
        walls: Bit mask representing the four walls.
        visited: Whether the cell has been visited by a generator.

    HABRA QUE VER/ESTUDIAR EL TEMA DEL COLOR DE LA CELDA.
    """
    walls: int = 0xF
    visited: bool = False
    cell_type: str = ""# ColorType.BACKGROUND

    def has_wall(self, direction: MazeDirection) -> bool:
        """Return whether the cell has a wall in a direction.

        Args:
            direction: Direction to check.
        Returns:
            True if the wall is closed, otherwise False.

        Supongamos:
            walls = 1011

        y comprobamos EAST:
        1011
        0010
        ----
        0010

        El operador & ->
            Compara cada bit y devuelve 1 solo si ambos bits son 1.
        Resultado distinto de cero: True
        Por tanto EAST está cerrada.
        """
        return bool(self.walls & direction)

    def add_wall(self, direction: MazeDirection) -> None:
        """Close a wall in the given direction.

        Args:
            direction: Direction of the wall to close.

        Utilizamos:
            self.walls |= direction
        Por ejemplo:
            1101
            0010
            ----
            1111
        Y vuelve a cerrarse.
        """
        self.walls |= direction

    def remove_wall(self, direction: MazeDirection) -> None:
        """Open a wall in the given direction.(Desactivar un bit)

        Args:
            direction: Direction of the wall to open.

        Por ejemplo:
        walls     = 1111
        EAST      = 0010
        ~EAST     = ...1101

        Resultado:
        1111
        1101
        ----
        1101
        """
        self.walls &= ~direction

    def is_fully_closed(self) -> bool:
        """Return whether all four walls are closed."""
        return self.walls == 0xF

    def to_hex(self) -> str:
        """Return the cell wall representation as one hexadecimal digit."""
        return format(self.walls, "X")


class Maze:
    """Represent the complete internal structure of a maze."""

    def __init__(self, maze_conf: MazeConfig) -> None:
        """Create a maze with all walls initially closed.

        Args:
            maze_config: Configuration of the maze.
        Raises:
            INCORRECTO(NO DEBERIA LANZAR NINGUN ERROR, ES UN INIT) -> ValueError: If width or height is not positive.
        """
        self.shortest_path: str = "NSEW"
        self._maze_config: MazeConfig = maze_conf
        self._maze_theme: MazeTheme = MazeTheme(
            self._maze_config.maze_renderer_type,
            self._maze_config.maze_theme
        )
        self.grid: list[list[MazeCell]] = [
            [MazeCell() for _ in range(maze_conf.maze_width)]
            for _ in range(maze_conf.maze_height)
        ]
        self.logo(self._maze_config.maze_height, self._maze_config.maze_width)


    def get_logo(
        self, height: int, width: int
    ) -> list[tuple[int, int]] | None:        
        if (height < 7 or width < 9): return None
        middlex, middley = width // 2, height // 2
        values = []
        logo_positions = [
            (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-3, -2), (-1, 1), (-1, 2),
            (1, 0), (2, 0), (3, 0), (3, -1), (3, - 2), (2, -2), (1, -2),
            (1, 1), (1, 2), (2, 2), (3, 2)
        ]
        for dx, dy in logo_positions:
            x = middlex + dx
            y = middley + dy
            if (0 <= x < width and 0 <= y < height):
                values.append((x, y))
        return values
        """ 
        for i in range(1, 4):
            values.append((middlex - i, middley))
            values.append((middlex + i, middley))
            values.append((middlex - 1, middley + i - 1))
            values.append((middlex + 1, middley + i - 1))
            values.append((middlex - 3, middley - i + 1))
            values.append((middlex + 1 + i, middley + i - 1))
            values.append((middlex + 3, middley - i + 1))
            values.append((middlex + 1 + i, middley - 2))
        return values
        """

    def get_maze_config(self) -> MazeConfig:
        return self._maze_config

    def set_maze_config(self, new_maze_config: MazeConfig) -> None:
        """"Se modificara el objeto correspondiente
        en la MazeConfig(usando validate-assigment)y se envia aqui la nueva con
        la modificacion validada."""
        self._maze_config = new_maze_config

    def get_maze_theme(self) -> MazeTheme:
        return self._maze_theme

    def set_maze_theme(self, new_maze_theme: MazeTheme) -> None:
        self._maze_theme = new_maze_theme

    def is_inside(self, x: int, y: int) -> bool:
        """Return whether coordinates are inside the maze."""
        valid_width = 0 <= x < self._maze_config.maze_width
        valid_height = 0 <= y < self._maze_config.maze_height
        return valid_width and valid_height

    def get_cell(self, x: int, y: int) -> MazeCell:
        """Return the cell at the given coordinates.
        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
        Returns:
            The requested MazeCell.
        Raises:
            IndexError: If coordinates are outside the maze.
        """
        if not self.is_inside(x, y):
            raise IndexError(
                f"Coordinates ({x}, {y}) are outside the maze."
            )
        return self.grid[y][x]

    def get_neighbor(
        self, x: int, y: int, direction: MazeDirection
    ) -> tuple[int, int] | None:
        """Return the coordinates of a neighbouring cell.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
            direction: MazeDirection in which to look.
        Returns:
            Neighbor coordinates, or None if there is no neighbour.
        """
        dx, dy = direction.delta
        neighbor_x = x + dx
        neighbor_y = y + dy
        if not self.is_inside(neighbor_x, neighbor_y):
            return None
        return neighbor_x, neighbor_y

    def open_wall(self, x: int, y: int, direction: MazeDirection) -> bool:
        """Open a wall and its matching neighbour wall.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
            direction: MazeDirection of the wall to open.
        Returns:
            True if the wall was opened, False if no neighbour exists.
        Raises:
            IndexError: If the source coordinates are outside the maze.

        Esta función es fundamental:
            maze.open_wall(2, 2, Direction.EAST)
                        EAST
            Cell A  ───────────>  Cell B
                │                     │
                │                     │
                └─────────────────────┘

        Y modifica las dos celdas:
            A.EAST = 0
            B.WEST = 0
        Esto nos garantiza automáticamente la coherencia
        exigida por el enunciado:
            cada pared compartida debe estar codificada
            de la misma forma en ambas celdas.
        Esta decisión nos va a ahorrar muchos bugs posteriormente.

        7. ¿Qué pasa si intentamos abrir hacia fuera?
        Por ejemplo:
            maze.open_wall(0, 0, Direction.WEST)

        No existe una celda a la izquierda.

        Entonces:
            neighbor = None
        y devolvemos:
            False
        No abrimos la pared.

        Esto es importante porque el PDF exige
            que los bordes exteriores permanezcan cerrados.

        Por tanto:
            maze.has_wall(0, 0, Direction.WEST)

        seguirá devolviendo:
            True
        """
        cell = self.get_cell(x, y)
        neighbor = self.get_neighbor(x, y, direction)
        if neighbor is None:
            return False
        neighbor_x, neighbor_y = neighbor
        neighbor_cell = self.get_cell(neighbor_x, neighbor_y)
        cell.remove_wall(direction)
        neighbor_cell.remove_wall(direction.opposite())
        return True

    def close_wall(self, x: int, y: int, direction: MazeDirection) -> bool:
        """Close a wall and its matching neighbour wall.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
            direction: MazeDirection of the wall to close.
        Returns:
            True if the wall was closed, False if no neighbour exists.
        Raises:
            IndexError: If the source coordinates are outside the maze.
        """
        cell = self.get_cell(x, y)
        neighbor = self.get_neighbor(x, y, direction)
        if neighbor is None:
            return False
        neighbor_x, neighbor_y = neighbor
        neighbor_cell = self.get_cell(neighbor_x, neighbor_y)
        cell.add_wall(direction)
        neighbor_cell.add_wall(direction.opposite())
        return True

    def has_wall(self, x: int, y: int, direction: MazeDirection) -> bool:
        """Return whether a cell has a wall in a direction."""
        return self.get_cell(x, y).has_wall(direction)

    def mark_visited(self, x: int, y: int) -> None:
        """Mark a cell as visited."""
        self.get_cell(x, y).visited = True

    def reset_visited(self) -> None:
        """Mark every cell as unvisited."""
        for row in self.grid:
            for cell in row:
                cell.visited = False

    def get_all_cells(self) -> list[tuple[int, int, MazeCell]]:
        """Return all maze cells with their coordinates(x, y)."""
        return [
            (x, y, self.grid[y][x])
            for y in range(self._maze_config.maze_height)
            for x in range(self._maze_config.maze_width)
        ]

    def to_hex_grid(self) -> list[str]:
        """Return the maze using one hexadecimal digit per cell."""
        return [
            "".join(cell.to_hex() for cell in row)
            for row in self.grid
        ]

    def write_hex_maze_on_file(self) -> None:
        """
        Write the maze to a file in hexadecimal format,
            along with entry and exit coordinates.
        Usage:
            maze_config = MazeConfig.from_file(file)
            a_maze_ing = Maze(maze_config)
            a_maze_ing.write_hex_maze_on_file()

        • After an empty line, the following 3 elements are inserted
        in the output file on 3 lines:
            ◦ the entry coordinates,
            ◦ the exit coordinates
            ◦ the shortest valid path from entry to exit,
                using the four letters N , E , S , W .
        • All lines end with a \n .
        """
        with open(self._maze_config.output_file, "w") as file:
            for row in self.to_hex_grid():
                file.write(row + "\n")
            file.write(self._maze_config.maze_entry)
            file.write("\n")
            file.write(self._maze_config.maze_exit)
            file.write("\n")
            # Escribimos the shortest valid path from entry to exit, using the four letters N , E , S , W .
            file.write(self.shortest_path + "\n")

    def display_maze(self) -> None:
        """Function that displays the maze based in self._maze_theme.renderer_type"""
        pass
    def regenerate_maze(self) -> None:
        """Function that regenerates the maze based in self._maze_config.maze_algorithm"""
        pass

    def cells(self) -> Iterator[tuple[int, int]]:
        """Yield every cell coordinate in row-major order."""
        for y in range(self.height):
            for x in range(self.width):
                yield x, y

    def non_pattern_cells(self) -> list[tuple[int, int]]:
        """Return every walkable coordinate, excluding the ``42`` cells."""
        return [
            (x, y)
            for x, y in self.cells()
            if (x, y) not in self.pattern42_cells
        ]

    def open_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        """Return neighbours reachable through open passages."""
        if (x, y) in self.pattern42_cells:
            return []
        result: list[tuple[int, int]] = []
        for direction in CARDINAL_DIRECTIONS:
            neighbor = self.get_neighbor(x, y, direction)
            if neighbor is None or neighbor in self.pattern42_cells:
                continue
            neighbor_x, neighbor_y = neighbor
            if self.has_wall(x, y, direction):
                continue
            if self.has_wall(
                neighbor_x,
                neighbor_y,
                direction.opposite,
            ):
                continue
            result.append(neighbor)
        return result

    def region(
        self, start: tuple[int, int] | None = None
    ) -> set[tuple[int, int]]:
        """Return every cell connected to ``start`` through passages."""
        origin = self.entry if start is None else start
        self.get_cell(*origin)
        seen: set[tuple[int, int]] = {origin}
        pending: list[tuple[int, int]] = [origin]
        while pending:
            current = pending.pop()
            for neighbor in self.open_neighbors(*current):
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        return seen

    def is_fully_connected(self) -> bool:
        """Return whether every non-``42`` cell belongs to one region."""
        target = set(self.non_pattern_cells())
        if not target:
            return True
        return self.region(self.entry) == target

    def count_passages(self) -> int:
        """Return the number of open passages between adjacent cells."""
        total = 0
        for x, y in self.non_pattern_cells():
            for direction in (MazeDirection.EAST, MazeDirection.SOUTH):
                neighbor = self.get_neighbor(x, y, direction)
                if neighbor is None:
                    continue
                if neighbor in self.pattern42_cells:
                    continue
                neighbor_x, neighbor_y = neighbor
                if self.has_wall(x, y, direction):
                    continue
                if self.has_wall(
                    neighbor_x,
                    neighbor_y,
                    direction.opposite,
                ):
                    continue
                total += 1
        return total

    def count_loops(self) -> int:
        """Return the number of independent cycles in the walkable graph."""
        cells = self.non_pattern_cells()
        if not cells:
            return 0
        remaining = set(cells)
        components = 0
        while remaining:
            start = remaining.pop()
            component = self.region(start)
            remaining.difference_update(component)
            components += 1
        return self.count_passages() - len(cells) + components

    def dead_end_cells(self) -> list[tuple[int, int]]:
        """Return walkable cells with exactly one open passage.

        This includes cells enclosed by the ``42`` pattern.  Use
        :meth:`real_dead_end_cells` to count only the ones that could
        still be connected to another normal cell.
        """
        return [
            (x, y)
            for x, y in self.non_pattern_cells()
            if len(self.open_neighbors(x, y)) == 1
        ]

    def _has_openable_wall(self, x: int, y: int) -> bool:
        for direction in CARDINAL_DIRECTIONS:
            neighbor = self.get_neighbor(x, y, direction)
            if neighbor is None:
                continue
            if neighbor in self.pattern42_cells:
                continue
            if self.has_wall(x, y, direction):
                return True
        return False

    def real_dead_end_cells(self) -> list[tuple[int, int]]:
        """Return dead ends with at least one wall openable to a cell."""
        return [
            (x, y)
            for x, y in self.dead_end_cells()
            if self._has_openable_wall(x, y)
        ]

    def enclosed_dead_end_cells(self) -> list[tuple[int, int]]:
        """Return dead ends surrounded only by the border or ``42`` cells."""
        real = set(self.real_dead_end_cells())
        return [
            cell for cell in self.dead_end_cells() if cell not in real
        ]

    def has_open_3x3(self) -> bool:
        """Return whether the maze contains a fully open ``3x3`` area."""
        for top in range(self.height - 2):
            for left in range(self.width - 2):
                if self._is_open_block(left, top):
                    return True
        return False

    def _is_open_block(self, left: int, top: int) -> bool:
        for y in range(top, top + 3):
            for x in range(left, left + 3):
                cell = self.get_cell(x, y)
                if x < left + 2 and cell.has_wall(MazeDirection.EAST):
                    return False
                if y < top + 2 and cell.has_wall(MazeDirection.SOUTH):
                    return False
        return  True

    def to_hex_rows(self) -> list[str]:
        """Return one hexadecimal string per maze row."""
        return [
            "".join(cell.to_hex() for cell in row)
            for row in self.grid
        ]

    def to_hex_grid(self) -> list[str]:
        """Alias for :meth:`to_hex_rows` kept for convenience."""
        return self.to_hex_rows()