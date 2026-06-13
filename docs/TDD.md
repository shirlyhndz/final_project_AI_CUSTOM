# TDD - Pruebas y validación

## 1. Objetivo

Documentar cómo se aplicó TDD durante la integración del módulo CAG, usando pruebas para guiar la implementación y validar que el sistema cumpliera el comportamiento esperado.

## 2. Pruebas base ejecutadas antes de modificar

Antes de modificar el código fuente se ejecutaron las pruebas base del proyecto:

```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py"
```

Resultado esperado:

```text
Ran 3 tests
OK
```

Esto permitió confirmar que el monolito inicial funcionaba antes de integrar CAG.

## 3. Pruebas de contrato CAG

Se ejecutó la prueba de validación:

```powershell
$env:PYTHONPATH="."; python -m unittest tests.validation.test_cag_contract
```

Inicialmente falló una prueba porque `/api/ask` no usaba el contexto guardado. Esto permitió identificar que el contexto se guardaba correctamente, pero no llegaba al flujo de respuesta del asistente.

## 4. Corrección aplicada

Se corrigió la integración haciendo que:

* `server.py` recupere el contexto del usuario desde `ContextStore`.
* `assistant.py` reciba `context_items` como parámetro.
* `cag.py` aplique el contexto a la respuesta base del RAG.
* `context_used` devuelva las claves de contexto utilizadas.

## 5. Pruebas propias agregadas

Se creó el archivo:

```text
tests/student/test_cag_unit.py
```

Las pruebas propias validan:

* Que `ContextStore` guarde y recupere contexto.
* Que una clave existente pueda actualizarse.
* Que `apply_context` agregue contexto a la respuesta.

Comando ejecutado:

```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/student -p "test_*.py"
```

Resultado:

```text
Ran 3 tests
OK
```

## 6. Validación final

Se validaron:

```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py"
$env:PYTHONPATH="."; python -m unittest tests.validation.test_cag_contract
$env:PYTHONPATH="."; python -m unittest discover -s tests/student -p "test_*.py"
```

Todas las pruebas relevantes pasaron correctamente.
