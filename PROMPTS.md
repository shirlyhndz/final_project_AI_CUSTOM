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

## Prompt 04 - Corrección de integración CAG por validación

**Objetivo del prompt:**  
Corregir la integración del módulo CAG después de ejecutar pruebas de validación.

**Prompt usado:**  
La prueba `test_ask_uses_context_to_influence_later_response` sigue fallando. El contexto se guarda correctamente con `/api/context`, pero `/api/ask` no está usando ese contexto en la respuesta. Analiza la causa sin rehacer todo el proyecto.

**Resumen de la respuesta recibida:**  
La IA identificó que `server.py` y `assistant.py` estaban usando instancias diferentes de `ContextStore`, por lo que el contexto guardado no llegaba al flujo de respuesta.

**Decisión tomada:**  
Se verificó manualmente el fallo mediante pruebas y se decidió corregir la arquitectura pasando `context_items` desde `server.py` hacia `answer_question`, en lugar de crear otra memoria dentro de `assistant.py`.

**Cambios realizados en el proyecto:**  
Se modificó `assistant.py` para recibir `context_items` como parámetro. También se modificó `server.py` para recuperar el contexto del usuario y enviarlo al asistente. Además, `cag.py` fue actualizado para aplicar el contexto sobre la respuesta base.

**Verificación aplicada:**  
Se ejecutó `python -m unittest tests.validation.test_cag_contract`. La primera validación falló, evidenciando el problema de integración. Después de la corrección, las tres pruebas CAG pasaron correctamente.

## Prompt 05 - Escenarios BDD para validación CAG

**Objetivo del prompt:**
Documentar escenarios BDD para validar el comportamiento esperado del módulo CAG.

**Prompt usado:**
Con base en el módulo CAG implementado, ayúdame a crear escenarios BDD en formato Given-When-Then para guardar contexto, recuperar contexto, usar contexto en respuestas posteriores y responder sin contexto previo.

**Resumen de la respuesta recibida:**
La IA propuso escenarios BDD enfocados en el comportamiento observable del sistema: guardar contexto, recuperarlo, aplicarlo en `/api/ask` y responder correctamente cuando no exista contexto.

**Decisión tomada:**
Se decidió documentar los escenarios en `docs/BDD.md` porque representan los comportamientos principales exigidos por el contrato de validación CAG.

**Cambios realizados en el proyecto:**
Se creó el archivo `docs/BDD.md`.

**Verificación aplicada:**
Se compararon los escenarios BDD contra las pruebas de `tests/validation/test_cag_contract.py` y la validación final ya ejecutada.


git add PROMPTS.md tests/student/test_cag_unit.py docs/evidencias/05_pruebas_propias_ok.png
git commit -m "Sprint 4: agregar pruebas propias CAG"