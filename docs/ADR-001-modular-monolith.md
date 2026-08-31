# ADR-001 — Modular Monolith

**Status:** Accepted

## Contexto

O SISADA possui autenticação, estrutura organizacional, avaliações, analytics, relatórios e IA, mas será inicialmente desenvolvido por uma única pessoa e terá um único núcleo transacional.

## Decisão

Utilizar um monólito modular no backend FastAPI.

## Alternativas consideradas

- microserviços;
- monólito sem separação modular.

## Consequências

### Positivas

- deploy simples;
- transações simples;
- debugging mais fácil;
- menor custo operacional;
- permite separar domínios internamente.

### Negativas

- módulos compartilham processo e banco;
- disciplina arquitetural precisa ser mantida pelo código e reviews.

## Regra

Microserviços só serão considerados se surgir um problema concreto que justifique separação operacional.
