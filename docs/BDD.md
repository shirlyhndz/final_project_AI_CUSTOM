# BDD - Escenarios de comportamiento

## Feature: Gestión de contexto CAG

El sistema debe permitir guardar, recuperar y utilizar contexto persistente por usuario para mejorar respuestas posteriores.

### Scenario 1: Guardar contexto de un usuario

**Given** que el usuario envía un contexto con `user_id`, `key` y `value`
**When** realiza una solicitud `POST /api/context`
**Then** el sistema debe guardar el contexto
**And** debe responder con estado `201`
**And** debe indicar que el contexto fue guardado correctamente.

### Scenario 2: Recuperar contexto guardado

**Given** que existe contexto guardado para un usuario
**When** se realiza una solicitud `GET /api/context?user_id=...`
**Then** el sistema debe devolver el contexto asociado a ese usuario
**And** debe incluir las claves y valores previamente almacenados.

### Scenario 3: Usar contexto en una respuesta posterior

**Given** que el usuario tiene contexto guardado con una preferencia de audiencia
**And** el contexto indica que se debe explicar como principiante
**When** el usuario realiza una pregunta mediante `POST /api/ask`
**Then** el sistema debe generar una respuesta usando RAG
**And** debe aplicar el contexto CAG guardado
**And** la respuesta debe reflejar la preferencia del usuario.

### Scenario 4: Responder sin contexto previo

**Given** que un usuario no tiene contexto guardado
**When** realiza una pregunta mediante `POST /api/ask`
**Then** el sistema debe responder usando la base documental RAG
**And** debe devolver `context_used` vacío
**And** no debe fallar por falta de contexto.

## Relación con las pruebas

Los escenarios anteriores se validan principalmente con:

* `tests/base/`
* `tests/validation/test_cag_contract.py`

La validación final confirmó que las pruebas base y las pruebas CAG pasan correctamente.
