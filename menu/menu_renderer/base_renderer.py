"""
4. Los dos renderers
Aquí es donde está la parte interesante.
Opción A: terminal con curses
Es la opción que elegiría si quieres algo funcional, elegante y relativamente sencillo de mantener.

Puedes conseguir:
- Navegación con flechas.
- Selección con Enter.
- Salir con Escape.
- Colores.
- Opciones resaltadas.
- Panel de información del laberinto.
- Mensajes de estado.
- Submenús.
- Indicadores de selección.
- Una interfaz que se actualice sin limpiar toda la terminal constantemente.
Por ejemplo, podrías tener:
╔══════════════════════════════════════════════╗
║                 A-MAZE-ING                   ║
╠══════════════════════════════════════════════╣
║                                              ║
║  MAZE INFORMATION                            ║
║  Size: 20 x 15                               ║
║  Algorithm: Recursive Backtracker            ║
║  Theme: Neon                                 ║
║  Shortest Path: Visible                      ║
║                                              ║
╠══════════════════════════════════════════════╣
║                                              ║
║  > Generate New Maze                         ║
║    Display Maze                              ║
║    Select Maze Theme                         ║
║    Change Wall Colours                       ║
║    Set Entry Point                           ║
║    Set Exit Point                            ║
║    Configure 42 Pattern                      ║
║    Show Shortest Path                         ║
║    Hide Shortest Path                         ║
║    Exit                                      ║
║                                              ║
╠══════════════════════════════════════════════╣
║  ↑ ↓ Navigate       ENTER Select             ║
╚══════════════════════════════════════════════╝

Lo interesante es que puedes utilizar curses para dibujar tanto el menú como el propio laberinto en la terminal.

Una advertencia sobre tu implementación actual: no mezclaría curses.wrapper() con print() e input() dentro de las acciones. Tu código actual sale temporalmente de curses con curses.endwin(), pero no restaura correctamente la interfaz para continuar el ciclo.

Lo correcto sería que los mensajes, submenús y entradas también se gestionasen mediante el renderer de curses.
Opción B: MiniLibX
Esta es la opción que elegiría si buscas una experiencia visual realmente potente.

Y aquí tengo una propuesta: no haría una ventana para el laberinto y otra para el menú.

Haría una única ventana de MiniLibX con dos zonas:
A-MAZE-ING
(RUNNING)

MAZE VISUALIZATION · 20 × 15

ALGORITHM

Backtracker

PATH

Visible
MAZE CONTROLS

› Generate New Maze

Display Maze

Select Maze Theme

Change Wall Colours

Set Entry Point

Set Exit Point

Configure 42 Pattern

Show Shortest Path

Hide Shortest Path

Exit Program
↑ ↓ NAVIGATE     ENTER SELECT     ESC EXIT

Concepto visual de una ventana única con el laberinto y el menú integrados. Es una referencia de diseño, no una captura real de MiniLibX.

La ventana tendría:
- Zona izquierda: laberinto.
- Zona derecha: menú.
- Parte inferior: información y mensajes.
- Selector visual que se desplaza por las opciones.
- Animaciones opcionales al regenerar el laberinto.
En MLX, la navegación se realizaría mediante callbacks de teclado y eventos de ventana.

Por ejemplo:
def on_key_press(keycode, param):    if keycode == KEY_UP:        menu.move_up()    elif keycode == KEY_DOWN:        menu.move_down()    elif keycode == KEY_ENTER:        menu.select_current_option()    elif keycode == KEY_ESC:        menu.exit_program()    return 0


Es código ilustrativo: los nombres y firmas exactos dependerán de los bindings de MiniLibX que estés utilizando.

La diferencia fundamental con curses es que MLX funciona mediante un bucle de eventos. No debes bloquearlo con un input() esperando que el usuario introduzca información.
"""

from abc import ABC, abstractmethod


class MenuRenderer(ABC):

    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def render(self, state) -> None:
        pass

    @abstractmethod
    def get_choice(self) -> str:
        pass

    @abstractmethod
    def show_message(self, message: str) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass