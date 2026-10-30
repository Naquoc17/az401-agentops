---
name: agentops-conventions
description: Coding and testing conventions for the AgentOps FastAPI project. Use when reviewing or writing Python code in app/ or tests/.
---

## Type hints

- Every function has type hints for parameters and return values.
- Test functions use `-> None`.

## Tests

- Every endpoint in app/ has at least one test in tests/.
- Test names follow `test_<endpoint>_<behavior>`.
