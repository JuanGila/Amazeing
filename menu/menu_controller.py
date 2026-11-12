

class MenuController:

    def __init__(self, maze, renderer):
        self.maze = maze
        self.renderer = renderer
        self.running = True

        self.options = {
            "1": self.regenerate_maze,
            "2": self.display_maze,
            "3": self.select_maze_theme,
            "4": self.select_maze_renderer,
            "5": self.set_entry_point,
            "6": self.set_exit_point,
            "7": self.select_42_pattern_colour,
            "8": self.show_shortest_path,
            "9": self.hide_shortest_path,
            "10": self.exit_program,
        }

    def run(self):
        while self.running:
            choice = self.renderer.get_choice()
            action = self.options.get(choice)
            if action is None:
                self.renderer.show_message("Invalid option")
                continue
            action()


"""
def on_key_press(keycode, param):
    if keycode == KEY_UP:
        menu.move_up()

    elif keycode == KEY_DOWN:
        menu.move_down()

    elif keycode == KEY_ENTER:
        menu.select_current_option()

    elif keycode == KEY_ESC:
        menu.exit_program()

    return 0


6. Algunas cosas que cambiaría de tu código actual
He revisado el archivo que has compartido y hay varios detalles que corregiría antes de seguir desarrollando el menú.

1. Eliminaría la opción X: Solve Maze.

Estoy de acuerdo con tu comentario: si el programa siempre genera y resuelve el laberinto inicialmente, no tiene mucho sentido tener una opción independiente para resolverlo, salvo que quieras permitir resolverlo de nuevo después de cambiar la entrada o la salida.

2. Unificaría la opción 4.

En tu código es Select Maze Renderer, pero el enunciado pide expresamente cambiar los colores de las paredes. Son funcionalidades diferentes. Puedes tenerlas ambas, pero no deberías dejar sin cubrir la interacción obligatoria de colores.

3. NO HAY NADA UTIL EN ESTE PUNTO

4. Evitaría que las acciones controlen directamente la interfaz.

Por ejemplo, regenerate_maze() no debería decidir cómo se dibuja el laberinto. Debería modificar el estado y solicitar una actualización al sistema de visualización.

5. Mantendría el estado del menú.

Deberías poder conocer:
- Opción seleccionada.
- Tema actual.
- Renderer actual.
- Estado de visualización del camino.
- Mensajes pendientes.
- Estado de ejecución.
Esto te permitirá implementar submenús sin complicar el controlador principal.

"""