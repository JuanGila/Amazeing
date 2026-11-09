---
description: Auditar A-Maze-Ing frente a la especificación oficial y la hoja de evaluación
agent: build
---

Quiero que realices una auditoría completa del proyecto A-Maze-Ing utilizando como referencias originales y obligatorias:

- `docs/project_description.pdf`
- `docs/project_evaluation.md`

Utiliza también los siguientes documentos como referencias auxiliares:

- `PROJECT_ANALYSIS.md`
- `EVALUATION_MATRIX.md`
- `ARCHITECTURE.md`

La especificación PDF y la hoja de evaluación originales tienen prioridad sobre cualquier interpretación realizada durante las fases anteriores.

## 1. Objetivo de la auditoría

Actúa como un evaluador independiente, crítico y riguroso.

Tu objetivo no es demostrar que el proyecto funciona, sino determinar objetivamente si la implementación cumple todos los requisitos y criterios de evaluación.

No confíes en las conclusiones de las fases anteriores. Comprueba cada requisito directamente contra la documentación original y la implementación real.

## 2. Ejecución de pruebas

1. Ejecuta todos los tests automatizados existentes.
2. Ejecuta las pruebas de integración.
3. Ejecuta las comprobaciones técnicas obligatorias del proyecto.
4. Comprueba los resultados de mypy, flake8 y las demás herramientas exigidas.
5. Comprueba que los tests se ejecutan correctamente y que sus resultados son reproducibles.
6. Identifica tests que no se ejecutan, están incompletos o no verifican realmente lo que indican.

No des por superado ningún test basándote únicamente en resultados anteriores.

## 3. Auditoría de los criterios de evaluación

Comprueba individualmente todos los criterios de `EVALUATION_MATRIX.md`.

Para cada criterio:

1. Localiza el requisito correspondiente en la documentación original.
2. Identifica los componentes responsables de satisfacerlo.
3. Inspecciona la implementación real.
4. Identifica los tests relacionados.
5. Ejecuta las pruebas correspondientes.
6. Comprueba que los tests verifican realmente el comportamiento exigido.
7. Determina si existe evidencia suficiente para considerar satisfecho el criterio.

Presta especial atención a los criterios que puedan haber quedado implementados parcialmente.

No agrupes criterios independientes ni omitas ninguno.

## 4. Detección de errores y deficiencias

Busca activamente:

- Funcionalidades incompletas.
- Comportamientos contrarios a la especificación.
- Errores de lógica.
- Casos límite no contemplados.
- Problemas de integración.
- Errores en la gestión de múltiples drones.
- Conflictos de movimiento.
- Incumplimientos de capacidades de zonas y conexiones.
- Errores en movimientos que requieren dos turnos.
- Problemas en la búsqueda y optimización de rutas.
- Errores de parsing.
- Problemas en la visualización.
- Restricciones técnicas incumplidas.
- Dependencias prohibidas.
- Problemas de tipado y calidad del código.
- Funcionalidades que existen pero no están correctamente verificadas.

No te limites a comprobar que los archivos y las clases existen. Comprueba el comportamiento real del sistema.

## 5. Auditoría de calidad de los tests

Comprueba específicamente que no existen falsos positivos.

Investiga si:

- Los tests tienen aserciones suficientes.
- Los resultados esperados están justificados por la documentación.
- Los tests comprueban el comportamiento real y no detalles triviales de implementación.
- Los tests detectan correctamente entradas inválidas.
- Los casos límite están suficientemente cubiertos.
- Existen tests que siempre pasan independientemente de la implementación.
- Existen mocks que ocultan errores reales.
- Los tests están acoplados a la implementación hasta el punto de no detectar incumplimientos funcionales.

Cuando sea posible, utiliza casos de prueba independientes o introduce temporalmente escenarios incorrectos en un entorno controlado para comprobar que las pruebas detectan los fallos.

No modifiques permanentemente los tests originales durante esta auditoría.

## 6. Clasificación de resultados

Cada criterio debe recibir exactamente uno de estos resultados:

- `PASS`: existe evidencia suficiente de que el requisito se cumple.
- `FAIL`: se ha identificado un incumplimiento o un error.
- `NOT VERIFIED`: no existe evidencia suficiente para confirmar su cumplimiento.

IMPORTANTE:

- Que exista código no implica PASS.
- Que un test pase no implica automáticamente PASS.
- Un criterio sin pruebas suficientes debe clasificarse como NOT VERIFIED.
- Un criterio parcialmente implementado debe clasificarse como FAIL si incumple algún requisito obligatorio.
- No ocultes problemas ni suavices los resultados.

## 7. Documento de auditoría

Genera `FINAL_EVALUATION.md` en la raíz del proyecto.

Debe contener las siguientes secciones:

### 7.1. Resumen ejecutivo

- Estado general del proyecto.
- Número total de criterios evaluados.
- Número de criterios PASS.
- Número de criterios FAIL.
- Número de criterios NOT VERIFIED.
- Resultado global de la auditoría.

### 7.2. Matriz de evaluación

Incluye una tabla con las siguientes columnas:

| ID | Criterio de evaluación | Resultado | Evidencia encontrada | Tests relacionados | Problemas detectados | Posibles mejoras |
|---|---|---|---|---|---|---|

Incluye todos los criterios sin excepción.

### 7.3. Resultados de testing

Documenta:

- Tests ejecutados.
- Tests superados.
- Tests fallidos.
- Tests no ejecutados.
- Errores encontrados.
- Posibles falsos positivos.
- Cobertura de criterios de evaluación.

### 7.4. Incumplimientos técnicos

Documenta los incumplimientos de las restricciones y requisitos técnicos del proyecto.

### 7.5. Problemas críticos

Identifica los errores que podrían provocar una pérdida importante de puntuación o impedir la aprobación del proyecto.

Clasifícalos por gravedad y explica su impacto.

### 7.6. Mejoras recomendadas

Propón las correcciones necesarias, ordenadas por prioridad.

Distingue entre:

- Correcciones obligatorias.
- Correcciones recomendables.
- Mejoras opcionales.

### 7.7. Verificaciones manuales pendientes

Identifica los criterios que requieren intervención humana y explica cómo verificarlos.

## 8. Restricciones de la auditoría

- No modifiques los tests para conseguir resultados positivos.
- No elimines pruebas fallidas.
- No debilites las aserciones.
- No modifiques los documentos originales.
- No alteres la especificación para justificar la implementación.
- No ocultes errores.
- No marques criterios como PASS sin evidencia.
- No implementes correcciones durante la auditoría.
- No cambies el comportamiento del proyecto para conseguir una evaluación favorable.

Si detectas un problema, documenta el problema y su posible solución, pero no lo corrijas.

## 9. Informe final

Cuando termines:

1. Confirma que has consultado la documentación original.
2. Indica cuántos criterios has evaluado.
3. Presenta el número de PASS, FAIL y NOT VERIFIED.
4. Resume los errores más importantes.
5. Identifica los posibles falsos positivos de los tests.
6. Indica las restricciones técnicas incumplidas.
7. Confirma que has generado `FINAL_EVALUATION.md`.
8. Explica qué debería corregirse antes de considerar A-Maze-Ing terminado.

## 10. Condición de aprobación

No declares el proyecto aprobado si existe al menos un criterio obligatorio con resultado FAIL o NOT VERIFIED.

El resultado debe reflejar fielmente el estado real del proyecto, aunque sea desfavorable.

Tu función es evaluar, no justificar las decisiones de implementación.


## Independencia de la auditoría

FINAL_EVALUATION.md es un documento independiente de EVALUATION_MATRIX.md.

Reglas obligatorias:

1. Utiliza EVALUATION_MATRIX.md únicamente como referencia de planificación y seguimiento.
2. No copies automáticamente sus estados a FINAL_EVALUATION.md.
3. Comprueba cada criterio directamente contra:
   - La especificación oficial del proyecto.
   - El código realmente implementado.
   - Las pruebas ejecutadas.
   - Las evidencias obtenidas durante la auditoría.
4. Determina de forma independiente el resultado de cada criterio.
5. Utiliza exclusivamente estos estados:
   - PASS: cumplimiento demostrado mediante evidencias.
   - FAIL: incumplimiento demostrado.
   - NOT VERIFIED: no existe evidencia suficiente para confirmar el cumplimiento.
6. Si EVALUATION_MATRIX.md indica IMPLEMENTED pero las pruebas no demuestran el cumplimiento, no marques PASS automáticamente.
7. No modifiques EVALUATION_MATRIX.md para hacer coincidir sus estados con los resultados de la auditoría.
8. No modifiques FINAL_EVALUATION.md durante el desarrollo.

FINAL_EVALUATION.md debe reflejar exclusivamente lo que se ha podido demostrar durante esta auditoría, no lo que se esperaba implementar.
