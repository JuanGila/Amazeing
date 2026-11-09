---
description: Diseñar e implementar los tests de evaluación de A-Maze-Ing
agent: build
---

Utiliza los siguientes documentos como referencia obligatoria:

- `PROJECT_ANALYSIS.md`
- `EVALUATION_MATRIX.md`

Consulta también los documentos originales cuando necesites verificar el origen o el significado exacto de un requisito:

- `docs/project_description.pdf`
- `docs/project_evaluation.md`

## 1. Objetivo

Diseña e implementa toda la estrategia de testing del proyecto A-Maze-Ing.

El objetivo es disponer de una batería de pruebas automatizadas que permita verificar objetivamente que la futura implementación cumple los requisitos del proyecto y todos los criterios verificables de la hoja de evaluación.

## 2. Diseño de los tests

Quiero que:

1. Crees tests automatizados para todos los criterios verificables de la hoja de evaluación.
2. Incluyas tests positivos, negativos y casos límite cuando corresponda.
3. Compruebes tanto los requisitos funcionales como las restricciones técnicas.
4. Identifiques qué criterios no pueden automatizarse y documentes cómo verificarlos manualmente.
5. Mantengas una correspondencia explícita entre cada test y su criterio de evaluación.

## 3. Reglas de testing

- Los tests deben basarse exclusivamente en los requisitos de la documentación.
- No inventes comportamientos esperados ni requisitos adicionales.
- No diseñes tests basados en decisiones arbitrarias de implementación.
- No presupongas nombres de clases, métodos, funciones o módulos que todavía no se hayan definido.
- No acoples los tests a una arquitectura concreta si el requisito puede comprobarse independientemente de ella.
- Cada test debe tener un objetivo claro y un comportamiento esperado justificable documentalmente.
- No utilices mocks para sustituir el comportamiento real cuando sea necesario verificar una funcionalidad completa.
- Evita tests redundantes que comprueben exactamente lo mismo.
- Incluye casos límite que puedan revelar errores en la planificación y simulación de múltiples drones.
- Los tests deben ser reproducibles y deterministas siempre que sea posible.

## 4. Correspondencia con la evaluación

Cada test debe estar relacionado con uno o varios identificadores de `EVALUATION_MATRIX.md`.

Utiliza identificadores únicos para los tests.

Para cada prueba documenta:

- Identificador.
- Criterio de evaluación asociado.
- Requisito que verifica.
- Descripción del escenario.
- Datos de entrada.
- Resultado esperado.
- Tipo de prueba: positiva, negativa o caso límite.

## 5. Criterios que no pueden automatizarse

No fuerces la automatización de criterios que necesiten intervención humana.

Identifica estos criterios y crea una sección específica en la documentación que explique:

- Qué se debe comprobar.
- Por qué no puede automatizarse completamente.
- Cómo realizar la comprobación manual.
- Qué evidencia permitiría considerar el criterio satisfecho.

## 6. Decisiones técnicas y dudas

Antes de implementar los tests, comprueba si dispones de suficiente información para diseñarlos correctamente.

Si necesitas conocer decisiones técnicas que no aparecen en la documentación:

1. Identifica la decisión pendiente.
2. Explica por qué es necesaria.
3. Propón las alternativas razonables.
4. Indica qué tests dependen de esa decisión.
5. Consúltame antes de tomar una decisión que pueda condicionar la arquitectura o el comportamiento del proyecto.

No inventes decisiones para poder continuar.

## 7. Documentos que debes generar

Genera los siguientes documentos:

### TESTING_STRATEGY.md

Debe describir:

- Estrategia general de testing.
- Tipos de pruebas.
- Organización de los tests.
- Relación entre requisitos y pruebas.
- Criterios automatizables.
- Criterios de verificación manual.
- Herramientas y dependencias necesarias.
- Procedimiento para ejecutar toda la batería de pruebas.

### TEST_COVERAGE_MATRIX.md

Debe contener una matriz que relacione:

- ID del criterio de evaluación.
- Requisito asociado.
- IDs de los tests correspondientes.
- Tipo de verificación.
- Estado de cobertura.

No marques un criterio como cubierto si todavía no existe una prueba implementada que lo verifique.

### Implementación de los tests

Crea los archivos de tests automatizados dentro de `tests/`, siguiendo la estrategia definida.

IMPORTANTE: el proyecto todavía no está implementado.

Por tanto:

- Puedes crear la estructura de directorios de tests.
- Puedes implementar tests basados en contratos y comportamientos documentados.
- No implementes clases, funciones ni módulos del proyecto para hacer que los tests pasen.
- No crees implementaciones provisionales dentro de `src/`.
- No modifiques los requisitos para adaptarlos a los tests.

Si un test necesita una interfaz o decisión de diseño todavía no definida, documenta la dependencia en lugar de inventarla.

## 8. Restricciones de esta fase

- No implementes el proyecto.
- No escribas código de producción.
- No modifiques los documentos originales.
- No elimines ni debilites requisitos.
- No alteres los criterios de evaluación.
- No declares que los tests pasan si no pueden ejecutarse por falta de implementación.

## 9. Informe final

Cuando termines:

1. Indica cuántos criterios de evaluación has identificado.
2. Indica cuántos tienen tests automatizados diseñados.
3. Indica cuántos requieren verificación manual.
4. Indica cuántos están pendientes por decisiones técnicas.
5. Resume los tipos de pruebas creados.
6. Indica qué archivos has generado.
7. Explica cómo se ejecutará la batería completa de tests cuando exista la implementación.
8. Señala cualquier duda que necesites resolver conmigo antes de continuar.

No comiences la implementación del proyecto.
