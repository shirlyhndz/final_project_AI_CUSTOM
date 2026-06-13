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

## Prompt 06 - Pruebas propias para el módulo CAG

**Objetivo del prompt:**
Crear pruebas propias para validar el comportamiento interno del módulo CAG y no depender únicamente de las pruebas base del proyecto.

**Prompt usado:**
Con base en la implementación del módulo CAG, ayúdame a crear pruebas unitarias propias para validar almacenamiento de contexto, actualización de claves existentes y aplicación del contexto en una respuesta.

**Resumen de la respuesta recibida:**
La IA propuso pruebas unitarias para `ContextStore` y `apply_context`, validando que el contexto pueda guardarse, recuperarse, actualizarse y aplicarse sobre una respuesta base.

**Decisión humana tomada:**
Se decidió agregar una carpeta `tests/student/` para separar las pruebas propias de las pruebas base y de validación entregadas por el proyecto.

**Cambios realizados en el proyecto:**
Se creó el archivo `tests/student/test_cag_unit.py` con tres pruebas unitarias propias.

**Verificación aplicada:**
Se ejecutó el comando `$env:PYTHONPATH="."; python -m unittest discover -s tests/student -p "test_*.py"` y las tres pruebas pasaron correctamente.

## Prompt 07 - Documentación TDD y pruebas propias

**Objetivo del prompt:**
Documentar la aplicación de TDD y las pruebas propias agregadas para validar CAG.

**Prompt usado:**
Con base en las pruebas ejecutadas y el módulo CAG implementado, ayúdame a crear una documentación TDD que explique pruebas base, prueba fallida inicial, corrección aplicada, pruebas propias y validación final.

**Resumen de la respuesta recibida:**
La IA propuso documentar el proceso TDD mostrando que primero se ejecutaron pruebas, luego se detectó el fallo de integración CAG, se corrigió el flujo y finalmente se agregaron pruebas propias.

**Decisión humana tomada:**
Se decidió documentar el fallo inicial y la corrección porque demuestra verificación real y no aceptación automática de la solución generada por IA.

**Cambios realizados en el proyecto:**
Se creó `docs/TDD.md`.

**Verificación aplicada:**
Se validaron pruebas base, pruebas CAG de contrato y pruebas propias con resultado OK.


## Prompt 08 - Documentación del flujo End-to-End

**Objetivo del prompt:**  
Documentar el flujo completo de la aplicación desde el frontend hasta el backend, incluyendo RAG y CAG.

**Prompt usado:**  
Con base en la implementación actual, ayúdame a documentar el flujo end-to-end del sistema, explicando cómo una pregunta pasa del frontend al backend, cómo se recupera contexto, cómo se consulta RAG y cómo CAG modifica la respuesta final.

**Resumen de la respuesta recibida:**  
La IA propuso documentar el flujo completo desde la entrada del usuario, consumo de endpoints, recuperación de contexto, recuperación documental RAG, aplicación CAG y respuesta final.

**Decisión humana tomada:**  
Se decidió crear un documento separado para facilitar la revisión técnica del flujo completo del sistema.

**Cambios realizados en el proyecto:**  
Se creó `docs/END_TO_END.md`.

**Verificación aplicada:**  
Se comparó el flujo documentado contra los archivos `frontend/app.js`, `backend/server.py`, `backend/assistant.py`, `backend/knowledge.py`, `backend/context_store.py` y `backend/cag.py`.


## Prompt 09 - Actualización del README final

**Objetivo del prompt:**  
Actualizar el README final del repositorio para explicar claramente la solución implementada.

**Prompt usado:**  
Con base en el proyecto final con CAG implementado, documentación Scrum, SDD, BDD, TDD, flujo end-to-end, pruebas y evidencias, ayúdame a estructurar un README técnico final para entregar el repositorio.

**Resumen de la respuesta recibida:**  
La IA propuso un README con descripción del proyecto, arquitectura, módulos RAG y CAG, endpoints, comandos de ejecución, pruebas realizadas, documentación incluida, evidencias, uso de IA, sprints y alcance logrado.

**Decisión tomada:**  
Se decidió reemplazar el README base por una versión final enfocada en explicar la solución implementada y facilitar la revisión del ingeniero.

**Cambios realizados en el proyecto:**  
Se actualizó `README.md`.

**Verificación aplicada:**  
Se revisó que el README incluya arquitectura, pruebas, documentación, evidencias, uso de IA y alcance final.