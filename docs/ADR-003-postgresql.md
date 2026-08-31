# ADR-003 — PostgreSQL

**Status:** Accepted

## Contexto

O domínio possui relacionamentos, constraints, histórico, transações, relatórios e dados estruturados.

## Decisão

Utilizar PostgreSQL como banco principal.

## Alternativas consideradas

- SQLite;
- MySQL;
- bancos NoSQL.

## Consequências

### Positivas

- integridade relacional;
- constraints robustas;
- transações;
- JSONB quando necessário;
- índices parciais úteis para memberships ativos.

### Negativas

- exige serviço de banco separado no desenvolvimento/deploy.
