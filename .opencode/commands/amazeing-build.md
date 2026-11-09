---
description: Implementar A-Maze-Ing siguiendo los requisitos y criterios de evaluación
agent: build
---

Ahora implementa el proyecto A-Maze-Ing siguiendo estrictamente los siguientes documentos:

- `docs/project_description.pdf`
- `docs/project_evaluation.md`
- `PROJECT_ANALYSIS.md`
- `EVALUATION_MATRIX.md`

Consulta también, cuando corresponda:

- `ARCHITECTURE.md`
- `TESTING_STRATEGY.md`
- `TEST_COVERAGE_MATRIX.md`

Estos documentos constituyen las referencias obligatorias para el desarrollo.

## 1. Objetivo

Implementa el proyecto completo siguiendo la especificación oficial y los criterios de evaluación.

Sigue la arquitectura propuesta y desarrolla el proyecto incrementalmente, asegurándote de que cada componente cumple su responsabilidad y respeta las restricciones documentadas.

## 2. Reglas de implementación

1. Implementa todos los requisitos de la especificación.
2. Prioriza los criterios de evaluación de mayor importancia.
3. Respeta todas las restricciones técnicas del PDF.
4. No elimines ni debilites los tests existentes.
5. Después de implementar cada componente, ejecuta los tests correspondientes.
6. Corrige los errores antes de continuar.
7. No marques ninguna funcionalidad como terminada sin haberla verificado.

## 3. Metodología de desarrollo

Trabaja de forma incremental siguiendo estas fases:

### Fase 1: Revisión previa

Antes de escribir código:

- Lee los documentos de referencia.
- Comprueba el estado actual del proyecto.
- Revisa la arquitectura propuesta.
- Examina los tests existentes.
- Identifica dependencias entre componentes.
- Identifica decisiones técnicas pendientes.

No presupongas que la arquitectura o los tests son correctos si contradicen los requisitos originales.

### Fase 2: Preparación de la estructura

Prepara la estructura de directorios y los archivos necesarios siguiendo `ARCHITECTURE.md`.

Respeta la separación de responsabilidades y evita introducir dependencias innecesarias.

### Fase 3: Implementación incremental

Implementa el proyecto por componentes.

Para cada componente:

1. Explica brevemente qué responsabilidad tiene.
2. Identifica los requisitos que debe satisfacer.
3. Implementa su funcionalidad.
4. Ejecuta los tests relacionados.
5. Analiza los resultados.
6. Corrige los errores encontrados.
7. Comprueba que no has introducido regresiones.
8. Actualiza la matriz de evaluación.

No avances al siguiente componente mientras existan errores que comprometan los requisitos del componente actual.

### Fase 4: Integración

Cuando los componentes individuales estén implementados:

- Integra los diferentes módulos.
- Comprueba sus interacciones.
- Ejecuta los tests de integración.
- Verifica el comportamiento completo del sistema.
- Comprueba los casos límite y las situaciones de error.

Presta especial atención a los componentes que interactúan entre sí y a las reglas que afectan simultáneamente a varios drones.

### Fase 5: Validación técnica

Comprueba todos los requisitos técnicos y restricciones documentados.

Ejecuta las herramientas de validación exigidas por el proyecto, incluyendo cuando corresponda:

- pytest.
- mypy.
- flake8.
- Makefile.
- Cualquier otra herramienta obligatoria indicada en la documentación.

No declares que una comprobación ha sido superada si no has ejecutado realmente la herramienta correspondiente.

## 4. Reglas de calidad

Durante toda la implementación:

- Mantén una arquitectura orientada a objetos coherente.
- Respeta los principios de responsabilidad única.
- Utiliza type hints adecuados.
- Sigue las convenciones de Python.
- Escribe docstrings conforme a PEP 257 cuando sean necesarios.
- Evita duplicación de código.
- Evita complejidad innecesaria.
- No introduzcas librerías prohibidas por la especificación.
- No modifiques los tests para ocultar errores de implementación.
- No reduzcas la cobertura de pruebas para conseguir resultados positivos.
- No implementes funcionalidades que contradigan el comportamiento especificado.

Prioriza siempre la corrección funcional y el cumplimiento de los requisitos frente a la rapidez de implementación.

## 5. Gestión de la matriz de evaluación

Actualiza `EVALUATION_MATRIX.md` durante todo el desarrollo.

Cada criterio debe reflejar uno de estos estados:

- `NOT STARTED`: todavía no implementado.
- `IN PROGRESS`: implementación iniciada, pero incompleta.
- `IMPLEMENTED`: implementación realizada, pero todavía no verificada.
- `VERIFIED`: implementación comprobada satisfactoriamente mediante tests o evidencia válida.
- `FAILED`: existen errores o incumplimientos.
- `NOT VERIFIED`: no se dispone de evidencia suficiente para verificarlo.

Para cada criterio actualiza:

- Estado.
- Componentes relacionados.
- Tests ejecutados.
- Resultado de los tests.
- Evidencia de cumplimiento.
- Problemas pendientes.

IMPORTANTE:

La implementación de una funcionalidad no implica que el criterio esté verificado.

Solo utiliza `VERIFIED` cuando exista evidencia suficiente de que el requisito se cumple.

## 6. Gestión de contradicciones y decisiones pendientes

Si encuentras contradicciones entre:

- El PDF oficial.
- La hoja de evaluación.
- PROJECT_ANALYSIS.md.
- EVALUATION_MATRIX.md.
- ARCHITECTURE.md.
- TESTING_STRATEGY.md.

No tomes decisiones arbitrarias.

En su lugar:

1. Identifica el conflicto.
2. Indica los documentos y requisitos afectados.
3. Explica las posibles interpretaciones.
4. Analiza las consecuencias de cada alternativa.
5. Propón una solución.
6. Consúltame antes de continuar si la decisión puede afectar a la evaluación o al comportamiento del proyecto.

No sacrifiques un requisito obligatorio para satisfacer un criterio adicional sin haber identificado y resuelto explícitamente el conflicto.

## 7. Restricciones

- No elimines requisitos.
- No modifiques los documentos originales.
- No elimines ni debilites tests.
- No ocultes errores.
- No declares funcionalidades verificadas sin evidencia.
- No introduzcas dependencias prohibidas.
- No sustituyas algoritmos exigidos por soluciones externas no permitidas.
- No avances sobre decisiones críticas pendientes de confirmación.

## 8. Informe de progreso

Al terminar cada componente, proporciona un resumen con:

- Componente implementado.
- Requisitos satisfechos.
- Tests ejecutados.
- Tests superados.
- Tests fallidos.
- Problemas encontrados.
- Estado de los criterios de evaluación relacionados.

Mantén el trabajo organizado y documentado para que pueda entender qué estás implementando y por qué.

## 9. Finalización

Cuando hayas terminado la implementación:

1. Ejecuta toda la batería de tests.
2. Ejecuta todas las comprobaciones técnicas obligatorias.
3. Comprueba todos los criterios de evaluación.
4. Identifica los criterios pendientes o fallidos.
5. Actualiza `EVALUATION_MATRIX.md`.
6. Genera un resumen del estado final del proyecto.

No declares A-Maze-Ing terminado si existen requisitos obligatorios incumplidos o criterios sin verificar.

Si encuentras contradicciones o decisiones que puedan afectar a la evaluación, consúltamelas antes de continuar.

## Separación entre seguimiento y auditoría

Existen dos documentos con responsabilidades independientes:

### EVALUATION_MATRIX.md
- Es el documento de seguimiento del desarrollo.
- Registra los criterios de evaluación y su estado de implementación.
- Puede actualizarse durante el desarrollo.
- Sus estados representan el progreso, no una certificación definitiva.
- Nunca debe utilizarse como prueba de que un criterio está superado.

### FINAL_EVALUATION.md
- Es el documento de resultados de la auditoría final.
- Solo debe generarse o actualizarse mediante `/flyin-audit`.
- No debes modificarlo durante la implementación.
- No debes anticipar resultados ni marcar criterios como PASS.
- La implementación de una funcionalidad no demuestra por sí sola que cumple el criterio.

IMPORTANTE:
Nunca mezcles los resultados de ambos documentos.
El estado IMPLEMENTED en EVALUATION_MATRIX.md no implica PASS en FINAL_EVALUATION.md.
