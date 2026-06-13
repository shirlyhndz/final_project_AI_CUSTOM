# SDD - Software Design Document

## 1. Propósito

Este documento describe el diseño técnico para integrar un módulo CAG (Context-Augmented Generation) dentro del proyecto monolítico base. El objetivo es mantener la arquitectura existente con frontend, backend y RAG, agregando una capa de contexto persistente sin reemplazar la recuperación documental actual.

## 2. Estado inicial del sistema

El sistema base contiene:

- `frontend/`: interfaz web estática para enviar preguntas y visualizar respuestas.
- `backend/server.py`: servidor HTTP con endpoints `/api/ask` y `/api/context`.
- `backend/assistant.py`: lógica principal del asistente.
- `backend/knowledge.py`: recuperación documental tipo RAG desde `data/knowledge_base.json`.
- `backend/context_store.py`: componente pendiente para almacenar y recuperar contexto.
- `backend/cag.py`: componente pendiente para aplicar contexto a las respuestas.

## 3. Problema detectado

El sistema puede responder usando RAG, pero no conserva contexto persistente por usuario. Esto provoca que cada pregunta sea tratada de forma aislada y que el sistema no pueda usar preferencias, historial o decisiones previas.

## 4. Solución propuesta

Se implementará una capa CAG compuesta por:

- `ContextStore`: almacena y recupera contexto asociado a un `user_id`.
- `apply_context`: toma la respuesta base del RAG y la enriquece con el contexto disponible.
- Integración en `answer_question`: combina pregunta actual, documentos recuperados y contexto persistente.

## 5. Flujo propuesto

1. El usuario escribe una pregunta en el frontend.
2. El frontend envía la solicitud a `POST /api/ask`.
3. El backend recupera fragmentos relevantes desde RAG.
4. El backend recupera contexto del usuario desde `ContextStore`.
5. CAG aplica el contexto sobre la respuesta base.
6. El backend devuelve respuesta, fuentes y contexto usado.
7. El frontend muestra la respuesta y consulta `/api/context`.

## 6. Decisión arquitectónica

Se decidió no reemplazar el RAG existente. CAG se integra como capa complementaria para mejorar la respuesta con memoria contextual. Esta decisión mantiene el monolito simple, pero con responsabilidades separadas.

## 7. Componentes modificados

| Archivo | Responsabilidad |
|---|---|
| `backend/context_store.py` | Guardar y recuperar contexto por usuario |
| `backend/cag.py` | Aplicar contexto a la respuesta |
| `backend/assistant.py` | Integrar RAG + CAG |
| `tests/` | Validar comportamiento del módulo CAG |

## 8. Validación esperada

La solución debe permitir:

- Guardar contexto con `POST /api/context`.
- Recuperar contexto con `GET /api/context?user_id=...`.
- Usar contexto en respuestas posteriores de `POST /api/ask`.
- Mantener las pruebas base funcionando.
- Pasar las pruebas de validación final.