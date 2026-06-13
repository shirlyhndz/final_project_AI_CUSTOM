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