""" Chapter V
Visual representation
Your program must provide a way to display the maze visually, using either:
• Terminal ASCII rendering, or
• A graphical display using the MiniLibX (MLX) library.


The visual should clearly show walls, entry, exit, and the solution path.

User interactions must be available, at least for the following tasks:
• Re-generate a new maze and display it -> OPCIONES 1 Y 2.
• Show/Hide a valid shortest path from the entrance to the exit -> OPCIONES 8 Y 9.
• Change maze wall colours -> OPCION 4
• Optional: set specific colours to display the “42” pattern -> OPCION 7


You can add extra user interactions.
"""
import sys
import curses
from typing import Any, Callable, TextIO

from core import Maze
from themes import MAZE_THEMES, MAZE_RENDERERS


class MazeMenu:
    """Lector de opciones del menú con validación de entrada.

    Args:
        amazeing_maze: Instancia de la clase Maze
        input_stream: Flujo de entrada. Por defecto, ``sys.stdin``.
        output_stream: Flujo de salida. Por defecto, ``sys.stdout``.
    """
    def __init__(
        self, amazeing_maze: Maze,
        input_stream: TextIO | Any = sys.stdin,
        output_stream: TextIO | Any = sys.stdout
    ):
        self.maze_menu_options: dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("Re-generate a new maze", self.regenerate_maze),
            "2": ("Display Maze", self.display_maze),
            # creo que esto es inutil, ya que el laberinto se muestra siempre resuelto, resolver el mazo entra dentro de las acciones a realizar en bulce en el programa
            "X": ("Solve Maze", self.solve_maze),
            "3": ("Select Maze Theme", self.select_maze_theme),
            "4": ("Select Maze Renderer", self.select_maze_renderer),
            "5": ("Set Entry Point", self.set_entry_point),
            "6": ("Set Exit Point", self.set_exit_point),
            "7": ("Select 42 Pattern Colour", self.select_42_pattern_colour),
            "8": ("Show Shortest Path", self.show_shortest_path),
            "9": ("Hide Shortest Path", self.hide_shortest_path),
            "10": ("Exit Program", self.exit_program),
        }
        self.maze: Maze = amazeing_maze
        self.input_stream = input_stream
        self.output_stream = output_stream

    def display_menu(self) -> None:
        print("Maze Menu:")
        for key, value in self.maze_menu_options.items():
            print(f"{key}. {value[0]}")

    def handle_choice(self) -> Callable[[], None]:
        user_choice = input("Elige una opcion: ").strip()
        while user_choice not in self.maze_menu_options:
            print("Opcion invalida, por favor intentelo de nuevo.")
            user_choice = input("Elige una opcion: ").strip()
        return self.maze_menu_options[user_choice][1]()

    def regenerate_maze(self) -> None:
        print("Regenerating a new maze...")
        # Implement the logic to regenerate a new maze. Creo que hay que ejecutar el mazegenerator
        self.maze.regenerate_maze()

    def display_maze(self) -> None:
        """"
        CUANDO SE REGENERA EL MAZO UNA VEZ YA MOSTRADO, SE REGENERA Y SE MUESTRA OTRA VEZ,
        PERO SI EN EL MENU SE CAMBIA EL THEME(sin cambiar la config)
        Y LUEGO SE DECIDE MOSTRAR HAY QUE MOSTRAR EL MAZE ACTUAL
        SIN REGENERARLO CON EL NUEVO THEME
        """
        print("Displaying the maze...")
        self.maze.display_maze()

    def select_maze_solve_algorithm(self) -> None:# Esta funcion tiene sentido si tenemos 2 algoritmos para resolver(a* + ¿claudia?)
        print("Solving the maze...")
        # Implement the logic to solve the maze and display the solution path
        maze_solver = "";

    def select_maze_theme(self) -> None:
        maze_themes: list[str] = MAZE_THEMES.keys()
        print(f"Selecting the maze theme ...")
        maze_theme = self.maze.get_maze_theme()
        print(f"Selected theme: {maze_theme.theme_name}")
        print("Available Maze Themes:")
        for index, theme in enumerate(maze_themes):
            print(f"{index}: {theme}")
        choice = input("Select a maze theme: ").strip()
        while not choice.isdigit() or not 0 <= int(choice) < len(maze_themes):
            print("Invalid choice. Please try again.")
            choice = input("Select a maze theme: ").strip()
        maze_theme.set_theme_name(maze_themes[int(choice)])
        self.maze.set_maze_theme(maze_theme)
        print(f"Selected theme: {maze_theme.theme_name}")
        # CUIDADO, CADA VEZ QUE SE CAMBIA EL THEME HAY QUE EJECUTAR display_maze() con el nuevo tema y visualizarlo creo(con la opcion display-maze).

    def select_maze_renderer(self) -> None:
        maze_renderers: list[str] = MAZE_RENDERERS.keys()
        print(f"Selecting the maze renderer ...")
        maze_theme = self.maze.get_maze_theme()
        print(f"Selected renderer: {maze_theme.theme_renderer}")
        print("Available Maze Renderers:")
        for index, theme in enumerate(maze_renderers):
            print(f"{index}: {theme}")
        choice = input("Select a maze renderer: ").strip()
        while not choice.isdigit() or not 0 <= int(choice) < len(maze_renderers):
            print("Invalid choice. Please try again.")
            choice = input("Select a maze renderer: ").strip()
        maze_theme.set_theme_renderer(maze_renderers[int(choice)])
        self.maze.set_maze_theme(maze_theme)
        print(f"Selected theme: {maze_theme.theme_name}")

    def set_entry_point(self) -> None:
        print("Setting entry point...")
        x, y = input(
            "Set the coordinates for the entry point(x,y): "
        ).strip().split(",", 2)
        while not self.maze.is_inside(x, y):
            print("Invalid coordinates. Please try again.")
            x, y = input(
                "Set the coordinates for the entry point(x,y): "
            ).strip().split(",", 2)
        #self.maze.get_maze_config().set_maze_entry_point((x, y))
        self.maze.get_maze_config().maze_entry = (x, y)
        """ CUIDADO:
        HAY QUE VER SI SE HAN DE ABRIR O CERRAR CELDAS CUANDO SE ESTABLECE UN PUNTO DE ENTRADA EN WALLS CERRADOS
        NUNCA PODRA SER EL 42(LA SEED) O EL OTRO PUNTO(EL DE SALIDA)
        """

    def set_exit_point(self) -> None:
        print("Setting exit point...")
        x, y = input(
            "Set the coordinates for the exit point(x,y): "
        ).strip().split(",", 2)
        while not self.maze.is_inside(x, y):
            print("Invalid coordinates. Please try again.")
            x, y = input(
                "Set the coordinates for the exit point(x,y): "
            ).strip().split(",", 2)
        """ CUIDADO:
        HAY QUE VER SI SE HAN DE ABRIR O CERRAR CELDAS CUANDO SE ESTABLECE UN PUNTO DE SALIDA EN WALLS CERRADOS
        NUNCA PODRA SER EL 42(LA SEED) O EL OTRO PUNTO(EL DE ENTRADA)
        """
        self.maze.get_maze_config().maze_exit = (x, y)

    def select_42_pattern_colour(self) -> None:
        print("Displaying 42 pattern colour...")
        # Implement the logic to display the 42 pattern colour

    def show_shortest_path(self) -> None:
        print("Showing the shortest path ...")
        # Implement the logic to show the shortest path from entry to exit

    def hide_shortest_path(self) -> None:
        print("Hiding the shortest path ...")
        # Implement the logic to hide the shortest path from entry to exit

    def exit_program(self) -> None:
        print("Exiting program ...")
        exit()#self.running = False

    def run(self) -> None:
        """Start the interactive terminal menu."""
        curses.wrapper(self._run_menu)

    def _run_menu(self, stdscr: curses.window) -> None:
        """Handle keyboard navigation and menu rendering."""
        curses.curs_set(0)
        stdscr.keypad(True)
        options = list(self.maze_menu_options.values())
        selected = 0
        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            title = "A-MAZE-ING"
            stdscr.addstr(1, max(0, (width - len(title)) // 2), title)
            for index, (label, _) in enumerate(options):
                y = 3 + index
                if y >= height - 2:
                    break
                x = 4
                text = f"> {label}" if index == selected else f"  {label}"
                if index == selected:
                    stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, text[:max(0, width - x - 1)])
                if index == selected:
                    stdscr.attroff(curses.A_REVERSE)
            footer = "UP/DOWN: Navigate | ENTER: Select | ESC: Exit"
            stdscr.addstr(
                height - 1,
                0,
                footer[:max(0, width - 1)]
            )
            stdscr.refresh()
            key = stdscr.getch()
            if key == curses.KEY_UP:
                selected = (selected - 1) % len(options)
            elif key == curses.KEY_DOWN:
                selected = (selected + 1) % len(options)
            elif key in (curses.KEY_ENTER, 10, 13):
                # Temporarily leave curses before running normal input/print methods.
                curses.endwin()
                options[selected][1]()
                stdscr.clear()
                #stdscr.refresh() - vibecoding
            elif key == 27:
                break

    # Opcion 2
    def render_menu(theme_name: str, algorithm: str, show_path: bool) -> str:
        """Construye el texto del menú con el estado actual."""
        path_state = "visible" if show_path else "oculto"
        lines = [
            "",
            "=== A-Maze-ing ===",
            f"Tema: {theme_name} | Algoritmo: {algorithm} | "
            f"Camino: {path_state}",
            "",
        ]
        for option in MENU_OPTIONS:
            lines.append(f"{option.key}. {option.label}")
        return "\n".join(lines)

    def prompt(
        self, theme_name: str,
        algorithm: str, show_path: bool
    ) -> int | None:
        """Pide una opción válida.

        Returns:
            El número de opción elegido, o ``None`` si la entrada se
            ha cerrado inesperadamente.
        """
        while True:
            self.output_stream.write(
                render_menu(theme_name, algorithm, show_path) + "\n"
            )
            self.output_stream.write("> ")
            self.output_stream.flush()
            raw_line = self.input_stream.readline()
            if raw_line == "":
                self.output_stream.write("\n")
                return None
            text = raw_line.strip()
            try:
                choice = int(text)
            except ValueError:
                self._show_invalid()
                continue
            if choice < 1 or choice > EXIT_OPTION:
                self._show_invalid()
                continue
            return choice

    def _show_invalid(self) -> None:
        """Informa de una opción no válida sin terminar el programa."""
        self.output_stream.write(
            "Opción no válida. Introduce un número del 1 al "
            f"{EXIT_OPTION}.\n"
        )

"""
Una consideración importante: tus métodos actuales utilizan print() e input().
curses controla la terminal y puede interferir con esas operaciones.
En el ejemplo he añadido curses.endwin() antes de ejecutar la opción, para que puedas probarlas con la terminal normal.
Si quieres que, después de ejecutar una opción, el menú siga funcionando de forma fiable,
    conviene restaurar el modo curses tras cada acción y gestionar los mensajes de resultado dentro de la interfaz.

Con esto ya tienes la base de navegación por flechas.
No necesitas implementar todavía el generador ni el solver para probarla:
    puedes seleccionar las opciones que ya tienes y comprobar que se ejecutan cuando pulsas Enter.
"""


"""Compatibility exports for the terminal menu."""

from app.menu import MENU_OPTIONS, Menu, render_menu

__all__ = ["MENU_OPTIONS", "Menu", "render_menu"]