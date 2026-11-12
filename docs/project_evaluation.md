## 🚀 A-Maze-Ing Tests

## 📌 0. Guidelines

### ⚠️ Rules

- La evaluación debe realizarse de forma respetuosa, constructiva y seria.
- La revisión se realiza únicamente sobre el contenido existente en el **repositorio Git del alumno o del grupo**.
- Verifica que el repositorio pertenece al alumno/grupo y que corresponde al proyecto evaluado.
- Comprueba que `git clone` se realiza en una carpeta vacía.
- Comprueba que no se han utilizado aliases maliciosos para mostrar contenido diferente al repositorio oficial.
- El evaluador y el evaluado deben revisar los posibles scripts utilizados para facilitar la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, debe leer previamente el subject completo.
- No se modifica ningún archivo salvo que sea estrictamente necesario y, en ese caso, se explica previamente al evaluado y ambos deben estar de acuerdo.
- Durante la defensa no se permite una terminación inesperada, prematura o no controlada del programa.
- Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.
- Si el trabajo está vacío, incompleto, no funciona, contiene un error de norma o se detecta cheating, la evaluación puede finalizar con la nota correspondiente según la escala.

### 📁 Expected repository contents

Comprueba que están presentes:

- `README.md`
- `LICENSE.md`
- `a_maze_ing.py`
- `mazegen-*.tar.gz` y/o fichero `.whl`
- Fichero de configuración
- Todos los elementos necesarios para volver a construir el paquete del generador de laberintos
- Los ficheros Python deben pasar `flake8`.
- El código debe pasar `mypy`.

Si falta alguno de los elementos obligatorios, la evaluación obtiene **0**.

### 🚩 Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, utiliza la flag correspondiente:

- **Empty work → El repositorio está vacío**
- **Incomplete work → Falta trabajo obligatorio**
- **Norme → Error de norma / `flake8`**
- **Cheat → Uso de cheating o contenido no autorizado**
- **Crash → Terminación inesperada o programa no funcional**
- **Incomplete group → El grupo no está completo**
- **Concerning situation → Situación preocupante**
- **Can't support / explain code → El alumno no puede explicar o defender el código**

---

# 📄 1. README.md

**Archivo:** `README.md`

### 🔍 Required content

- El archivo existe en la raíz del repositorio.
- La primera línea está en cursiva y tiene exactamente el formato:
  `This project has been created as part of the 42 curriculum by <login>, <login>.`
- Existe una sección **Description** que explica el propósito y ofrece una visión general del proyecto.
- Existe una sección **Instructions** con información relevante sobre compilación, instalación y/o ejecución.
- Existe una sección **Resources** con referencias externas y explicación del uso de IA, indicando para qué tareas y partes del proyecto se utilizó.
- Se documenta completamente el fichero de configuración.
- Se indica el algoritmo utilizado para generar el laberinto.
- Se explica por qué se eligió dicho algoritmo.
- Se incluye documentación breve sobre el módulo reutilizable del maze generator.
- Se documenta la gestión del proyecto y del equipo:
  - Roles de cada miembro.
  - Planificación prevista y cómo evolucionó.
  - Qué funcionó bien y qué podría mejorarse.
  - Herramientas específicas utilizadas.
- Se permiten otras secciones relevantes.

### 🧪 README Tests

| Prueba | Esperado |
|---|---|
| `README.md` en la raíz | Presente |
| Primera línea obligatoria | Formato correcto |
| Description | Presente |
| Instructions | Presente |
| Resources | Presente |
| Uso de IA documentado | Presente |
| Configuración documentada | Completa |
| Algoritmo explicado | Presente |
| Motivo de elección del algoritmo | Presente |
| Módulo reutilizable documentado | Presente |
| Roles y planificación | Documentados |
| Herramientas utilizadas | Documentadas |

---

# 🎮 2. Standard Usage

**Archivo principal:** `a_maze_ing.py`

### ▶️ Execution

Ejecuta:

```bash
python3 a_maze_ing.py
```

utilizando el fichero de configuración por defecto.

### 🔍 Functionality

- Se genera un laberinto aleatoriamente.
- El laberinto se muestra en el terminal o mediante una ventana gráfica dedicada.
- El programa permite interactuar con el laberinto.
- Se puede regenerar un nuevo laberinto.
- Existe un control para mostrar/ocultar el camino más corto desde la entrada hasta la salida.
- Existe un botón/control para cambiar los colores de las paredes.
- Se pueden implementar interacciones adicionales, pero las anteriores son las obligatorias.

### 🧪 Interactive Menu Tests

| Prueba | Resultado esperado |
|---|---|
| Ejecutar con configuración por defecto | Se genera y muestra un laberinto |
| Regenerar laberinto | Se genera un nuevo laberinto |
| Mostrar shortest path | El camino aparece correctamente |
| Ocultar shortest path | El camino deja de mostrarse |
| Cambiar color de paredes | El color cambia correctamente |
| Interacción general | El programa continúa funcionando sin terminación inesperada |

---

# ⚙️ 3. Configuration File

### 📌 Format

El fichero de configuración debe respetar:

- Las líneas de comentario empiezan por `#`.
- Cada línea de configuración utiliza el formato `KEY=VALUE`.
- Se permite utilizar minúsculas para las claves.
- Deben estar presentes las claves:
  - `WIDTH`
  - `HEIGHT`
  - `ENTRY`
  - `EXIT`
  - `OUTPUT_FILE`
  - `PERFECT`

### 🧪 Error Management Tests

Edita temporalmente la configuración para comprobar:

| Caso | Resultado esperado |
|---|---|
| Eliminar una clave obligatoria | Error gestionado correctamente |
| Línea sin `=` | Error gestionado correctamente |
| Sustituir números por letras | Error gestionado correctamente |
| Boolean incorrecto para `PERFECT` | Error gestionado correctamente |
| `ENTRY` con formato incorrecto | Error gestionado correctamente |
| `EXIT` con formato incorrecto | Error gestionado correctamente |
| Error de configuración | No debe producir una terminación inesperada |

> ⚠️ Si una prueba provoca una terminación inesperada del programa durante la defensa, la evaluación se detiene y la nota final es 0.

---

# 🧱 4. Output File

### ▶️ Generation

Ejecuta `a_maze_ing.py` y verifica que el primer laberinto generado y mostrado también se guarda en el fichero definido por `OUTPUT_FILE`.

### 🔍 Required format

El fichero de salida debe contener:

1. `HEIGHT` líneas.
2. Cada línea debe contener exactamente `WIDTH` caracteres.
3. Una línea vacía.
4. La tupla `ENTRY`.
5. La tupla `EXIT`.
6. El camino más corto desde entrada hasta salida utilizando únicamente:
   - `N`
   - `E`
   - `S`
   - `W`

### 🧪 Maze Analyzer

Ejecuta:

```bash
python3 maze_analyzer.py <output_file>
```

Comprueba:

- Coherencia de las paredes.
- Que el laberinto coincide con el modo indicado en `PERFECT`.
- Que no existe incoherencia estructural.
- Que el modo **perfect maze** se corresponde con `PERFECT=True`.
- Que el modo **Pac-Man-usable** se corresponde con `PERFECT=False`.
- Que la secuencia del shortest path coincide con su representación visual.

Cualquier incoherencia o mismatch hace que esta cuestión falle.

---

# 🌀 5. Maze Generator Module

## 🔧 Maze Generation

El módulo debe cumplir las expectativas del subject.

### 🔍 Functionality

- El laberinto se genera aleatoriamente.
- Puede utilizarse un módulo estándar de Python como `random`.
- Se gestiona correctamente la entrada cuando los parámetros son inconsistentes:
  - `ENTRY` fuera del laberinto.
  - `EXIT` fuera del laberinto.
  - `WIDTH` negativa.
  - `HEIGHT` negativa.
  - Otros parámetros inconsistentes.
- Todas las celdas son alcanzables, salvo las que eventualmente formen el patrón `42`.
- Existen paredes alrededor de todo el laberinto.
- No existe una zona abierta de `3x3` o mayor sin paredes.
- El patrón `42` está presente cuando el tamaño lo permite.
- Si el tamaño no permite crear el patrón `42`, se muestra un mensaje por terminal.

### 🔢 PERFECT=True

Cuando `PERFECT=True`:

- El laberinto es un **perfect maze**.
- Existe exactamente un camino entre entrada y salida.
- No existen loops.

### 👾 PERFECT=False

Cuando `PERFECT=False`:

- El laberinto funciona como un tablero para un juego tipo Pac-Man.
- Todos los corredores son alcanzables.
- Las cuatro esquinas están abiertas.
- El centro está abierto.
- Existen al menos dos rutas independientes.
- Se toleran algunos dead-ends.

### 🎲 Reproducibility

- Con una seed idéntica debe poder reproducirse el mismo laberinto.
- Comprueba esta propiedad modificando la configuración o el código según corresponda.

### 🧪 Objective Tests

Genera un laberinto con cada modo:

```bash
PERFECT=True
python3 maze_analyzer.py <output_file>
```

Debe informar de un **PERFECT maze**.

Después:

```bash
PERFECT=False
python3 maze_analyzer.py <output_file>
```

Debe informar de un **Pac-Man-USABLE**.

Comprueba también:

- Número de loops.
- Número de dead-ends.
- Umbrales indicados por el analyzer.
- Conectividad.
- Coherencia del patrón `42`.
- Reproducibilidad con seed idéntica.

### 🧠 Questions to ask

- ¿Qué algoritmo utilizaste para generar el laberinto?
- ¿Por qué elegiste ese algoritmo?
- ¿Cómo garantizas que todas las celdas son alcanzables?
- ¿Cómo controlas `PERFECT=True` frente a `PERFECT=False`?
- ¿Cómo evitas zonas abiertas de `3x3` o mayores?
- ¿Cómo implementaste o verificaste el patrón `42`?
- ¿Cómo haces que una misma seed produzca el mismo laberinto?

---

# 📦 6. Reusable Maze Generator Module

### ▶️ Package regeneration

El alumno/equipo debe volver a generar el paquete, preferiblemente dentro de un virtualenv o entorno equivalente.

La operación debe volver a crear:

- `mazegen-*.tar.gz`
- y/o el fichero `.whl`

### 🧪 Installation Test

En un **virtualenv diferente**:

1. Instala el paquete recién generado.
2. Utiliza el paquete instalado desde el nuevo entorno.
3. Ejecuta `a_maze_ing.py`.
4. Utiliza su fichero de configuración.
5. Comprueba que todo sigue funcionando correctamente.

### 🔍 Expected result

- El paquete se genera correctamente.
- El paquete se instala correctamente.
- `a_maze_ing.py` utiliza correctamente el módulo instalado.
- El fichero de configuración sigue funcionando.
- El comportamiento del generador es correcto después de la instalación.

---

# 🧹 7. Code Quality & Best Practices

## 🐍 Python

- El código Python pasa `flake8`.
- El código pasa `mypy`.
- No existen errores de norma relevantes.
- Los tipos están correctamente definidos.
- El código es legible y estructurado.
- La gestión de errores es clara.
- Las salidas del programa son comprensibles.
- La implementación no depende de resultados hardcodeados.

## 🧩 Maze Generator

- La lógica de generación está separada adecuadamente.
- El módulo es reutilizable.
- La generación es realmente aleatoria cuando corresponde.
- La seed se respeta correctamente.
- La lógica de `PERFECT` está implementada de forma real.
- La conectividad se comprueba correctamente.
- El formato del output es coherente con la especificación.

## 📦 Packaging

- El paquete puede reconstruirse.
- El paquete puede instalarse en un entorno limpio.
- El programa funciona utilizando el paquete generado.
- No depende accidentalmente del entorno de desarrollo original.

---

# ⭐ 8. Bonuses

> Los bonuses solo pueden considerarse si todas las cuestiones anteriores han sido superadas correctamente.

Se pueden validar hasta **5 bonuses** diferentes, siempre que cada uno represente una cantidad razonable de trabajo.

### Possible bonuses

#### 🌀 No dead-ends

- El laberinto por defecto no contiene ningún dead-end.
- Ejecuta:

```bash
python3 maze_analyzer.py <output_file> --max-dead-ends 0
```

- El resultado debe seguir siendo **Pac-Man-USABLE**.
- El analyzer debe reportarlo como bonus-grade.

#### 🔀 Multiple algorithms

- Soporte para múltiples algoritmos de generación de laberintos.
- El alumno debe poder explicar las diferencias y demostrar que ambos funcionan.

#### 🎞️ Animation

- Existe animación durante la generación del laberinto.
- La animación debe funcionar realmente y no ser únicamente decorativa o hardcodeada.

### 🧪 Bonus evaluation

| Bonus | Comprobación |
|---|---|
| No dead-ends | Analyzer con `--max-dead-ends 0` |
| Multiple algorithms | Demostrar y explicar varios algoritmos |
| Animation | Ejecutar y observar la generación animada |
| Otros | Deben representar una cantidad razonable de trabajo |

---

# 🚩 9. Defense

## 💬 Questions

1. ¿Qué algoritmo has utilizado para generar el laberinto?

2. ¿Por qué has elegido ese algoritmo?

3. ¿Cómo garantizas que todas las celdas del laberinto son alcanzables?

4. ¿Qué diferencia hay entre `PERFECT=True` y `PERFECT=False`?

5. ¿Cómo garantizas que un `PERFECT` maze no contiene loops?

6. ¿Cómo garantizas que existen al menos dos rutas independientes en el modo Pac-Man?

7. ¿Cómo controlas los valores inválidos de `WIDTH` y `HEIGHT`?

8. ¿Qué ocurre si `ENTRY` o `EXIT` están fuera del laberinto?

9. ¿Cómo validas el formato `KEY=VALUE` del fichero de configuración?

10. ¿Cómo implementaste el patrón `42`?

11. ¿Qué ocurre cuando el tamaño del laberinto no permite crear el patrón `42`?

12. ¿Cómo evitas una zona abierta de `3x3` o mayor?

13. ¿Cómo funciona la reproducibilidad mediante una seed?

14. ¿Cómo se calcula o genera el shortest path?

15. ¿Cómo compruebas que el shortest path del fichero de salida coincide con el camino visual?

16. ¿Qué información contiene el fichero generado por `OUTPUT_FILE`?

17. ¿Cómo has estructurado el módulo reutilizable del maze generator?

18. ¿Cómo reconstruyes el paquete `mazegen-*.tar.gz` o `.whl`?

19. ¿Puedes instalar el paquete en un virtualenv nuevo y ejecutarlo desde allí?

20. ¿Qué herramientas utilizaste durante el desarrollo?

21. ¿Qué parte del proyecto desarrollaste tú y qué parte desarrolló el otro miembro del equipo?

22. ¿Qué dificultades encontraste y cómo las resolviste?

---

# 📝 10. Final Evaluation

### Checklist

- Repositorio no vacío
- Repositorio correcto
- Trabajo completo
- `README.md`
- `LICENSE.md`
- `a_maze_ing.py`
- `PERFECT=True` correcto
- `PERFECT=False` correcto
- `maze_analyzer.py` correcto
- Paquete `mazegen-*.tar.gz` y/o `.whl`
- Configuración correcta
- `mypy` y `flake8` correcto
- Standard usage correcto
- Menú interactivo correcto
- Configuración validada
- Output correcto
- Seed reproducible
- Maze generator funcional
- Paquete regenerable
- Instalación en entorno limpio correcta
- Bonuses, si procede
- Defense completada
- El alumno puede explicar el código

### 📊 Result

**Rating:** `0 → 5`

**Flags:**

- Ok
- Outstanding project
- Empty work
- Incomplete work
- Norme
- Cheat
- Crash
- Incomplete group
- Concerning situation
- Can't support / explain code
