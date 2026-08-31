# ADR-002 — FastAPI

**Status:** Accepted

## Contexto

O produto precisa de uma API Python tipada, documentada e adequada a integração futura com serviços de IA.

## Decisão

Utilizar FastAPI como framework HTTP do backend.

## Consequências

### Positivas

- OpenAPI automática;
- integração direta com Pydantic;
- suporte a async;
- boa adequação ao ecossistema Python/IA.

### Negativas

- autenticação e arquitetura precisam ser definidas explicitamente;
- suporte a async pode induzir complexidade desnecessária se usado sem critério.
