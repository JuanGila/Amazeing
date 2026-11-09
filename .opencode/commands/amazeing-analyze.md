---
description: Analizar la especificación y la hoja de evaluación de A-Maze-Ing
agent: plan
---

Analiza completamente los dos documentos del proyecto:

- `docs/project_description.pdf`
- `docs/project_evaluation.md`

Analiza completamente las herramientas adicionales del proyecto:

- `docs/maze_analyzer.py`
- `docs/mlx-2.2`

## 1. Lectura de la documentación

Lee ambos documentos íntegramente antes de realizar cualquier otra acción.

Si no puedes extraer el contenido del PDF, indícalo y busca una forma alternativa de extraer su texto antes de continuar.

No te limites a leer fragmentos, resúmenes o las primeras páginas. Necesitas comprender la totalidad de ambos documentos.

Utiliza el PDF como fuente principal para determinar los requisitos originales del proyecto. La hoja de evaluación debe utilizarse como referencia adicional para identificar todos los criterios que se evaluarán.

## 2. Análisis del proyecto

Realiza un análisis detallado que incluya:

1. Explica qué proyecto hay que desarrollar y cuál es su objetivo.
2. Extrae todos los requisitos funcionales.
3. Extrae todos los requisitos técnicos y las restricciones de implementación.
4. Analiza individualmente cada criterio de la hoja de evaluación.
5. Identifica todas las funcionalidades, componentes y requisitos necesarios para obtener la máxima puntuación.
6. Identifica posibles ambigüedades, contradicciones y requisitos implícitos entre ambos documentos.
7. Propón una arquitectura y una organización de directorios adecuadas para el proyecto. la cual escribiras en ARCHITECTURE.md.
8. Diseña una estrategia de testing que permita verificar cada criterio de evaluación.

## 3. Reglas de análisis

- No inventes requisitos ni restricciones.
- No omitas ningún requisito funcional o técnico.
- No omitas ningún criterio de evaluación.
- Diferencia claramente los requisitos del PDF de los criterios adicionales de la hoja de evaluación.
- Cuando encuentres contradicciones, documenta ambas interpretaciones y señala cuál debe prevalecer o qué decisión necesita confirmación.
- No confundas una propuesta de implementación con un requisito obligatorio.
- No des por cumplido ningún criterio sin disponer de evidencia documental.
- Relaciona cada requisito evaluable con una forma concreta de comprobarlo.
- Si algún criterio no puede verificarse mediante tests automatizados, propón un procedimiento de verificación manual.

## 4. Documentos que debes generar

Genera los siguientes documentos en la raíz del proyecto:

### PROJECT_ANALYSIS.md

Debe contener el análisis completo de la especificación:

- Descripción y objetivos del proyecto.
- Requisitos funcionales.
- Requisitos técnicos.
- Restricciones y prohibiciones.
- Comportamientos esperados.
- Reglas de funcionamiento.
- Ambigüedades y contradicciones.
- Requisitos adicionales de evaluación.
- Arquitectura propuesta.
- Organización de directorios.
- Estrategia general de testing.

### EVALUATION_MATRIX.md

Debe contener una matriz de trazabilidad que relacione todos los criterios de evaluación con los requisitos del proyecto.

Incluye, como mínimo, las siguientes columnas:

| ID | Criterio de evaluación | Origen | Prioridad | Implementación prevista | Verificación / Test |
|---|---|---|---|---|---|

Cada criterio de evaluación debe disponer de:

- Un identificador único.
- Su descripción.
- Su procedencia (PDF o evaluación).
- Su prioridad.
- La funcionalidad o componente que debe implementarse.
- Una propuesta concreta de test o procedimiento de verificación.

No agrupes criterios independientes si eso provoca que alguno quede sin identificar o verificar.

## 5. Restricciones de esta fase

IMPORTANTE:

- No escribas código.
- No implementes funcionalidades.
- No crees tests todavía.
- No modifiques los documentos originales.
- No instales dependencias.
- No tomes decisiones irreversibles sobre la arquitectura.

En esta fase únicamente debes analizar la documentación y generar los dos documentos solicitados.

## 6. Informe final

Cuando hayas terminado:

1. Confirma que has leído íntegramente ambos documentos.
2. Indica si has podido extraer correctamente todo el contenido del PDF.
3. Resume los principales requisitos identificados.
4. Indica cuántos criterios de evaluación has identificado.
5. Señala las contradicciones o ambigüedades encontradas.
6. Confirma que has generado `PROJECT_ANALYSIS.md`, `ARCHITECTURE.md` y `EVALUATION_MATRIX.md`.
7. Indica cualquier información que necesites que te aclare antes de continuar con el desarrollo.
