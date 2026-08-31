# ADR-005 — Redis + Celery

**Status:** Accepted, implementação adiada até necessidade real

## Contexto

Geração de relatórios por IA e PDFs pode exceder o tempo aceitável de uma requisição HTTP.

## Decisão

Usar Redis como broker e Celery para background jobs quando essas funcionalidades forem implementadas.

## Consequências

### Positivas

- requisições HTTP não ficam bloqueadas;
- retries e processamento em background;
- arquitetura preparada para tarefas demoradas.

### Negativas

- adiciona processo worker;
- adiciona Redis;
- aumenta complexidade operacional.

## Regra

Não usar Celery para CRUD ou operações rápidas.
