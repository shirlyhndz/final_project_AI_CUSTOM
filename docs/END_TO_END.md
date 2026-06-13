# Flujo End-to-End

## Objetivo

Documentar cómo fluye una solicitud desde el frontend hasta el backend, integrando RAG y CAG para generar una respuesta con conocimiento documental y contexto persistente.

## Flujo completo

1. El usuario ingresa su `user_id` y una pregunta en el frontend.
2. El frontend envía la pregunta a `POST /api/ask`.
3. El backend recibe `user_id` y `question`.
4. El backend recupera contexto del usuario usando `ContextStore`.
5. El backend consulta la base documental mediante RAG usando `retrieve_snippets`.
6. El asistente construye una respuesta base con la información recuperada.
7. El módulo CAG aplica el contexto guardado sobre la respuesta.
8. El backend devuelve:

   * `user_id`
   * `answer`
   * `sources`
   * `context_used`
9. El frontend muestra la respuesta.
10. El frontend consulta `GET /api/context?user_id=...` para mostrar el contexto guardado.

## Endpoints involucrados

| Endpoint                   | Método | Función                           |
| -------------------------- | ------ | --------------------------------- |
| `/api/context`             | POST   | Guarda contexto por usuario       |
| `/api/context?user_id=...` | GET    | Recupera contexto guardado        |
| `/api/ask`                 | POST   | Genera respuesta usando RAG + CAG |

## Ejemplo de uso

Primero se guarda contexto:

```json
{
  "user_id": "luis",
  "key": "audience",
  "value": "explicar como principiante"
}
```

Luego el usuario pregunta:

```json
{
  "user_id": "luis",
  "question": "Que es CAG?"
}
```

El sistema responde usando la base documental y además aplica el contexto guardado, indicando que la explicación debe adaptarse a un principiante.

## Resultado esperado

La respuesta final debe incluir información recuperada por RAG y evidencia de que el contexto fue usado mediante el campo `context_used`.

Ejemplo:

```json
{
  "user_id": "luis",
  "answer": "Segun la base de conocimiento del curso...",
  "sources": ["cag"],
  "context_used": ["audience"]
}
```
