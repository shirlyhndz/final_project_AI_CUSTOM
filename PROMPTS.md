# Registro cronológico de uso de IA

## Prompt 01 - Análisis inicial del monolito

**Objetivo del prompt:**  
Analizar la estructura del proyecto base antes de modificarlo, identificando frontend, backend, RAG, endpoints existentes y puntos pendientes para integrar CAG.

**Prompt usado:**  
Analiza este proyecto monolítico base con frontend, backend y recuperación tipo RAG. Identifica sus capas principales, cómo fluye una pregunta desde el frontend hasta el backend, qué componentes ya existen para CAG, qué partes están incompletas y dónde sería más mantenible integrar contexto persistente sin romper la arquitectura existente.

**Resumen de la respuesta recibida:**  
Se identificó que el frontend ya consume los endpoints `/api/ask` y `/api/context`. El backend ya expone dichos endpoints, pero `context_store.py` lanza `NotImplementedError`, `cag.py` no aplica contexto y `assistant.py` solo usa RAG mediante `retrieve_snippets`. La base documental se encuentra en `data/knowledge_base.json`.

**Decisión humana tomada:**  
Se decidió no reemplazar el RAG existente. La solución se integrará como una capa CAG complementaria, usando almacenamiento de contexto por usuario y aplicándolo en el flujo de respuesta del asistente.

**Cambios realizados en el proyecto:**  
Se creó el registro inicial de uso de IA en `PROMPTS.md` y se documentó el análisis previo antes de modificar código fuente.

**Verificación aplicada:**  
Se ejecutaron las pruebas base con `python -m unittest discover -s tests/base -p "test_*.py"` y pasaron correctamente. También se revisaron manualmente los archivos `server.py`, `assistant.py`, `knowledge.py`, `context_store.py`, `cag.py`, `frontend/index.html`, `frontend/app.js` y `data/knowledge_base.json`.

## Prompt 02 - Planificación Scrum del proyecto

**Objetivo del prompt:**
Organizar el trabajo del proyecto usando metodología Scrum, con backlog y cuatro sprints incrementales.

**Prompt usado:**
Con base en el enunciado del examen y el análisis del monolito, ayúdame a estructurar una documentación Scrum con backlog, Sprint 1 de análisis, Sprint 2 de diseño CAG, Sprint 3 de implementación CAG y Sprint 4 de validación final, evidencias y entrega.

**Resumen de la respuesta recibida:**
La IA propuso una planificación Scrum organizada en cuatro sprints: análisis inicial, diseño técnico, implementación CAG y validación final. También sugirió incluir backlog, tareas priorizadas, cierre de sprint y entregables esperados.

**Decisión humana tomada:**
Se decidió trabajar con cuatro sprints para mostrar un proceso incremental más claro: análisis, diseño, implementación y validación final.

**Cambios realizados en el proyecto:**
Se creó el archivo `docs/SCRUM.md` con backlog, planificación de cuatro sprints, ejecución y cierre.

**Verificación aplicada:**
Se revisó que la documentación Scrum incluya las tareas obligatorias del enunciado: CAG, pruebas, documentación, evidencias, commits incrementales y Pull Request.

## Prompt 03 - Diseño técnico SDD para integración CAG

**Objetivo del prompt:**  
Documentar el diseño técnico para integrar CAG dentro del monolito sin reemplazar el RAG existente.

**Prompt usado:**  
Con base en el análisis del monolito, ayúdame a crear un SDD que explique el estado inicial, problema detectado, solución propuesta, flujo de integración CAG, componentes modificados y validación esperada.

**Resumen de la respuesta recibida:**  
La IA propuso un documento SDD con propósito, estado inicial, problema, solución CAG, flujo propuesto, decisión arquitectónica, componentes a modificar y criterios de validación.

**Decisión:**  
Se decidió mantener RAG como base documental y agregar CAG como capa complementaria de contexto persistente.

**Cambios realizados en el proyecto:**  
Se creó `docs/SDD.md`.

**Verificación aplicada:**  
Se ejecutaron nuevamente las pruebas base y pasaron correctamente.