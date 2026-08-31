# ADR-004 — React + TypeScript + Vite

**Status:** Accepted

## Contexto

O backend será FastAPI. O frontend precisa ser uma SPA moderna sem introduzir uma segunda camada de backend.

## Decisão

Utilizar React + TypeScript + Vite.

## Alternativas consideradas

- Next.js;
- templates server-side.

## Consequências

### Positivas

- separação clara frontend/backend;
- menor complexidade que Next.js para este projeto;
- aprendizado direto de consumo de API;
- build simples.

### Negativas

- não teremos SSR no MVP;
- autenticação e roteamento são tratados na SPA.
